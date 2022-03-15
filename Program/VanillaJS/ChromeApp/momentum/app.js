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
  const username = loginInput.value;
  loginForm.classList.add("hidden");
  console.log(username);
}

loginForm.addEventListener("submit", onLoginSubmit);
