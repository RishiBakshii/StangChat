const message=document.getElementById('message-container')
window.setInterval(function(){
    message.scrollTop=message.scrollHeight-message.clientHeight

},100)

const toggleButton=document.getElementsByClassName('navbar-toggle')[0];
const navbarlinks=document.getElementsByClassName('navbar-links');

toggleButton.addEventListener('click',function(){
    Array.from(navbarlinks).forEach(function(element){
        element.classList.toggle('active')
    })
})
