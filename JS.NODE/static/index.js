const http = require("http")
const color = require('colors')
const data = require("./data.js")
const port = 3000;
const stats = 202

http.createServer((req,resp)=>{
resp.writeHead(stats,{'content-type':'applicition\json'})
    resp.write(JSON.stringify(data))
    resp.end()
}).listen(port,()=>{
    console.warn('started server...'.bgBlue)
})