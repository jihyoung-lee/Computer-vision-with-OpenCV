#include "opencv2/opencv.hpp"
#include <iostream>  //cout

using namespace std;
using namespace cv;

int main()
{
	Mat img = imread("cat.jpg"); //Mat�� ������ �����԰� ���ÿ� ������ �о��
	Mat gray, res;
	cvtColor(img, gray, COLOR_BGR2GRAY);

	namedWindow("input image");
	imshow("input image", img);

	namedWindow("grayscale image");
	imshow("grayscale image",gray);

	char choice = (char)waitKey(0);

	if (choice == 'e')
	{
		equalizeHist(gray, res);

		namedWindow("equalized image");
		imshow("equalized image",res);

	}
	else if (choice == 'b')
	{
		threshold(gray, res, 127, 255, THRESH_BINARY);

		namedWindow("binary image");
		imshow("binary image", res);
	}

}