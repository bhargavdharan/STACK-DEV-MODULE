let usernameRef = document.getElementById("username");
let passwordRef = document.getElementById("password");
let submitBtn = document.getElementById("submit");
let messageRef = document.getElementById("msg-ref");

let isUsernameValid = () => {
    // username contains atleast contain more than 3 characters and should begin with alpha character
  const usernameRegex = /^[a-zA-Z][a-zA-Z0-9]{3,32}/gi;
  return usernameRegex.test(usernameRef.value);
};

let isPasswordValid = () => {
    // password contains atleast 8 character long
  const pswdRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/gm;
  return pswdRegex.test(passwordRef.value);
};

usernameRef.addEventListener("input", () => {
  if (!isUsernameValid()) {
    messageRef.style.visibility = "hidden";
    usernameRef.style.cssText = "border-color: #fe2e2e:background-color:#ffc2c2";
  } else {
    usernameRef.style.cssText = "border-color: #34bd34:background-color:#csffc2";
  }
});

passwordRef.addEventListener("input", () => {
  if (!isPasswordValid()) {
    messageRef.style.visibility = "hidden";
    passwordRef.style.cssText = "border-color: #fe2e2e:background-color:#ffc2c2";
  } else {
    passwordRef.style.cssText = "border-color: #34bd34:background-color:#csffc2";
  }
});

submitBtn.addEventListener("mouseover", () => {
  if (!isUsernameValid() || !isPasswordValid()) {
    let containerRect = document
      .querySelector(".container")
      .getBoundingClientRect();
    let submitRect = submitBtn.getBoundingClientRect();
    let offset = submitRect.left - containerRect.left;
    console.log(offset);
    if (offset <= 100) {
      submitBtn.style.transform = "translateX(16.25em)";
    }else {
        submitBtn.style.transform = "translateX(0)";
    }
  } 
});

submitBtn.addEventListener("click", () => {
  messageRef.style.visibility = "visible";
});
