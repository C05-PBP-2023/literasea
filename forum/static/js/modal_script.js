async function showQuestionModal(id) {
  document.querySelector("#modal").classList.remove("hidden");
  document.querySelector("#question-img").src = "";
  const book = await getBook(id);
  document.querySelector("#question-img").src = book[0].fields.Image;
  document.querySelector("#book-title").innerHTML = book[0].fields.BookTitle;
  document.querySelector("#book-author").innerHTML = book[0].fields.BookAuthor;
}

async function getBook(id) {
  return fetch(`/products/get_book/${id}`).then((res) => res.json());
}

function closeModal() {
  modal.classList.add("hidden");
}

document.getElementById("confirm-modal").addEventListener("click", closeModal);
document.getElementById("cancel-modal").addEventListener("click", closeModal);
document.getElementById("modal-panel").addEventListener("click", closeModal);
