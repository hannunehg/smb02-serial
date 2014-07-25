
#include <stdio.h>


int main()
{
	int i;
	int hwCheck;
	
	hwCheck = system("grep 00000000367e0dc8 /proc/cpuinfo > /dev/null");
	if (hwCheck)
		goto error;

	
	for (i = 0; i < 4; i++)
	{
		// Start sampler

		// Process reading.bin
		system("calc/calc.py >> reading.val");

	}

	// Process reading.val
	system("errorCheck/errorCheck.py > res");
	
	// Format output	
	system("csv/csv.py >> data.csv");

	// clean up
	system("rm reading.val");
	return 0;

	error:
	printf("HW verification fails, check system provider\n");
}
