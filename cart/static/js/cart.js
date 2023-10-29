// Get the modal
let modal = document.getElementById("myModal");

// Get the button that opens the modal
let btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

let cancel = document.getElementById("button_cancel");

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

cancel.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

async function getCart() {
    return fetch("get-cart/").then((res) => res.json())
}

function checkout(){
    fetch("checkout/",{
        method: "POST",
        body: new FormData(document.querySelector("#checkoutForm"))
    }).then(refreshCart)
    return false
}

function removeBookFromCart(id) {
    fetch(`remove-book/${id}`, {
        method: "POST"
    }).then(refreshCart)

    return false
}

document.getElementById("button_checkout").onclick = function(){
    checkout();
    modal.style.display = "none"
}

async function refreshCart(){
    document.getElementById("cart_content").innerHTML = "";
    
    const cart = await getCart();
    let htmlString = ``;

    let totalBookString = 0;
    let priceString = '';

    if(cart.length == 0){
        btn.disabled = true;
        btn.style.backgroundColor = "gray"
        htmlString += `
            <div class="min-w-[528.44px] ml-[50%] mt-[100px] text-2xl font-bold text-gray-400">Empty cart</div>
        `
        document.getElementById("cart_content").innerHTML += htmlString;
    }else{
        totalBookString+= cart.length;
        cart.forEach(book => {
            htmlString += `
            <div class="flex justify-between bg-white mb-5 hover:bg-[#e4e8ed] px-10 py-5 mt-5 md:mt-0 mx-auto md:min-w-[528.44px] text-sm md:text-base md:ml-0 transition-all duration-500 rounded-md">
                <div class="flex flex-col md:flex-row">
                    <div class="m-5 mr-10">
                        <img src="${book.fields.Image}" width="80px" class="min-w-[50px] md:min-w-[80px]" style="box-shadow: 16px 13px 0px -1px rgba(0,19,78,1);">
                    </div>
                    <div class="flex flex-col m-5 max-w-[300px]">
                        <p class="font-bold">${book.fields.BookTitle}</p>
                        <p>${book.fields.BookAuthor}</p>
                        <p>${book.fields.Year_Of_Publication}</p>
                        <p>${book.fields.Publisher}</p>
                    </div>
                </div>
                <div class="self-end mb-5 ml-5">
                    <a onclick="removeBookFromCart(${book.pk})" class="cursor-pointer" ><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                  </svg>
                  </a>
                </div>
            </div>
            `
        });

        document.getElementById("cart_content").innerHTML = htmlString;
    }

    let totalString = 100*totalBookString;

    document.getElementById("books_total").innerHTML = totalBookString
    document.getElementById("total_price").innerHTML = "Rp"+totalString+",00"
}

refreshCart();

