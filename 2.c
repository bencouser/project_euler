#include <stdio.h>
#include <stdlib.h>

int main(){

  int total = 0;
  int i = 1;
  int j = 2;
  int k;

  total += i;
  total += j;
  
  while(j < 4000000){
    k = i + j;
    if(k % 2 == 0){
      total += k; 
    }
    i = j;
    j = k;

  }
    
  printf("The sum of even primes less that 4,000,000 is: %d\n", total);

  return 0;
}
