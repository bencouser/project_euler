#include <stdio.h>
#include <stdlib.h>

int main(){

  int sum;
  int iOne;
  int iTwo;
  int plus;
  int jump = 1;
  
  iTwo = 2;

  sum += 1;
  sum += 2;

  for(iOne = 1; iOne < 2000000; iOne += jump){
    jump = iTwo - iOne;
    plus = iTwo + iOne;
    iOne = iTwo;
    iTwo = plus;
    sum += plus;
    
  }
    
  printf("%d", sum);

  return 0;
}
