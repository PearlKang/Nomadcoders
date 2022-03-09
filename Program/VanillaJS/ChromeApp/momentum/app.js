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


const playerName = "nico";
const playerPoints = 121212;
const playerHandsome = false;
const playerFat = "little bit";

// player[0] == name
// player[1] == points
const player1 = ["nico", 1212, false, "little bit"];

const player = {
    name: "nico", 
    points: 10,
    fat: true,
}
console.log(player);
console.log(player.name);
console.log(player["name"]);

player.fat = false;
console.log(player);

player.lastName = "potato";
player.points = 16;
console.log(player);

player.points = player.points + 16;
console.log(player);


function sayHello() {
    console.log("Hello!");
}

sayHello();

function sayHello2(nameOfPerson) {
    console.log("Hello my name is " + nameOfPerson);
}

sayHello2("nico");
sayHello2("dal");
sayHello2("lynn");

function sayHello3(nameOfPerson, age) {
    console.log("Hello my name is " + nameOfPerson + " and I'm " + age);
}

sayHello3("nico", 10);
sayHello3("dal", 23);
sayHello3("lynn", 21);


function plus1(a, b) {
    console.log(a, b);
}

plus1();

function plus2(a, b) {
    console.log(a + b);
}

plus2();
plus2(8, 60);

function plus3(firstNumber, secondNumber) {
    console.log(firstNumber + secondNumber);
}

plus3();
plus3(8, 60);


function plus(firstNumber, secondNumber) {
    console.log(firstNumber + secondNumber);
}

// console.log(firstNumber);

function divide(a, b) {
    console.log(a / b);
}

plus(60, 8);
divide(98,20);


const players = {
    name: "nico",
    sayHello: function() {
        console.log("hello!");
    },
    sayHello2: function(otherPersonsName) {
        console.log("hello " + otherPersonsName + " nice to meet you!");
    },
}

console.log(players.name);
//console.log(players.sayHello);
//console.log(players.sayHello());
players.sayHello();
players.sayHello2("lynn");
