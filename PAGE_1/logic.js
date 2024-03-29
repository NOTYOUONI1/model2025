/*class rolls{
    constructor(){
        console.log('parent')
       // this.car = 'rolls'
        this.name = 'rakib'

    }
    slep(){
        console.log('niglt')
    }
    eat(){
        console.log('rice')
    }
}

class eng extends rolls{
    constructor(mk,name){
        console.log('child')
        super(name);
        this.ml = mk
        this.work = 'coing'
        console.log('exit')
    }
    workf(){
        supper.eat();
        console.log('work f')
    }
}

let engobj = new eng('app')*/

/*let data = 'sicret data'

class usr {
    constructor(name,email){
        this.name = name
        this.email = email
    }
    viwe_data(){
        console.log('data')
    }
}

class admin extends usr{
    constructor(name,email){
        super(name,email);
    }

    editedata(){
        data =
    }
}

let student1 = new usr('rakib','sorry')
let student2 = new usr('sakib','mar56969')

let admin1 = new admin('admin','admin@admin')*/
/*function hello(){
    console.log('hello')
}

setTimeout(()=>{
    console.log('h')
},2000)*/

/*function getdata(dataid){
    setTimeout(()=>{
        console.log('data ID',dataid)
    },2000)
}*/
/*let getpromise =()=>{
    return new Promise((rv,rj)=>{
        console.log('i ma a promise');
        rj('network error')
    })
} 

let gpromise = getpromise()

gpromise.then((res)=>{
    console.log('fullfild promise',res)
});
gpromise.catch((rej)=>{
    console.log('promise fullfild but error',rej)
})*/


/*function asyncfunc(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            console.log('some data1')
            resolve('success')
        },4000)
    })
}
function asyncfunc2(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            console.log('some data2')
            resolve('success')
        },4000)
    })
}

function asyncfunc3(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            console.log('some data3')
            resolve('success')
        },4000)
    })
}

asyncfunc()
    .then(()=>{
        return asyncfunc2()
    })
    .then((res)=>{
        return  asyncfunc3()
    })*/

/*function promise(dataid){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            console.log('data id',dataid)
            resolve('success')
        },100)
    })
}

(async function(){
    console.log('data load...')
    await promise(1);
    console.log('data load...')
    await promise(2);
    console.log('data load...')
    await promise(3);
    console.log('data load...')
    await promise(4);
    console.log('successfull')
})()
try{
on()
} catch(err){
    console.log(err)
}*/

const url = "https://api.coindesk.com/v1/bpi/currentprice.json"

const button = document.querySelector("#bin")
const prapa = document.querySelector("#p")

const getfect = async ()=>{
    console.log('getting data...');
    let responce = await fetch(url);
    //let data = await responce.json();
    prapa.innerText = responce

};
button.addEventListener("click",getfect)
