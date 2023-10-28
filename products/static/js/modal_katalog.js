async function showAddBookModal() {
  document.querySelector("#modal").classList.remove("hidden");

  document.getElementById("confirm-modal").onclick = async function () {
      await addBook();
      closeModal();
  };
}

function closeModal() {
  document.querySelector("#form").reset();
  window.location.href="/products";
  document.querySelector("#modal").classList.add("hidden");
}

async function addBook() {
  const form = new FormData(document.querySelector("#form"));
  const response = await fetch("/products/add_book/", {
    method: "POST",
    body: form,
  });

  if (!response.ok) {
    throw new Error("Failed to add book");
  }
  return false;
}


function submitFilterForm() {
  var form = document.getElementById('filterForm');
  form.addEventListener('submit', function() {
    form.reset();
  });
  form.submit();
}

function returnToKatalog(){
  window.location.href="/products";
}

function addToCart() {
  document.getElementById('addToCartButton').addEventListener('click', function () {
      var bookId = this.getAttribute('data-book-id');
      var userId = this.getAttribute('data-user-id');
      returnAddToCart(bookId, userId);
  });
}

function returnAddToCart(bookId, userId) {
  var url = '/products/add_to_cart/' + bookId + '/' + userId + '/';

  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          window.location.href="/products";
      }
  };
  xhr.send();
}
document.addEventListener('DOMContentLoaded', addToCart);


document.getElementById("cancel-modal").addEventListener("click", closeModal);