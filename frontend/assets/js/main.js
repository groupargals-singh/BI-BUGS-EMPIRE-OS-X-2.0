"use strict";

const toggle = document.querySelector(".nav-toggle");
const navigation = document.querySelector("#primary-navigation");

if (toggle && navigation) {
  toggle.addEventListener("click", () => {
    const isOpen = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!isOpen));
    navigation.classList.toggle("is-open", !isOpen);
  });

  navigation.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      toggle.setAttribute("aria-expanded", "false");
      navigation.classList.remove("is-open");
    }
  });
}
