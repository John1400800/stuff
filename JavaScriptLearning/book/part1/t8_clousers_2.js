function changeBalance(balance = 0) {
  return function (sum) {
    if (sum) {
      balance += sum;
    } else {
      return balance;
    }
  };
}

let change = changeBalance(10);
change(30);
change(5);
console.log(change());

let change2 = changeBalance();
change2(5);
change2(3);
console.log(change2());
