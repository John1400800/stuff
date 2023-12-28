type User = {
  readonly _id: string;
  name: string;
  email: string;
  isActive: boolean;
  credcardDetails?: number;
};

type cardNumber = {
  cardnumber: string;
};

type cardDate = {
  cardDate: string;
};

// type & type  ▷👍
// {} & {}      ▷👎
type cardDetails = cardNumber &
  cardDate & {
    cvv: number;
  };

let myUser: User = {
  _id: "1245",
  name: "Abraham",
  email: "a@a.eu",
  isActive: false,
};

myUser.email = "abraham@mail.eu";
myUser._id = "LOL";
//     ^^^ (readonly)
