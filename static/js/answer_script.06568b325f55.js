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
      <p class="font-bold text-sm md:text-base">Answer:</p>
      <p class="text-sm md:text-base">${newData.answer}</p>
      <p class="text-xs md:text-sm text-slate-500 mt-4">Answered by ${newData.user}</p>
  </div>`;
}

async function getQuestions() {
  return fetch("get-questions/").then((res) => res.json());
}

async function refreshQuestions() {
  let htmlString = ``;
  let data = await getQuestions();
  for (let i = data.length - 1; i >= 0; i--) {
    el = data[i];
    htmlString += `\n<div class="border flex flex-col justify-between rounded-lg p-4 md:p-6">
    <div class="flex ${
      window.innerWidth <= 768 ? "flex-col" : ""
    } justify-between">
        <div class="flex md:hidden flex-grow justify-start">
        <img class="h-16 md:h-32" src="${el.Image}">
            <div class="ml-4">
                <p class="text-xs font-bold max-w-xs">${el.BookTitle}</p>
                <p class="text-xs text-slate-500">${el.BookAuthor}</p>
            </div>
        </div>
        <div>
            <p class="font-bold md:text-xl mt-2 md:mt-0">${el.title}</p>
            <p class="text-xs md:text-sm text-slate-500">Asked by ${
              el.full_name
            }</p>
            <p class="mt-4 md:mt-6 text-sm md:text-base max-w-sm">${
              el.question
            }</p>
        </div>
        <div class="hidden md:flex flex-grow justify-end">
            <div class="text-end mr-4">
                <p class="text-sm font-bold max-w-xs">${el.BookTitle}</p>
                <p class="text-sm text-slate-500">${el.BookAuthor}</p>
            </div>
            <img class="h-16 md:h-32" src="${el.Image}">
        </div>
    </div>
    <div id="answer-section-${el.id}" class="flex pt-4">`;
    if (el.answered) {
      htmlString += `\n<div>
      <p class="font-bold text-sm md:text-base">Answer:</p>
      <p class="text-sm md:text-base">${el.answer}</p>
      <p class="text-xs md:text-sm text-slate-500 mt-4">Answered by ${el.user_answer}</p>
  </div>`;
    } else {
      if (el.user_type === "reader") {
        htmlString += `\n<p class="text-xs md:text-sm text-slate-500">This question is not yet answered.</p>`;
      } else {
        htmlString += `\n<button id="answer-btn-${
          el.id
        }" onclick="showAnswerField(${
          el.id
        })" class="px-4 py-1 bg-[#005b9c] hover:bg-[#003f7e] text-white text-sm">Answer</button>
        <div id="answer-field-${
          el.id
        }" class="hidden grow flex items-center gap-2 md:gap-4">
            <form id="answer-form-${
              el.id
            }" class="w-full flex items-center" method="POST">
                <textarea class="w-full rounded-md md:rounded-full border resize-none text-xs md:text-sm px-2 md:px-4 py-1.5 md:py-2" rows="1" name="answer" placeholder=${
                  window.innerWidth <= 768
                    ? "Answer..."
                    : "Write your answer..."
                } id="id_answer"></textarea>
            </form>
            <button onclick="addAnswer(${
              el.id
            })" class="hover:text-[#005b9c] rounded-full">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
                </svg>
            </button>
        </div>`;
      }
    }
    htmlString += `\n</div>
  </div>`;
  }

  document.querySelector("#question-display").innerHTML = htmlString;
}

refreshQuestions();
