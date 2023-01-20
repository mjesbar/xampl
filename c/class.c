#include<stdlib.h>
#include<stdio.h>


typedef struct {

	float radio;
	float (*area)(float);
	//area = area; / we cannot assign the area funtion address to the area pointer due to struct in C
	// don't support neither functions nor funtions assignments
} ball;

// prototypes
float area(float r);

// Class constructor
ball BallClass() {		/* we can also declare this constructor as a pointer '*BallClass()' 
						   and keep in mind that we'll need to use '->' operator to access
						   to members */
	ball instance;
	instance.area = area;
	return instance;
}

// function definitions
float area(float r)	{
	return r * r;
}


int main(void)	{

	ball ball_object = BallClass();
	ball_object.radio = 10.4567;

	printf("radio: %.2lf, area: %.2f", ball_object.radio, ball_object.area(ball_object.radio));

}
