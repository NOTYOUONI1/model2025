const box = document.querySelectorAll(".box")
const res = document.querySelector(".winner")
const start = document.querySelector(".start")
const reset = document.querySelector(".reset")
const computer = document.querySelector(".fffg")
let compc = 0;
let user = 0;
reset.innerText="COMPUTER 0"
start.innerText="USER 0"
res.innerText="PLAY GAME"

box.forEach((boxl)=>{
    boxl.addEventListener("click",()=>{
        const ss = boxl.getAttribute("id")
        const option = ['rock','papper','sigr']
        const gh = Math.floor(Math.random() * 3)
        let gg = option[gh]
        if(ss === gg){
            res.innerText = "DRW"
        } else if(ss == "rock" && gg == "papper"){
            compc ++;
            reset.innerText=`COMPUTER ${compc}`
            res.innerText = `WINNER COMPUTER`
        }else if(ss == "sicsger" && gg == "rock"){
            compc ++;
            reset.innerText=`COMPUTER ${compc}`
            res.innerText = `WINNER COMPUTER`
        }else if(ss == "papper" && gg == "sigr"){
            compc ++;
            reset.innerText=`COMPUTER ${compc}`
            res.innerText = `WINNER COMPUTER`
        } else{
            user ++
            res.innerText=`YOU ARE WIN`
            start.innerText=`USER ${user}`
        }
        computer.innerText=`COMPUTER ${gg}`
    })
})