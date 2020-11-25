(() => {

  const twoToThousand = Math.pow(2, 1000);
  
  //console.log(BigInt(twoToThousand));

  const componentParts = [...String(BigInt(twoToThousand))].map(Number);

  console.log(componentParts.reduce((acc, currentVal) => acc + currentVal));
})();
