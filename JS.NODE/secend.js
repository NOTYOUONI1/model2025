const data = require('./API.js')

`document.querySelector('#name').innerHTML=data.data.name
document.querySelector('#age').innerHTML=data.data.age
document.querySelector('#job').innerHTML=data.data.job`
console.log(data.data)