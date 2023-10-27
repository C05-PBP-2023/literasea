function showAnswerField(id) {
  document.querySelector(`#answer-btn-${id}`).classList.add("hidden");
  document.querySelector(`#answer-field-${id}`).classList.remove("hidden");
}
