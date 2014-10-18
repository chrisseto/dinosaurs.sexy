var getThat = {};

getThat.vm = {};

getThat.vm.init = function() {
    self = this;

    self.domains = [];

    m.request({method: "GET", url: "/api/v1/domains"}).then(function(ret) {
        self.domains = ret.availableDomains;
    });
};


getThat.controller = function() {
    getThat.vm.init();
};

getThat.header = function() {
    return m('.row', [
        m('.col-md-10', [
            m('.jumbotron', [
                m('h1', [
                    m('a[href="//getthat.email"]', 'Get That Email')
                ])
            ])
        ])
    ]);
};

getThat.emailSelectBtn = function() {
    return m('button.btn.btn-default.dropdown-toggle[type="button"][data-toggle="dropdown"][style="border-bottom-right-radius: 0px;border-top-right-radius: 0px"]', [
        'Select a Domain ',
        m('span.caret'),
    ]);
};

getThat.emailSelectDropdown = function() {
    return m('ul.dropdown-menu[role="menu"]', this.vm.domains.map(function(domain, index) {
        return m('li', [
            m('a[href]="#"', domain)
        ]);
    }));
};

getThat.input = function() {
    return m('.row', [
        m('.col-md-10', [
            m('.input-group', [
                m('input.form-control[type="text"'),
                m('.input-group-btn', [
                    this.emailSelectBtn(),
                    this.emailSelectDropdown(),
                    m('button.btn.btn-success[type="button"]', [
                        m('span.glyphicon.glyphicon-credit-card'),
                        ' Get It!'
                    ])
                ])
            ])
        ])
    ]);
};

getThat.view = function() {
    return m('.container', [
        this.header(),
        this.input()
    ]);
};

//initialize
m.module(document.body, getThat);
