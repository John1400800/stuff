function Circle(radius) {
  this.radius = radius;

  // protected property
  let defaultLocation = { x: 0, y: 0 };

  // protected method
  let computeOptimumLocation = function () {
    // ...
  };

  this.drow = function () {
    // замыкание
    computeOptimumLocation();

    console.log("drow");
  };

  this.getDefaultLocation = function () {
    console.log(defaultLocation);
  };

  this.setDefaultLocation = function (x, y) {
    defaultLocation.x = x;
    defaultLocation.y = y;
  };
}

let oneCircle = new Circle(15);
oneCircle.getDefaultLocation();
oneCircle.setDefaultLocation(10, 20);
oneCircle.getDefaultLocation();

let twoCircle = new Circle(14);
twoCircle.getDefaultLocation();
