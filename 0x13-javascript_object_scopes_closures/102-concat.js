#!/usr/bin/node

const fs = require('fs');

const file_a = process.argv[2];
const file_b = process.argv[3];
const file_3 = process.argv[4];

if (fs.existsSync(file_1) &&
    fs.statSync(file_1).isFile &&
    fs.existsSync(file_2) &&
    fs.statSync(file_2).isFile &&
    file_3 !== undefined) {
    const file_1_Content = fs.readFileSync(file_1);
    const file_2_Content = fs.readFileSync(file_2);
    const stream = fs.createWriteStream(file_3);

    stream.write(file_1_Content);
    stream.write(file_2_Content);
    steram.end();
}
