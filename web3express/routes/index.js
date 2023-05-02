const express = require('express');
const router = express.Router();
const qs = require('querystring');
const template = require('../lib/template.js');

router.get('/', function(request, response) {
  var title = 'Welcome';
  var description = 'Hello, Node.js';
  var list = template.list(request.list);
  var html = template.HTML(title, list,
    `<h2>${title}</h2>${description}
      <img src="images/Capture.PNG" style="width:300px; display:block; margin-top:30px>"`,
    `<a href="/topic/create">create</a>`
  );
  response.send(html);
});

module.exports = router;
