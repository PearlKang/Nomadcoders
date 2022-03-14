/*
const loginForm = document.querySelector("#login-form");
const loginForm = document.getElementById("login-form");
*/
/*
const loginForm = document.getElementById("login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");
*/
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

//handleLoginBtnClick
function onLoginSubmit(event) {
  event.preventDefault();
  console.log(event);
}

loginForm.addEventListener("submit", onLoginSubmit);
