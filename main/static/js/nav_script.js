const dropdownContent = document.getElementById("dropdown-content");
const dropdownContentMobile = document.getElementById(
  "dropdown-content-mobile"
);
let justOpened = false;
if (window.innerWidth <= 768) {
  const menuOpenBtn = document.querySelector("#menu-open-btn");
  const menuCloseBtn = document.querySelector("#menu-close-btn");
  const sideMenu = document.querySelector("#side-menu");

  menuOpenBtn.addEventListener("click", () => {
    sideMenu.classList.remove("translate-x-full");
    sideMenu.classList.add("translate-x-0");
  });

  menuCloseBtn.addEventListener("click", () => {
    sideMenu.classList.remove("translate-x-0");
    sideMenu.classList.add("-translate-x-full");
  });
}

const toggleDropdown = (isMobile, isAuthenticated) => {
  if (isMobile) {
    dropdownContentMobile.classList.contains("hidden")
      ? showDropdown(true)
      : closeDropdown(true);
  } else {
    dropdownContent.classList.contains("hidden")
      ? showDropdown(false)
      : closeDropdown(false);
  }
};

const showDropdown = (isMobile) => {
  isMobile
    ? dropdownContentMobile.classList.remove("hidden")
    : dropdownContent.classList.remove("hidden");
  justOpened = true;
};

const closeDropdown = (isMobile) => {
  isMobile
    ? dropdownContentMobile.classList.add("hidden")
    : dropdownContent.classList.add("hidden");
};

if (window.innerWidth <= 768) {
  dropdownContentMobile.addEventListener("click", (event) => {
    event.stopPropagation();
  });
} else {
  dropdownContent.addEventListener("click", (event) => {
    event.stopPropagation();
  });
}

window.onclick = (event) => {
  if (
    !event.target.matches("#dropdown-content") ||
    !event.target.matches("#dropdown-content-mobile")
  ) {
    if (!justOpened) {
      if (window.innerWidth <= 768) {
        if (!dropdownContentMobile.classList.contains("hidden")) {
          console.log("kena");
          closeDropdown(true);
        }
      } else {
        if (!dropdownContent.classList.contains("hidden")) closeDropdown(false);
      }
    }
    justOpened = false;
  }
};
