#!/usr/bin/node

const fs = require('fs');

const file_a = process.argv[2];
const file_b = process.argv[3];
const file_c = process.argv[4];

if (fs.existsSync(file_a) &&
    fs.statSync(file_a).isFile &&
    fs.existsSync(file_b) &&
    fs.statSync(file_b).isFile &&
    file_c !== undefined) {
    const file_a_Content = fs.readFileSync(file_a);
    const file_b_Content = fs.readFileSync(file_b);
    const stream = fs.createWriteStream(file_c);

    stream.write(file_a_Content);
    stream.write(file_b_Content);
    steram.end();
}
