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
        htmlString += `Empty cart`
    }else{
        totalBookString+= cart.length;
        cart.forEach(book => {
            htmlString += `
            <div class="flex justify-between m-5 bg-white">
                <div class="flex">
                    <div class="m-5">
                        <img src="${book.fields.Image}" width="80px" class="min-w-[80px]">
                    </div>
                    <div class="flex flex-col m-5 max-w-[300px]">
                        <p class="font-bold">${book.fields.BookTitle}</p>
                        <p>${book.fields.BookAuthor}</p>
                        <p>${book.fields.Year_Of_Publication}</p>
                        <p>${book.fields.Publisher}</p>
                    </div>
                </div>
                <div class="self-end mb-5 ml-5">
                    <a onclick="removeBookFromCart(${book.pk})" class="cursor-pointer" >Remove From Cart</a>
                </div>
            </div>
            `
        });
    }

    let totalString = 100*totalBookString;

    document.getElementById("cart_content").innerHTML = htmlString
    document.getElementById("books_total").innerHTML = totalBookString
    document.getElementById("total_price").innerHTML = "Rp"+totalString+",00"
}

refreshCart();

