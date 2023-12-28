const User = {
  name: "Peter",
  email: "peter@lco.dev",
  isActive: true,
};

const createUser = ({ name: string, isPaid: boolean }) => {};
createUser({ name: "Misha", isPaid: "maybe", email: "misha@gmail.com" });
let newUser = { name: "Bill", isPaid: "maybe", email: "misha@gmail.com" };
createUser(newUser);
//      -> ^^^^^^^ <-- (по идее должна быть ошибка) 
// некотрые странности в TypeScript из JS

createUser({ name: "Mariah", isPaid: true });

const createCourse = (): { name: string; price: number } => {
  return { name: "reavt js", price: 399 };
};
