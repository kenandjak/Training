function even(n: number): number {
  return Math.floor(n / 2);
}

function odd(n: number): number {
  return 3 * n + 1;
}

let n: number = 22;
while (n > 1) {
  if (n % 2 === 0) {
    n = even(n);
  } else {
    n = odd(n);
  }
  console.log(n);
}
