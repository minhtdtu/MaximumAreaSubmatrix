#include <stdio.h>
#include <malloc.h>
#include <time.h>

//////////////////Stack Building///////////////////////////
struct Stack {
    int top;
    unsigned capacity;
    int* array;
};

struct Stack* createStack(unsigned capacity)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
};

int isEmpty(struct Stack* stack)
{
    return (stack->top == -1)?1:0;
}

void push(struct Stack* stack, int item)
{
    stack->array[++stack->top] = item;
}

int pop(struct Stack* stack)
{
    return stack->array[stack->top--];
}

int peek(struct Stack* stack)
{
    return stack->array[stack->top];
}
//////////////////////////End Building Stack//////////////////////////////////////////////

int maxHistogram(int histogram[], int size)
{
	// Stack for storing the index.
    struct Stack* stack = createStack(size);
    int i,curr,width,area,maxArea;
    maxArea = 0;
    area = area = i= 0;
    while(i<size)
	{
		//Advance the index when either the stack is empty or the
        //current height is greater than the top one of the stack.
        if(isEmpty(stack) || histogram[i] > histogram[peek(stack)])
		{
            push(stack, i++);
        }
		else
		{
            curr = pop(stack);
            if (isEmpty(stack)) 
			{
            	width = i;
            	area = histogram[curr] * width;
            }
			else
			{
            	width = (i - peek(stack) - 1);
                area = histogram[curr] * width;
            }
            if (area > maxArea)
			{
                maxArea = area;
            }
        }
    }
	// Clean the stack
    while (!isEmpty(stack))
	{
        curr = pop(stack);

        if (isEmpty(stack))
		{
        	width = i;
            area = histogram[curr] * width;
        }
		else
		{
        	width = (size - peek(stack) - 1);
            area = histogram[curr] * width;
        }
        if(area > maxArea)
		{
            maxArea = area;
        }
    }
    return maxArea;
}

int main()
{
    // Read file input
    FILE *inputFile;
    inputFile = fopen("in.txt", "r");
    char c;
    //count runtime
    //clock_t time_req; 
	//Taking the size value
    c = fgetc(inputFile);
    //Change c char type to int type
    int size = c - '0';
    int matrix[size][size];
    int row, col;
	row = col = 0;
	
	//Taking the matrix as 5 string element
    while (fgetc(inputFile) != EOF)
    {	
    	// Taking input single character at a time 
        c = fgetc(inputFile);
        matrix[row][col++] = c - '0';
        if(col >= size)
		{
            row += 1;
            col = 0;
        }
    }

    fclose(inputFile);
    //////////////////End Read File input/////////////////////////////

    // Find largest Area
    int i,j,area,maxArea;
    maxArea = 0;
    //Create the table to store value
    int lookupTable[size];
    for(i=0; i<size; i++)
	{
        lookupTable[i] = 0;
    }
    //Find len(Lookuptable)
    int lenLookupTable = sizeof(lookupTable)/4;
    
    //Using loop for update the lookupTable
    for(i=0; i<size; i++)
	{
        for(j=0; j<size; j++)
		{
			//If it is "1"
            if(matrix[i][j] > 0)
			{
				//Accumulate the column if if's 1's.
                lookupTable[j] += matrix[i][j];
        	}
			else if (matrix[i][j] == 0)
			{
				//Clean the column if it's 0's.
                lookupTable[j] = 0;
            }
        }
        //Find the update the max variable
        area = maxHistogram(lookupTable, lenLookupTable);
        if(area > maxArea)
		{
            maxArea = area;
        }
        //printf("%d\n",maxArea);
    }

	//Write File output
    FILE *outputFile;
    outputFile = fopen("out.txt", "w");
    fprintf(outputFile,"%d", maxArea);
    fclose(outputFile);
	//////////////////End Write File Output/////////////////////////////
	/*float time = clock() - time_req;
	printf("\n%lf",time);*/
	////////////////////F yeah i'm done/////////////////////////////////
    return 0;
}
