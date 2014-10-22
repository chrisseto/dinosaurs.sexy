var m = require('mithril');
var userData = require('../models/index.js');


module.exports = function() {
    self = this;

    self.email = m.prop('');
    self.domains = [];
    self.currentDomain = m.prop('');

    self.init = function() {

        m.request({method: "GET", url: "/api/v1/domains"}).then(function(ret) {
            self.domains = ret.availableDomains;
            self.currentDomain(self.domains[0]);
        });
    };

    self.getIt = function(email) {
        m.request({
            method: "POST",
            url: "/api/v1/emails",
            data: {
                'domain': self.currentDomain(),
                'email': self.email()
            }
        }).then(self.gotIt, self.lostIt);
    };

    self.gotIt = function(ret) {
        userData.email(ret.email);
        userData.password(ret.password);
        userData.domain(ret.domain);
        return m.route('/gotit');
    };

    self.lostIt = function() {
        userData.email(self.email());
        userData.domain(self.currentDomain());
        return m.route('/lostit');
    };

    self.init();
};
