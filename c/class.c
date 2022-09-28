#include<stdlib.h>
#include<stdio.h>



typedef struct ball ball;
struct ball	{

	float radio;
	float (*area)(float);
	//area = qarea;
	
};


float qarea(float r)	{
	return r * r;
}



int main(void)	{


	ball new_ball;
	new_ball.radio = 10.4567;

	printf("radio: %f, area: %f", new_ball.radio, qarea(new_ball.radio));

}
