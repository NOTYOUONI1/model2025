const {MongoClient} = require("mongodb")
const url = 'mongodb://127.0.0.1:27017/'
const client = new MongoClient(url)
const color = require('colors')
const v11 = document.querySelector('#name').value
const v22 = document.querySelector('#email').value
const v33 = document.querySelector('#pass').value
const btn = document.querySelector('button')



async function getdata(){
  let result = await client.connect()
  let db = result.db('man')
  let collection = db.collection('man')
  return collection
}

btn.addEventListener('click',()=>{
    console.log('clicked')
})
