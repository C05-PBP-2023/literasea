async function getBook(id) {
    return fetch(`/products/get_book/${id}`).then((res) => res.json());
  }

// Initialization for ES Users
import {
    Modal,
    Ripple,
    initTE,
  } from "tw-elements";
  
  initTE({ Modal, Ripple });