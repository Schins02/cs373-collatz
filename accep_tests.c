
/* ***************************************************************** */
/*                                                                   */
/*                                                                   */
/* ***************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

FILE *input;
FILE *output;

typedef short Boolean;
#define TRUE 1
#define FALSE 0

Boolean debug = FALSE;

typedef char *STRING;

#define CAST(t,e) ((t)(e))
#define TYPED_MALLOC(t) CAST(t*, malloc(sizeof(t)))


Boolean max_cycle(int start, int fin, int max_cycle, long max, int arr[]){
    if(start > fin){
        int temp = start;
        start = fin;
        fin = temp;
    }
    //int start_const = start;
    if( (fin >> 1) > start ){
        start = fin >> 1;
    }
    int v = 1;
    while(start <= fin){
        int num = start;
        v = 1;
        while(num > 1){
            if(num >= 715827882){
                 //printf("start_contst %d\n",start_const );
                return FALSE;  
            }
            if(num % 2 == 0){
                num = num >> 1;
                v++;
            }
            else{
                num = num*3 + 1;
                v++;
            }
        }
        if(v > arr[2])
            arr[2] = v;
        start++;
    }
    return TRUE;
}


/* ***************************************************************** */
/*                                                                   */
/*                                                                   */
/* ***************************************************************** */

int main(int argc, STRING *argv)
{

                input = fopen("john02-RunCollatz.in","w");
                output = fopen("john02-RunCollatz.out", "w");
                long max = pow(2, 31) - 1;
                Boolean valid;
                int num_tests = 1;
                int values[3] = {0, 0, 1};

                while(num_tests <= 1000 ){
                    values[2] = 1;
                    int choice = rand() % 25 + 1;

                    switch(choice){
                        case 1:
                            values[0] = rand() % 10 + 1;
                            values[1] = rand() % 20 + 1;
                            break;
                        case 2:
                          values[0] = rand() % 20 +  1;
                          values[1] = rand() % 40 + 1;
                            break;
                        case 3:
                          values[0] = rand() % 15 +  1;
                          values[1] = rand() % 60 + 1;
                            break;
                        case 4:
                          values[0] = rand() % 15 + 1;
                            values[1] = rand() % 90 + 1;
                            break;
                        case 5:
                           values[0] = rand() % 20 +  1;
                           values[1] = rand() % 170 + 1;
                            break;
                        case 6:
                          values[0] = rand() % 40 +  1;
                            values[1] = rand() % 300 + 1;
                            break;
                        case 7:
                            values[0] = rand() % 100 +  1;
                            values[1] = rand() % 600 + 1;
                            break;
                        case 8:
                            values[0] = rand() % 50000 + 1;
                            values[1] = rand() % 160000 + 1;
                            break;
                        case 9:
                           values[0] = rand() % 100 +  1;
                            values[1] = rand() % 800 + 1;
                            break;
                        case 10:
                          values[0] = rand() % 90 +  1;
                            values[1] = rand() % 900 + 1;
                            break;
                            case 11:
                          values[0] = rand() % 100 +  1;
                            values[1] = rand() % 1000 + 1;
                            break;
                            case 12:
                          values[0] = rand() % 100 +  1;
                            values[1] = rand() % 1300 + 1;
                            break;
                            case 13:
                          values[0] = rand() % 150 +  1;
                            values[1] = rand() % 1500 + 1;
                            break;
                            case 14:
                          values[0] = rand() % 100 +  1;
                            values[1] = rand() % 3000 + 1;
                            break;
                            case 15:
                          values[0] = rand() % 1000 +  1;
                            values[1] = rand() % 6000 + 1;
                            break;
                            case 16:
                          values[0] = rand() % 10000 +  1;
                            values[1] = rand() % 20000 + 1;
                            break;
                            case 17:
                          values[0] = rand() % 10000 +  1;
                            values[1] = rand() % 40000 + 1;
                            break;
                            case 18:
                          values[0] = rand() % 10 +  1;
                            values[1] = rand() % 50000 + 1;
                            break;
                            case 19:
                          values[0] = rand() % 2000 +  1;
                            values[1] = rand() % 60000 + 1;
                            break;
                            case 20:
                          values[0] = rand() % 1000 +  1;
                            values[1] = rand() % 70000 + 1;
                            break;
                              case 21:
                          values[0] = rand() % 12000 +  1;
                            values[1] = rand() % 70000 + 1;
                            break;
                              case 22:
                          values[0] = rand() % 40000 +  1;
                            values[1] = rand() % 115000 + 1;
                            break;
                              case 23:
                          values[0] = rand() % 65000 +  1;
                            values[1] = rand() % 125000 + 1;
                            break;
                              case 24:
                          values[0] = rand() % 1000 +  1;
                            values[1] = rand() % 160000 + 1;
                            break;
                              case 25:
                          values[0] = rand() % 35000 +  1;
                            values[1] = rand() % 160000 + 1;
                            break;

                    }
                    valid = max_cycle(values[0], values[1], values[2], max, values);
                    
                    
                    if(valid){
                        printf("choice %d  --  test num %d (value 1:%d) (value2:%d) max max_cycle %d\n",choice, num_tests,values[0], values[1], values[2] );
                        fprintf(input, "%d %d\n",values[0], values[1] );
                        fprintf(output, "%d %d %d\n",values[0], values[1], values[2] );
                        num_tests++;
                    }
                }
    exit(0);
}
