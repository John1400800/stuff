function addTwo(num: number): number {
  return num + 2;
}

let loginUser = (
  name: string,
  email: string,
  isPaid: boolean = false
): void => {};

const heros = ["thor", "spiderman", "ironman"];
console.log(heros.map((hero: string) => `hero is ${hero}`));

function consoleError(errmsg: string): void {
  console.log(errmsg);
}
function handleError(errmsg: string): never {
  throw new Error(errmsg);
}
