const menu =  document.querySelector('nav ul');
const hamburger = document.getElementById('bars');
// Faire disparaitre le menu
document.getElementById('xmark').addEventListener('click', function(){
    menu.style.display = "none";
});

document.getElementById('bars').addEventListener('click', function(){
    menu.style.display = "block";
});