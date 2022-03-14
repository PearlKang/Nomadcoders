/*
const loginForm = document.querySelector("#login-form");
const loginForm = document.getElementById("login-form");
*/
/*
const loginForm = document.getElementById("login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");
*/
const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");

//handleLoginBtnClic
function onLoginBtnClick() {
  console.log("hello", loginInput.value);
  //console.log("click!!!!");
}

loginButton.addEventListener("click", onLoginBtnClick);
