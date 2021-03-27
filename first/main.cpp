#include "opencv2\opencv.hpp"
using namespace cv;

int main()
{
	Mat img;

	img = imread("a.jpg");
	
	putText(img, "LEE JIHYOUNG", Point(190, 50), FONT_HERSHEY_SIMPLEX, 1, Scalar(0, 0, 0), 1, LINE_AA, false);
	line(img, Point(190, 60), Point(400, 60), Scalar(0, 0, 0));
	line(img, Point(190, 70), Point(400, 70), Scalar(0, 0, 0));
	namedWindow("Hello");
	imshow("Hello", img);

	waitKey(0);

	return 0;



}