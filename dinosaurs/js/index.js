var getThat = {};
var m = require('mithril');


getThat.view = require('dinosaurs/views/index.js');
getThat.controller = require('dinosaurs/controllers/index.js');

m.route(document.body, '/', {
    '/': getThat,
});
