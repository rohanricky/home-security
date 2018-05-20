const express = require('express');
const bodyParser = require('body-parser');
const comm = require('./comm');

const app = express();
app.use(bodyParser.urlencoded({extended:true})); //req.body args
app.use(bodyParser.json());

app.get('/home/security_cam',isLoggedIn,isFamily,(req,res,next)=>{
    start_security_cam();
});

function start_security_cam() {
    console.log("Starting Security Cam");
    comm.start(function (err, body) {
        if(!err) {
            console.log(body);
        }
    });
}