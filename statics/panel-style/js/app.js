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
