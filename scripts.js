// var express = require('express');
// var app = express();
// app.listen(3000, function() {
//     console.log('server running on port 3000');
// } )
// app.get('/mov', callName);
// function callName(req, res) {
    
//     var spawn = require("child_process").spawn;
//     //  http://localhost:3000/mov?movie=nowyouseeme
  
//     var process = spawn('python',["./app.py",req.query.movie] );
  
//     process.stdout.on('data', function(data) {
//         res.send(data.toString());
//     } )
// }

const express = require('express')
const { spawn } = require('child_process')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    let dataToSend
    let largeDataSet = []
    // spawn new child process to call the python script
    const python = spawn('python', ['./app.py'])

    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...')
        //dataToSend =  data;
        largeDataSet.push(data)
    })

    // in close event we are sure that stream is from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`)
        // send data to browser
        res.send(largeDataSet.join(''))
    })
})

app.listen(port, () => {
    console.log(`App listening on port ${port}!`)
})