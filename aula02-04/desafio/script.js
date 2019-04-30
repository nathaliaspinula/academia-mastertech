let menu = document.querySelector("button");
let nav = document.querySelector(".links");

function abrirNav(){
    nav.classList.toggle("mostrarNav");
}

menu.onclick=abrirNav;