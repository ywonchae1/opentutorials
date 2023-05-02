const express = require('express')
const app = express()
const fs = require('fs');
const path = require('path');
const sanitizeHtml = require('sanitize-html');
const compression = require('compression');
const bodyParser = require('body-parser');
const topicRouter = require('./routes/topic.js');
const indexRouter = require('./routes/index.js');
const helmet = require('helmet');

app.use(helmet());

app.use(express.static('public'));

app.use(bodyParser.urlencoded({extended: false}));
app.use(compression());
app.get('*', function(request, response, next){
    fs.readdir('./data', function(error, filelist) {
	request.list = filelist;
	next();
    });
});

app.use('/', indexRouter);
app.use('/topic', topicRouter);

app.listen(3000, function() {
    console.log('Example app listening on port 3000!');
});
