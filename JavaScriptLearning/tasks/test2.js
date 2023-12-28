function Circle(radius) {
  this.radius = radius;
  let defaultLocation = { x: 0, y: 0 };

  Object.defineProperty(this, "defaultLocation", {
    get: function () {
      return defaultLocation;
    },

    set: function (value) {
      if (!value.x || !value.y) {
        throw new Error("Invalid Locatin.");
      }

      defaultLocation = value;
    },
  });
}

let circle1 = new Circle(12);
console.log(circle1.defaultLocation);
circle1.defaultLocation = {x: 2, y: 3};
console.log(circle1.defaultLocation);

let circle2 = new Circle(12);
console.log(circle2.defaultLocation);
