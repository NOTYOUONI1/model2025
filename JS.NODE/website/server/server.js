const ex = require('express');
const color = require('colors');
const ejs = require('ejs');
const path = require('path');
const app = ex();
const port = process.env.PORT || 9000;


app.set('view engine', 'ejs');


app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
    res.render('we_home');
});

app.get('/Project', (req, res) => {
    res.render('project');
});

app.get('/Project/profile', (req, res) => {
    res.render('profile');
});

app.get('/Project/click', (req, res) => {
    res.render('currenttime');
});

app.get('/Project/Qrcode', (req, res) => {
    res.render('qr code');
});

app.get('/Project/confrompass', (req, res) => {
    res.render('cinform_password');
});

app.get('/project/tesk', (req, res) => {
    res.render('task');
});

app.get('/project/weather', (req, res) => {
    res.render('weather');
});

app.get('/project/LIST', (req, res) => {
    res.render('maing-learing');
});

app.get('/project/OTP', (req, res) => {
    res.render('OTP');
});

app.get('/project/Timer', (req, res) => {
    res.render('timmer');
});

app.use((req,res,next)=>{
    const data = req.url
    if(data !== '/' || '/Project' || '/Project/profile' || '/Project/clock' || '/Project/Qrcode' || '/Project/cinformpass' || '/Project/tesk' || "/project/weather" || '/project/OTP'||'/project/Timer'){
        res.render('invalid')
    } else{
        next()
    }
})

app.listen(port, () => {
    console.log(`Server is running on port ${port}`.green);
});
