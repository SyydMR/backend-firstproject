

function applyTranform6() {
  document.getElementById("lbl6").style.transform = "translate(0, 0)";
  document.getElementById("lbl6").style.color = "black";
  document.getElementById("lbl6").style.transition = "0.3s all";
}

document.addEventListener("DOMContentLoaded", function () {
  const inputElement6 = document.getElementById("count");
  const labelElement6 = document.getElementById("lbl6");
  inputElement6.addEventListener("blur", function () {
    if (inputElement6.value === "") {
      labelElement6.style.transform = "translate(20px, 40px)";
      labelElement6.style.color = "#a8adb3";
    }
  });
});




let container = document.getElementById("container_count");

function btn_count_national_code() {
  const input = document.getElementById("count");
  const inputValue = parseInt(input.value);
  if ((inputValue == null) || (inputValue <= 0)) {
    inputValue = 0
  }
  container.innerHTML = ``;
  for (let i = 0; i < inputValue; i++) {
    container.innerHTML += `
    <div class="div-mellicode inp-div">
        <label class="lbl-mellicode lbl">National Code ` + parseInt(i + 1) + `</label>
        <input name="national_code_` + parseInt(i + 1)  + `" class="inp-mellicode inp" type="text">
    </div>
    `;
  }
}


document.getElementById("radio-1").addEventListener("click", myFunction1, true);
document.getElementById("radio-2").addEventListener("click", myFunction2, true);
document.getElementById("radio-3").addEventListener("click", myFunction3, true);

function myFunction1() {
    document.querySelector(".glider").style.backgroundColor = "#df3e3e";
    document.querySelector(".submit-btn").style.backgroundColor = "#df3e3e";
}
function myFunction2() {
    document.querySelector(".glider").style.backgroundColor = "#a8adb3";
    document.querySelector(".submit-btn").style.backgroundColor = "#a8adb3";
}
function myFunction3() {
    document.querySelector(".glider").style.backgroundColor =
        "rgba(34, 200, 206, 0.7)";
    document.querySelector(".submit-btn").style.backgroundColor =
        "rgba(34, 200, 206, 0.7)";
}




