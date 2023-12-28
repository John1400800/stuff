let prson = {
  _name: "",
  _age: "",

  get name() {
    return _name;
  },

  set name(value) {
    if (value.length > 2) {
      this._name = value;
    } else {
      console.log("Name is too short!");
    }
  },

  get age() {
    return this._age;
  },

  set age(value) {
    if (value < 5) {
      console.log("Too young!");
    } else {
      this._age = value;
    }
  },

  get details() {
    return `Nane: ${this._name}, Age: ${this.age}`;
  },
};

function People(firstName, age) {
  let alphavit = "qwertyuiopasdfghjklzxcvbnm";
  alphavit += alphavit.toUpperCase();

  function isAlphavit(s) {
    if (typeof s !== "string" || s.length == 0) return false;
    for (let i = s.length - 1; i >= 0; i--)
      if (!(s[i] in alphavit)) return false;
    return true;
  }

  this.getFirstName = () => {
    return firstName;
  };

  this.setFirstName = (value) => {
    if (typeof value === "string" && value.length > 2) {
      firstName = value;
    }
  };
}
