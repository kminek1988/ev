const panels=document.querySelectorAll('.panel')
panels.forEach((panel)=>{//loop on every cards
    console.log(panel)
  panel.addEventListener("mouseover",()=>{//add a click event
    removeActiveClasses()
    panel.classList.add("active");//when i click i add a class style 'active '
  })//
})
function removeActiveClasses(){
    panels.forEach((panel)=>{//when i click in other cards i remove active class on the others panel
        panel.classList.remove("active")
    })
}
  