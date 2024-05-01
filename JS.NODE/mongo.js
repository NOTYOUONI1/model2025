/*const {MongoClient} = require("mongodb")
const url = 'mongodb://127.0.0.1:27017/'
const client = new MongoClient(url)
const color = require('colors')



async function getdata(){
  let result = await client.connect()
  let db = result.db('man')
  let collection = db.collection('man')
/*  let responce = await collection.find({tag:'t'}).toArray()
  console.log(responce)
  return collection
}

//getdata()

/*getdata().then((res)=>{
  res.find({name:'RAKIB'}).toArray().then((data)=>{
    console.warn(data)
  })
})
*/
/*const main = async()=>{
  let data = await getdata()
  data  = await data.insertOne({name:'RAKIB'}).then(()=>console.log('seuccessfilly insert'))
}
main()*/

/*const insert = async () => {
    let db = await getdata();
    db = await db.insertOne({ name: 'sakil' });
}

insert();*/


/*async function update(v1,v2,v3){
  let data = await getdata()
  let result =await data.insertOne({name:`${v1}`,email:`${v2}`,pass:`${v3}`})
}

module.exports=update*/

const fs = require('fs').promises;
const colors = require('colors');


function getda(){
  try{
    fs.appendFile('hello.txt','\nand my name is rakib')
    console.log('successfully append text'.bgGreen)
  } catch(err){
    console.log(err)
  }
}
getda()
console.log(process.argv[2].bgBlue)