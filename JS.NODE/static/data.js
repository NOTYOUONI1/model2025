const fs = require('fs')
const color = require('colors')

const input = process.argv;

if(input[2]=='add'){
    fs.writeFileSync(input[3]+'txt',input[4])
} else if(input[2]=='remove'){
    fs.unlinkSync(input[3]+'txt',input[4])
} else{
    console.warn('invalid output'.bgBlue)
}