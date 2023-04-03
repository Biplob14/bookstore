let footer = document.getElementById('footer_large');
let footer_height = footer.scrollHeight;

let navbar = document.getElementById('navbar');
let navbar_height = navbar.scrollHeight;

let content = document.getElementById('content');
let window_height = window.innerHeight;
content.style.minHeight= `${window_height - footer_height - navbar_height}px`;
