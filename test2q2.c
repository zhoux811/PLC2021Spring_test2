#include <stdio.h>
#include <time.h>

const int ARRAY_SIZE = 100;

int main()
{

    int arr[ARRAY_SIZE][ARRAY_SIZE];

    int *ptr = &arr[0][0];

    clock_t begin1 = clock();
    for (size_t i = 0; i < ARRAY_SIZE; i++)
    {
        for (size_t j = 0; j < ARRAY_SIZE; j++)
        {
            int a = arr[i][j];
        }
    }
    clock_t end1 = clock();
    double time_spent1 = (end1 - begin1);

    clock_t begin2 = clock();
    for (size_t i = 0; i < ARRAY_SIZE * ARRAY_SIZE; i++)
    {
        int b = *(ptr + i);
    }
    clock_t end2 = clock();
    double time_spent2 = (end2 - begin2);

    printf("referencing via pointer used %lf unit of time,\n\
referencing via pointer used %lf unit of time",
           time_spent1, time_spent2);

    return 0;
}
