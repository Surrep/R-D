'use strict'

const express = require('express')
const path = require('path')
const port = 3000
const app = express()
const ncp = require('ncp').ncp
const fs = require('fs')


const [nodePath, filePath, appPath] = process.argv

// Pass base app to be copied
if (!fs.existsSync('base')) {
    fs.mkdirSync('base')

    ncp(appPath, 'base/', function (err) {
        if (err)
            return console.error(err);

        console.log('Server initted');
    })
} else console.log('Only one base app allowed')


app.use(function (req, res, next) {
    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', null);

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});

// Launch base pages
app.use("/", express.static("base"))
// Find data
app.use(express.static("/Users/tru/Desktop/photos/"))
app.use(express.static("/Users/tru/Desktop/texts/"))

app.listen(port, function (err) {
    if (err) throw err
    else console.log('HTTP server patiently listening on port', port)
})