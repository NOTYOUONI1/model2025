const EX = require('express');
const path = require('path');
const color = require('colors');
const port = 3000;

const app = EX();

app.get('/', (req, res) => {
    const filePath = path.join(__dirname, 'developer.html');
    res.sendFile(filePath);
});

app.listen(port, () => {
    console.warn('Server started on port 3000'.bgBlue);
});

module.exports = app; // Optional: export the app for testing purposes
