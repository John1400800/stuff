// цикл for

// обобщённый вид цикла for:

// for (start_point; condition; step) {
//     код для выполнения
// }

for (let i = 0; i < 100; i++) {
  document.writeln(`${i}, `);
  if (i == 45) {
    break;
  }
}

let floors = 28;
for (let i = 1; i <= floors; i++) {
  if (i == 13) {
    // нет такого этажа (floor)
    continue;
  }
  document.write(`${i} `);
}

for (let i = 25; i > 0; i--) {
  document.writeln(`${i} `);
}

for (let i = "a"; i != "aaaaaa"; i += "a") {
  document.writeln(i);
}

// let i = 0;
for (; i < 10; ) {
  document.write(i);
  i++;
}

let i = 0;
let yay = true;
for (; yay; ) {
  if (i == 10) {
    yay = false;
  } else {
    document.write(`${i} `);
    i++;
  }
}
