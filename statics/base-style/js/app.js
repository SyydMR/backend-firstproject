const menuIcon = document.querySelector(".menu-logo");
const menuBurger = document.querySelector(".menu-burger");
const searchIcon = document.querySelector(".search-logo");
const searchField = document.querySelector(".search-field");
menuIcon.addEventListener("click", showList);
searchIcon.addEventListener("click", showField);

function showList() {
  menuBurger.classList.toggle("show");
}

function showField() {
  searchField.classList.toggle("show");
}
setInterval(functionName, 1000);
function functionName(){
  setTimeout(function() {
    $('#message_container').fadeOut('fast');
  }, 2000);
}

function removeMessage() {
    $('#message_container').fadeOut('fast');
}

 

const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#username");

togglePassword.addEventListener("click", function () {
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    
    this.classList.toggle("bi bi-eye-slash");
});

const form = document.querySelector("form");
form.addEventListener('submit', function (e) {
    e.preventDefault();
});