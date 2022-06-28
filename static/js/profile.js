let images=document.getElementsByClassName('imagesimages')

Array.from(images).forEach(function(element){
    element.addEventListener('click',function(){
        element.classList.add('.popup')
    })
})