let names = ["marge", "homer", "bart", "lisa", "maggie"];

function firstLatterUpperCase(arr) {
  let newName = [];
  for (let i = 0; i < names.length; i++) {
    newName.push(`${names[i][0].toUpperCase()}${names[i].slice(1)}`);
  }
  return newName;
}

// let newNames = firstLatterUpperCase(names);
// console.log(newNames);
// console.log(names);

console.log([2, 5, 8, 2, 1].sort())