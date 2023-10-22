const dropdownContent = document.getElementById("dropdown-content");
let justOpened = false;

const toggleDropdown = () => {
  dropdownContent.classList.contains("hidden")
    ? showDropdown()
    : closeDropdown();
};

const showDropdown = () => {
  dropdownContent.classList.remove("hidden");
  justOpened = true;
};

const closeDropdown = () => {
  dropdownContent.classList.add("hidden");
};

dropdownContent.addEventListener("click", (event) => {
  event.stopPropagation();
});

window.onclick = (event) => {
  if (!event.target.matches("#dropdown-content")) {
    if (!dropdownContent.classList.contains("hidden") && !justOpened) {
      closeDropdown();
    }
    justOpened = false;
  }
};
