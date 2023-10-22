const select_element = document.querySelector("#id_user_type");
const username_field = document.querySelector("#id_username");
const fullname_field = document.querySelector("#id_full_name");
const email_field = document.querySelector("#id_email");
const password = document.querySelector("#id_password1");
const confirm_pass = document.querySelector("#id_password2");

const validateSelect = () => {
  return select_element.value === "";
};

const validateUsername = () => {
  return username_field.value == "";
};

const validateFullName = () => {
  return fullname_field.value == "";
};

const validateEmail = () => {
  return !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(
    email_field.value
  );
};

const validateFirstPassword = () => {
  return password.value == "";
};

const validateSecondPassword = () => {
  return password.value != confirm_pass.value;
};

const validateSelectMsg = () => {
  const res = validateSelect();
  if (res) {
    select_element.classList.add("border-red-500", "focus:outline-red-500");
    document.querySelector("#select-msg").innerHTML = "Choose one!";
  } else {
    select_element.classList.remove("border-red-500", "focus:outline-red-500");
    document.querySelector("#select-msg").innerHTML = "";
  }
  validateFields();
};

const validateUsernameMsg = () => {
  const res = validateUsername();
  if (res) {
    username_field.classList.add("border-red-500", "focus:outline-red-500");
    document.querySelector("#username-msg").innerHTML =
      "Field cannot be empty!";
  } else {
    username_field.classList.remove("border-red-500", "focus:outline-red-500");
    document.querySelector("#username-msg").innerHTML = "";
  }
  validateFields();
};

const validateFullNameMsg = () => {
  const res = validateFullName();
  if (res) {
    fullname_field.classList.add("border-red-500", "focus:outline-red-500");
    document.querySelector("#fullname-msg").innerHTML =
      "Field cannot be empty!";
  } else {
    fullname_field.classList.remove("border-red-500", "focus:outline-red-500");
    document.querySelector("#fullname-msg").innerHTML = "";
  }
  validateFields();
};

const validateEmailMsg = () => {
  const res = validateEmail();
  if (res) {
    email_field.classList.add("border-red-500", "focus:outline-red-500");
    document.querySelector("#email-msg").innerHTML = "Enter a valid email!";
  } else {
    email_field.classList.remove("border-red-500", "focus:outline-red-500");
    document.querySelector("#email-msg").innerHTML = "";
  }
  validateFields();
};

const validateFirstPasswordMsg = () => {
  const res = validateFirstPassword();
  if (res) {
    password.classList.add("border-red-500", "focus:outline-red-500");
    document.querySelector("#pass1-msg").classList.add("text-red-500");
    document.querySelector("#pass1-msg").innerHTML =
      "Password cannot be empty!";
  } else {
    password.classList.remove("border-red-500", "focus:outline-red-500");
    document.querySelector("#pass1-msg").classList.remove("text-red-500");
    document.querySelector("#pass1-msg").innerHTML =
      "Your password must contain at least 8 characters, not entirely numeric and not too common.";
  }
  validateFields();
};

const validateSecondPasswordMsg = () => {
  const res = validateSecondPassword();
  if (res) {
    confirm_pass.classList.add("border-red-500", "focus:outline-red-500");
    document.querySelector("#pass-msg").innerHTML =
      "The two passwords didn't match!";
  } else {
    confirm_pass.classList.remove("border-red-500", "focus:outline-red-500");
    document.querySelector("#pass-msg").innerHTML = "";
  }
  validateFields();
};

function validateFields() {
  const btn = document.getElementById("submit-btn");
  if (
    !(
      validateSelect() ||
      validateUsername() ||
      validateFullName() ||
      validateEmail() ||
      validateFirstPassword() ||
      validateSecondPassword()
    )
  ) {
    btn.disabled = false;
  } else {
    btn.disabled = true;
  }
}
