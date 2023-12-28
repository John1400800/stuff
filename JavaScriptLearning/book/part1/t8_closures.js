// замыкания важна тема про области видимости функций
// замыкания —  позволяют функциям работать, даже
// когда их среда существенно изменяется или исчезает.

function stopWatch() {
  let startTime = Date.now();

  function getDelay() {
    let elapsedTime = Date.now() - startTime;
    console.log(elapsedTime);
  }

  return getDelay;
}

let start = stopWatch(); // начвло секундомера
for (let i = 0; i < 100000; i++) {} // занимает время
let point1 = start(); // сколбко прошло сначала
let point2 = start(); // сколбко прошло сначала
let point3 = start(); // сколбко прошло сначала
