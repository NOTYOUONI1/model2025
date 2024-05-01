/*const express = require('express');
const app = express();
const port = process.env.PORT || 8000;

// Set EJS as the view engine
app.set('view engine', 'ejs');

// Import your router
const yourRouter = require('./routers/index');

// Use your router
app.use('/', yourRouter);

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

console.warn(yourRouter); // This line will log the router object to the console
*/

//const { syncIndexes } = require("mongoose")


/*const express = require('express');
const app = express();
const router = require('./routers/index');
const port = process.env.PORT || 8000;

app.set('view engine', 'ejs'); // Corrected typo

app.use(router);

app.listen(port, () => {
    console.warn('Started server...');
});*/

// Define the URL for the CoinGecko API endpoint

// Define the URL for the CoinGecko API endpoint to list all supported coins/markets

// Define the URL for the CoinGecko API endpoint
/*const ex = require('express')
const app = ex()
const port = process.env.PORT || 8000
const router = require('./routers/index')


app.use(router)


app.listen(port,()=>{
  console.log('server started...')
})*/

/*const options = { method: 'GET', headers: { accept: 'application/json' } };

fetch('https://api.fastforex.io/convert?api_key=fd483885c4-3de2a1d3ed-sceexp', options)
  .then(response => response.json())
  .then(data => {
    // Add custom message to the response
    data.msg = 'success';
    console.log(data);
  })
  .catch(err => console.error(err));
*/
/*const fs = require('fs');
const path = require('path');
const dir = path.join(__dirname+'/text.txt');

console.log(dir);

fs.readdir(dir, (err, fils) => {
  if (err) {
    console.error('Error reading directory:', err);
    return;
  }

  fils.forEach((item) => {
    console.log(item);
  });
});*/
/*const fs = require('fs');
const path = require('path');
const color = require('colors')
const dirpath = path.join(__dirname,'pactic');

fs.appendFile(`${dirpath}/apple.txt`,'',(err) => {
  if(err){
    console.log(`error${err}`.bgRed)
  }
  console.log('successfully append text'.bgGreen)
});*/
/*const a = 10

const getdata= new Promise((resolve,reject)=>{
  setTimeout(() => {
    resolve(20)
  }, 2000);
})

getdata.then((data)=>{
  console.log(a+data)
})*/

/*const express = require('express');
const app = express();
const port = 3000;

// Middleware to log incoming requests
app.use((req, res, next) => {
  const url = req.url; // Extracting the URL of the incoming request
  console.warn(url); // Logging the URL of the incoming request

  // Checking if the URL is not equal to '/'
  if (url !== '/') {
    res.send('invalide url')
  } else {
    next(); // Proceeding to the next middleware or route handler
  }
});



// Routes
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
*/

/*const express = require('express');
const path = require('path')
require('dotenv').config();
const app = express();
const port = process.env.PORT || 3000;
const ejs = require('ejs')

app.set("view engine", "ejs")

app.get("/", (req, res) => {
  const data = {
    name: "rakib",
    age: 15
  }
  res.render("index3", data)

});

app.get('/about',(req,res)=>{
  re
})

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
*/
const logic = require('./logic')
console.log(logic)