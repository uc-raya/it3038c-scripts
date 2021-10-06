var path = require("path");

var hello = "Hello from Node JS Variable!"
console.log(`Printing variable hello: ${hello}`);

console.log("directory name: " + __dirname);
console.log("directory and file name: " + __filename);

console.log("Using path module:")
console.log(`Hello from file ${path.basename(__filename)}`)

console.log(`Process args: ${process.argv}`)