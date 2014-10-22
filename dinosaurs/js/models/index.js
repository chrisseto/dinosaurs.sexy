var m = require('mithril');

var user = {
    email: m.prop(''),
    password: m.prop(''),
    domain: m.prop('')
};

module.exports = user;
