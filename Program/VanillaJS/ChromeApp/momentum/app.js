console.log(123123123);
console.log("testestest");
console.log(5+2);
console.log(5*2);
console.log(5/2);

const a = 5;
const b = 2;
const myName = "nico";
const veryLongVariableName = 0;

console.log(a + b);
console.log(a * b);
console.log(a / b);

let myNames = "nico";
console.log("hello " + myNames);
myNames = "nicolas";
console.log("your new name is " + myNames);

const amIFat = false;
const amIFat2 = null;
const amIFat3 = undefined;
console.log(amIFat);

let something;
console.log(something, amIFat); 

const mon = "mon";
const tue = "tue";
const wed = "wed";
const thu = "thu";
const fri = "fri";
const sat = "sat";
const sun = "sun";

const daysOfWeek = mon + tue + wed + thu + fri + sat + sun;
console.log(daysOfWeek);
const daysOfWeek2 = [mon, tue, wed, thu, fri, sat, sun];

const nonsense = [1, 2, "hello", false, null, true, undefined, "nico"];
console.log(daysOfWeek2, nonsense);

const daysOfWeek3 = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
console.log(daysOfWeek3);

// Get Item from Array
console.log(daysOfWeek3[5]);

// Add one more doy to the array
daysOfWeek3.push("weekday");
console.log(daysOfWeek3);

const toBuy = ["potato", "tomato", "pizza"];
toBuy.push("kimbab");
console.log(toBuy[2]);