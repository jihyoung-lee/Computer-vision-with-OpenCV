#include "opencv2\opencv.hpp"
using namespace cv;

int main()
{
	Mat img;

	img = imread("cat.jpg");
	
	putText(img, "Kim Minyoung", Point(150, 150 ), FONT_HERSHEY_SIMPLEX, 1, Scalar(255, 255, 255), 1, LINE_AA, false);
	line(img, Point(140, 160), Point(400, 160), Scalar(255, 255, 255));
	line(img, Point(140, 170), Point(400, 170), Scalar(255, 255, 255));
	namedWindow("Hello");
	imshow("Hello", img);

	waitKey(0);

	return 0;



}