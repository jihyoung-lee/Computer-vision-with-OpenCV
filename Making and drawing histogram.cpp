#include "opencv2/opencv.hpp"
#include <iostream>  //cout

using namespace std;
using namespace cv;

int main()
{
	Mat img = imread("cat.jpg"); //Mat형 변수를 선언함과 동시에 파일을 읽어옴
	Mat gray, res;
	cvtColor(img, gray, COLOR_BGR2GRAY);

	namedWindow("input image");
	imshow("input image", img);

	namedWindow("grayscale image");
	imshow("grayscale image",gray);

	char choice = (char)waitKey(0); //waitKey 함수를 사용자가 누른 키의 문자열을 반환하는 함수

	if (choice == 'e')
	{
		equalizeHist(gray, res); //히스토그램 평활화를 적용한 후 결과를 res에 저장

		namedWindow("equalized image");
		imshow("equalized image",res);

	}
	else if (choice == 'b')
	{
		threshold(gray, res, 127, 255, THRESH_BINARY);// 세번째 파라미터를 임계값으로 하여 이진영상 res 생성

		namedWindow("binary image");
		imshow("binary image", res);
	}
	else if (choice == 'h')
	{
		int channels[1] = { 0 };
		Mat histo;
		int histsize[1]={ 256 };
		float hranges[2] = { 0.0f,256.0f };
		const float* ranges[1] = { hranges };

		calcHist(&gray, 1, channels, Mat(), histo, 1, histsize, ranges);

		double vmax, vmin;

		minMaxLoc(histo, &vmin, &vmax, 0, 0);
		res = Mat::ones(256, 256, CV_8U) * 255;

		for (int i = 0; i < histsize[0]; i++)
		{
			line(res, Point(i, 256), Point(i, 256 - (int)((histo.at<float>(i) / vmax) * (0.8 * 256))), Scalar(0, 0, 0));

		}
		namedWindow("histogram");
		imshow("histogram", res);
	}	
	else
	{
		cout << "Error:";
		exit(0);
	}
}