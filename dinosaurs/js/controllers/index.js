var m = require('mithril');

module.exports = function() {
    self = this;

    self.domains = [];
    self.currentDomain = m.prop('');

    self.init = function() {

        m.request({method: "GET", url: "/api/v1/domains"}).then(function(ret) {
            self.domains = ret.availableDomains;
            self.currentDomain(self.domains[0]);
        });
    };

    self.init();
};
