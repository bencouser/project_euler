#include <stdio.h>
#include <stdlib.h>

int main(){

  int N = 999;
  int i;
  int sum = 0;

  for(i = 0; i <= N; i++){
    if(i%3 == 0){
      sum += i;
    }
    if(i%5 == 0){
      sum += i;
    }
    if(i%15 == 0){
      sum += -i;
    }
  }

  printf("%d\n", sum);

  return 0;
}
