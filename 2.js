(() => {

const limit =4000000;

let sum = 2;
let x = 1, y = 2, fib;

while (x < limit){
  fib = x + y;
  x = y;
  y = fib;
  if (fib % 2 === 0) sum += fib;
}
console.log(sum);
})();
