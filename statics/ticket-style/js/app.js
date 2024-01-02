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

function change_loc(url) {
  document.location.href = url;
}

function applyTranform1() {
  document.getElementById("lbl1").style.transform = "translate(0, 0)";
  document.getElementById("lbl1").style.color = "black";
  document.getElementById("lbl1").style.transition = "0.5s all";
  document.getElementById("lbl1").style.fontSize = "24px";
}

function applyTranform2() {
  document.getElementById("lbl2").style.transform = "translate(0, 0)";
  document.getElementById("lbl2").style.color = "black";
  document.getElementById("lbl2").style.transition = "0.5s all";
  document.getElementById("lbl2").style.fontSize = "24px";
}

function applyTranform3() {
  document.getElementById("lbl3").style.transform = "translate(0, 0)";
  document.getElementById("lbl3").style.color = "black";
  document.getElementById("lbl3").style.transition = "0.5s all";
  document.getElementById("lbl3").style.fontSize = "24px";
}

function applyTranform4() {
  document.getElementById("lbl4").style.transform = "translate(0, 0)";
  document.getElementById("lbl4").style.color = "black";
  document.getElementById("lbl4").style.transition = "0.5s all";
  document.getElementById("lbl4").style.fontSize = "24px";
}

function applyTranform5() {
  document.getElementById("lbl5").style.transform = "translate(0, 0)";
  document.getElementById("lbl5").style.color = "black";
  document.getElementById("lbl5").style.transition = "0.5s all";
  document.getElementById("lbl5").style.fontSize = "24px";

}

function applyTranform6() {
  document.getElementById("lbl6").style.transform = "translate(0, 0)";
  document.getElementById("lbl6").style.color = "black";
  document.getElementById("lbl6").style.transition = "0.5s all";
  document.getElementById("lbl6").style.fontSize = "24px";
}

document.addEventListener("DOMContentLoaded", function () {
  const inputElement1 = document.getElementById("fname");
  const inputElement2 = document.getElementById("lname");
  const inputElement3 = document.getElementById("origin");
  const inputElement4 = document.getElementById("phone");
  const inputElement5 = document.getElementById("date");
  const inputElement6 = document.getElementById("mellicode");
  const labelElement1 = document.getElementById("lbl1");
  const labelElement2 = document.getElementById("lbl2");
  const labelElement3 = document.getElementById("lbl3");
  const labelElement4 = document.getElementById("lbl4");
  const labelElement5 = document.getElementById("lbl5");
  const labelElement6 = document.getElementById("lbl6");

  inputElement1.addEventListener("blur", function () {
    if (inputElement1.value === "") {
      labelElement1.style.transform = "translate(20px, 40px)";
      labelElement1.style.color = "#a8adb3";
      labelElement2.style.fontSize = "20px";
      
    }
  });
  inputElement2.addEventListener("blur", function () {
    if (inputElement2.value === "") {
      labelElement2.style.transform = "translate(20px, 40px)";
      labelElement2.style.color = "#a8adb3";
      labelElement2.style.fontSize = "20px";

    }
  });
  inputElement3.addEventListener("blur", function () {
    if (inputElement3.value === "") {
      labelElement3.style.transform = "translate(20px, 40px)";
      labelElement3.style.color = "#a8adb3";
      labelElement3.style.fontSize = "20px";

    }
  });
  inputElement4.addEventListener("blur", function () {
    if (inputElement4.value === "") {
      labelElement4.style.transform = "translate(20px, 40px)";
      labelElement4.style.color = "#a8adb3";
      labelElement4.style.fontSize = "20px";

    }
  });
  inputElement5.addEventListener("blur", function () {
    if (inputElement5.value === "") {
      labelElement5.style.transform = "translate(20px, 40px)";
      labelElement5.style.color = "#a8adb3";
      labelElement5.style.fontSize = "20px";
    }
  });
  inputElement6.addEventListener("blur", function () {
    if (inputElement6.value === "") {
      labelElement6.style.transform = "translate(20px, 40px)";
      labelElement6.style.color = "#a8adb3";
      labelElement6.style.fontSize = "20px";
    }
  });
});

document.getElementById("radio-1").addEventListener("click", myFunction1, true);
document.getElementById("radio-2").addEventListener("click", myFunction2, true);
document.getElementById("radio-3").addEventListener("click", myFunction3, true);

function myFunction1(){
  document.querySelector(".glider").style.backgroundColor = "#df3e3e";
  document.querySelector(".submit-btn").style.backgroundColor = "#df3e3e";

}
function myFunction2(){
  document.querySelector(".glider").style.backgroundColor = "#a8adb3";
  document.querySelector(".submit-btn").style.backgroundColor = "#a8adb3";

}
function myFunction3(){
  document.querySelector(".glider").style.backgroundColor = "rgba(34, 200, 206, 0.7)";
  document.querySelector(".submit-btn").style.backgroundColor = "rgba(34, 200, 206, 0.7)";

}
