var getThat = {};

getThat.viewModel = function() {
    self = this;

    self.init = function() {
        self.domains = [];
        self.currentDomain = m.prop('');

        m.request({method: "GET", url: "/api/v1/domains"}).then(function(ret) {
            self.domains = ret.availableDomains;
            self.currentDomain(self.domains[0]);
        });
    };
};


getThat.controller = function() {
    this.vm = new getThat.viewModel();
    this.vm.init();
};



//initialize
m.module(document.body, getThat);
