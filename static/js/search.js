
const toggleButton=document.getElementsByClassName('navbar-toggle')[0];
const navbarlinks=document.getElementsByClassName('navbar-links');

toggleButton.addEventListener('click',function(){
    Array.from(navbarlinks).forEach(function(element){
        element.classList.toggle('active')
    })
})
let chatpopup=document.getElementById('chat')

chatpopup.addEventListener('click',function(){
    let popup=document.getElementById('chatpopupbox')
    popup.classList.add('showchatpopup')
})

let closeee=document.getElementById('closechatpopup').addEventListener('click',function(){
    let popup=document.getElementById('chatpopupbox')
    popup.classList.remove('showchatpopup')
})
