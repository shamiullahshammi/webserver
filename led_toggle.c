#include <stdio.h>
#include <stdlib.h>	//to use system()
#include <string.h> //to use strcpy()
#include <unistd.h>
int main()
{
	char command[100];
	char command2[100];
	char command3[100];
	char command4[100];

	
	//executing ls command
	strcpy(command, "echo 43 > /sys/class/gpio/export");
	system(command);
	strcpy(command2, "echo out > /sys/class/gpio/gpio43/direction");
	system(command2);
	while(1)
	{
	
	strcpy(command3, "echo 1 > /sys/class/gpio/gpio43/value");
        system(command3);
	usleep(1000000);
	strcpy(command4, "echo 0 > /sys/class/gpio/gpio43/value");
        system(command4);
	usleep(1000000);

	}
	return 0;
}
