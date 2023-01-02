const navbar=document.getElementById("hamb")
let open=false
const hamburger=document.querySelector(".dropdown")
navbar.addEventListener("click", function(){
open=!open
if (open == true){
    hamburger.style.display="block"
}
else{
    hamburger.style.display="none"
}
})
