async function showQuestionModal(id) {
  document.querySelector("#modal").classList.remove("hidden");
  document.querySelector("#question-img").src = "";
  const book = await getBook(id);
  document.querySelector("#question-img").src = book[0].fields.Image;
  document.querySelector("#book-title").innerHTML = book[0].fields.BookTitle;
  document.querySelector("#book-author").innerHTML = book[0].fields.BookAuthor;
  document.getElementById("confirm-modal").onclick = function () {
    addQuestion(id);
  };
}

async function getBook(id) {
  return fetch(`/products/get_book/${id}`).then((res) => res.json());
}

function closeModal() {
  document.querySelector("#form").reset();
  document.querySelector("#modal").classList.add("hidden");
}

async function addQuestion(id) {
  form = new FormData(document.querySelector("#form"));
  form.append("id", id);
  await fetch("/forum/add-question/", {
    method: "POST",
    body: form,
  });

  document.querySelector("#form").reset();
  window.location.href = "/forum/";
  return false;
}

document.getElementById("cancel-modal").addEventListener("click", closeModal);
document.getElementById("modal-panel").addEventListener("click", closeModal);
