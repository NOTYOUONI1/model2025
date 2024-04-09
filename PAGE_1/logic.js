const fs = require('fs')

const b = fs.writeFile('damo.txt',"gg",()=>{
    console.log('Written to the file')
})

const a = fs.readFileSync('damo.txt')
console.log(a.toString())