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

    if(cart.length == 0){
        btn.disabled = true;
        htmlString += `Empty cart`
    }else{
        cart.forEach(book => {
            htmlString += `
            <div class="flex m-5 bg-white">
                <div class="m-5">
                    <img src="${book.fields.Image}" width="80px">
                </div>
                <div class="m-5">
                    <p>${book.fields.BookTitle}</p>
                    <p>${book.fields.BookAuthor}</p>
                    <p>${book.fields.Year_Of_Publication}</p>
                    <p>${book.fields.Publisher}</p>
                    ${book.pk}
                </div>
                <div class="items-center">
                    <a onclick="removeBookFromCart(${book.pk})">Remove From Cart</a>
                </div>
            </div>
            `
        });
    }

    document.getElementById("cart_content").innerHTML = htmlString
}

refreshCart();

