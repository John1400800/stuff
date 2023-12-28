// Ниже описанны разные подходы к созданию обьектов
// Factory function:
function createCircle(radius) {
  return {
    radius,
    drow: function () {
      console.log("drow");
    },
  };
}
const circle = createCircle(5);

// Constructor function:
function Circle(radius) {
  console.log("this", this);
  this.radius = radius;
  this.drow = function () {
    console.log("drow");
  };
  // нет искуственного возврата себя
  // это произойдёт с опиратором new
  return this; // не нужно писать return this возвращяет оператор new
}

const another = new Circle(24);

