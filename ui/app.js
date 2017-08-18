// Packages
const express = require('express');

// Configurations
var app = express();
app.set('view engine', 'pug');
app.use(express.static('static'));

// Views
app.get('*', function (req, res) {
    var v = req.path.replace(/\//g, '');
    if (v === '') v = 'index';
    res.render(v, null, function (err, html) {
        if (err) {
            res.render('404');
        } else {
            res.send(html);
        }
    });
});

// Start
app.listen(9999, function () {
    console.log('Server started.')
});