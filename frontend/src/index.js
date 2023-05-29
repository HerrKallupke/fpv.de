const express = require('express');
const multer = require('multer');
const axios = require('axios');
const https = require('https');
const fs = require('fs');

const { PORT, API_PORT, CERTIFICATE, PRIVATE_KEY } = require('../config.json');

const upload = multer();
const app = express();
app.set('view engine', 'pug');
app.set('views', './views');
app.use(express.static('./static'));

app.get('/', (req, res) => {
    res.render('index', { title: 'fpv.de - FPV Equipment aus Deutschland' });
});

app.post('/search', upload.none(), (req, res) => {
    const query = req.body.query;

    if (query == ''){
        res.render('index', { message: 'Du musst etwas eingeben!' });
    }else {
        axios.get(`http://127.0.0.1:${API_PORT}/${query}`, { headers: { 'Content-Type': 'application/json' } }).then(result => {
            res.render('results', { data: result.data });
        });
    }
});

const certificate = fs.readFileSync(CERTIFICATE);
const privateKey = fs.readFileSync(PRIVATE_KEY);

https.createServer({ cert: certificate, key: privateKey }, app).listen(PORT);