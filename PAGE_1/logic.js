const box = document.querySelectorAll(".box")

box.forEach((boxl)=>{
    boxl.addEventListener("click",()=>{
        const ss = boxl.getAttribute("id")
        console.log(ss)
        const gg = ()=>{
            const option = ['rock','papper','sigr']
            const gh = Math.floor(Math.random() * 3)
            return option[gh]
        }
        console.log(gg())
        if(ss === gg()){
            console.log("d")
        }
    })
})