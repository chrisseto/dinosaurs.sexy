var getThat = {};
var m = require('mithril');


getThat.view = require('dinosaurs/views/index.js');
getThat.controller = function() {};

m.route(document.body, '/', {
    '/': getThat,
});
