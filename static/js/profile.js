let images=document.getElementsByClassName('imagesimages')

Array.from(images).forEach(function(element){
    element.addEventListener('click',function(){
        element.classList.add('.popup')
    })
})

// new code form here
const followingpopup=document.querySelector('.followingpopup')
const following=document.getElementById('following').addEventListener('click',function(){
    followingpopup.classList.toggle('showfollowingpopup')
})
const followerspopup=document.querySelector('.followerspopup')
const followers=document.getElementById('followers').addEventListener('click',function(){
    followerspopup.classList.toggle('showfollowerspopup')
})