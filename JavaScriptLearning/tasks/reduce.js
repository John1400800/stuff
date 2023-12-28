const reduce = (arr, func, initialValue = null) => {
  let i = 0;
  initialValue == null ? ((initialValue = arr[0]), (i = 1)) : 0;
  for (i; i < arr.length; i++) {
    initialValue = func(initialValue, arr[i]);
  }
  return initialValue;
};

console.log([1, 2, 3, 4].reduce((total, current) => total + current));
console.log(reduce([1, 2, 3, 4], (total, current) => total + current));
