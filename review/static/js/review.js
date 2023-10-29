async function showReviewModal(id) {
  document.querySelector("#modal").classList.remove("hidden");
  document.querySelector("#review-img").src = "";
  const book = await getBook(id);
  document.querySelector("#review-img").src = book[0].fields.Image;
  document.querySelector("#book-title").innerHTML = book[0].fields.BookTitle;
  document.querySelector("#book-author").innerHTML = book[0].fields.BookAuthor;
  document.getElementById("aplot").onclick = function () {
    addReview(id);
  };
}

async function getBook(id) {
  return fetch(`/products/get_book/${id}`).then((res) => res.json());
}

function closeModal() {
  document.querySelector("#form").reset();
  document.querySelector("#modal").classList.add("hidden");
}

async function addReview(id) {
  form = new FormData(document.querySelector("#form"));
  form.append("id", id);
  await fetch("/review/add-review/", {
    method: "POST",
    body: form,
  });

  document.querySelector("#form").reset();
  window.location.href = "/review/";
  return false;
}

document.getElementById("aplot").addEventListener("click", closeModal);
document.getElementById("gagal").addEventListener("click", closeModal);