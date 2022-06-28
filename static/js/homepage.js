const showsugg=document.getElementById('showsuggestions')
showsugg.addEventListener('click',function(){
    let suggwindow=document.getElementById('suggestion-window')
    suggwindow.classList.add('showsuggwindow')
})

const closesuggbtn=document.getElementById('closesuggbtn')
closesuggbtn.addEventListener('click',function(){
    let suggwindow=document.getElementById('suggestion-window')
    suggwindow.classList.remove('showsuggwindow')
})



const chatpopup=document.getElementById('openchat')

chatpopup.addEventListener('click',function(){
    let popup=document.getElementById('chatpopupbox')
    popup.classList.add('showchatpopup')

})

let closeee=document.getElementById('closechatpopup').addEventListener('click',function(){
    let popup=document.getElementById('chatpopupbox')
    popup.classList.remove('showchatpopup')
})


const toggleButton=document.getElementsByClassName('navbar-toggle')[0];
const navbarlinks=document.getElementsByClassName('navbar-links');

toggleButton.addEventListener('click',function(){
    Array.from(navbarlinks).forEach(function(element){
        element.classList.toggle('active')
    })
})
let pos=document.querySelector('.post-container')
ypos=localStorage.getItem('pos')
pos.scrollTo(0,ypos)


const videobtn=document.getElementById('postvideo')
const videopopupbackbtn=document.getElementById('videopopupbackbtn')

videopopupbackbtn.addEventListener('click',function(){
    let newvideopopup=document.getElementById('newvideopopup')
    newvideopopup.classList.remove('showvideopopup')
})


videobtn.addEventListener('click',function(){
    let newvideopopup=document.getElementById('newvideopopup')
    newvideopopup.classList.add('showvideopopup')
})


// for getting current scroll position from each like button
let likebtn=document.getElementsByClassName('like-img')

Array.from(likebtn).forEach(function(element){
    element.addEventListener('click',function(){
        let pos=document.querySelector('.post-container')
        localStorage.setItem('pos',pos.scrollTop)
    })
})

let stanglike=document.getElementsByClassName('stanglikebtn')

Array.from(stanglike).forEach(function(element){
    element.addEventListener('click',function(){
        let pos=document.querySelector('.post-container')
        localStorage.setItem('pos',pos.scrollTop)
    })
})

// to open the post popup
let newpost_btn=document.getElementById('newpost').addEventListener('click',function(){
    let popup=document.getElementById('newpostpopup')
    popup.classList.add('show')
})

// to close the post popup
let newpostbackbtn=document.getElementById('postpopupbackbtn').addEventListener('click',function(){
    let ff=document.getElementById('newpostpopup')
    ff.classList.remove('show')
})


//to open the new stang pop up
let newstang=document.getElementById('newstang').addEventListener('click',function(){
    let newstangpopup= document.getElementById('newstangpopup')
    newstangpopup.classList.add('show')
})

// to close the new stang popup
let stangbackbtn=document.getElementById('stangpopupbackbtn').addEventListener('click',function(){
    let newstangpopup= document.getElementById('newstangpopup')
    newstangpopup.classList.remove('show')
})



//topline animation here
const topline=document.getElementById('topline')

let stangchat=document.getElementById('stangchat')

stangchat.addEventListener('mouseenter',function(){
    topline.style.width='14rem'
})
stangchat.addEventListener('mouseleave',function(){
    topline.style.width='0rem'
  
})


let about=document.getElementById('about')
about.addEventListener('mouseenter',function(){
    topline.style.width='21rem'

})
about.addEventListener('mouseleave',function(){
    topline.style.width='0rem'
    
})

let chat=document.getElementById('chat')
chat.addEventListener('mouseenter',function(){
    topline.style.width='28rem'
   
})
chat.addEventListener('mouseleave',function(){
    topline.style.width='0rem'
 
})
let logout=document.getElementById('logout')
logout.addEventListener('mouseenter',function(){
    topline.style.width='37rem'

})
logout.addEventListener('mouseleave',function(){
    topline.style.width='0rem'

})

// let img=document.getElementsByClassName('mainpost')

// Array.from(img).forEach(function(element){
//     element.addEventListener('dblclick',function(){
//         let like=document.getElementsByClassName('.testlike')
//         Array.from(like).forEach(function(element){
//             element.click()
//         })
//     })
// })

// let comment=document.getElementsByClassName('commentcomment')

// Array.from(comment).forEach(function(element){
//     element.addEventListener('click',function(){
//         let showcommentpopup=document.getElementById('commentbox')
//         showcommentpopup.classList.add('showcommentbox')
//     })
// })

let options=document.getElementsByClassName('postoptions')

Array.from(options).forEach(function(element){
    element.addEventListener('mouseleave',function(){
        let list=document.getElementsByClassName('option1')
        Array.from(list).forEach(function(element){
            element.classList.remove('showdelete')
        })
    })
    element.addEventListener('click',function(){
        let list=document.getElementsByClassName('option1')
        Array.from(list).forEach(function(element){
            element.classList.add('showdelete')
        })
    })
})




const modal =document.querySelector('.modal')
const previews= document.querySelectorAll('.mainpost')
const imgtext=document.querySelector('popanimationcaption')
const original=document.querySelector('.full-img')

Array.from(previews).forEach(function(element){
    element.addEventListener('click',function(e){
        modal.classList.add('open')
        original.classList.add('imageopen')
        //dynamic chnage text and image
        const originalsrc=element.getAttribute('src')
        original.setAttribute('src',`${originalsrc}`)
    })
})

modal.addEventListener('click',function(e){
    if (e.target.classList.contains('modal')){
        modal.classList.remove('open');
        original.classList.remove('imageopen')
    }
})











