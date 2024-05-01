const fs = require('fs');

fs.writeFile('uploads/hello.txt', 'rakib', (err) => {
    if (err) {
        console.warn(err);
    } else {
        console.log('Data written successfully!');
    }
});
