function Circle(radius) {
  this.radius = radius;
  this.drow = function () {
    console.log("drow");
  };
}

const Circle1 = new Function(
  "radius",
  `
this.radius = radius;
  this.drow = function () {
    console.log("drow");
  };
`
);

const circle = new Circle1(6);
const another = new Circle(6);

console.log(circle)
console.log('\n')
console.log(another)

