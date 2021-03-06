window.$ = window.jQuery = require('jquery');
require('bootstrap/dist/js/bootstrap.js');

var m = require('mithril');

var getThat = {};
var gotThat = {};
var lostThat = {};

getThat.view = require('dinosaurs/views/index.js');
getThat.controller = require('dinosaurs/controllers/index.js');

gotThat.view = require('dinosaurs/views/gotIt.js');
gotThat.controller = function() {};

lostThat.view = require('dinosaurs/views/lostIt.js');
lostThat.controller = function() {};

m.route(document.body, '/', {
    '/': getThat,
    '/gotit': gotThat,
    '/lostit': lostThat
});
