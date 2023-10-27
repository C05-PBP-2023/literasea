function showAnswerField(id) {
  document.querySelector(`#answer-btn-${id}`).classList.add("hidden");
  document.querySelector(`#answer-field-${id}`).classList.remove("hidden");
}

async function addAnswer(id) {
  form = new FormData(document.querySelector(`#answer-form-${id}`));
  form.append("id", id);
  await fetch("/forum/add-answer/", {
    method: "POST",
    body: form,
  });

  document.querySelector(`#answer-form-${id}`).reset();
  changeCardData(id);
  return false;
}

async function changeCardData(id) {
  const newData = await fetch(`/forum/get-answer/${id}`).then((res) =>
    res.json()
  );
  document.querySelector(`#answer-section-${id}`).innerHTML = `\n<div>
<p class="font-bold">Answer:</p>
<p>${newData.answer}</p>
<p class="text-sm text-slate-500 mt-4">Answered by ${newData.user}</p>
</div>`;
}
