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

getThat.header = function() {
    return m('.row', [
        m('.col-md-offset-1.col-md-10', [
            m('.jumbotron', [
                m('h1', [
                    m('a[href="//getthat.email"]', 'Get That Email')
                ])
            ])
        ])
    ]);
};

getThat.emailSelectBtn = function(ctrl) {
    return m('button.btn.btn-default.dropdown-toggle[type="button"][data-toggle="dropdown"][style="border-bottom-right-radius: 0px;border-top-right-radius: 0px"]', [
        '@' + ctrl.vm.currentDomain() + ' ',
        m('span.caret'),
    ]);
};

getThat.emailSelectDropdown = function(ctrl) {
    return m('ul.dropdown-menu[role="menu"]', ctrl.vm.domains.map(function(domain, index) {
        return m('li', [
            m('a[href="#"]', {onclick: m.withAttr('text', ctrl.vm.currentDomain)}, domain)
        ]);
    }));
};

getThat.input = function(ctrl) {
    return m('.row', [
        m('.col-md-offset-1.col-md-10', [
            m('.input-group', [
                m('input.form-control[type="text"'),
                m('.input-group-btn', [
                    this.emailSelectBtn(ctrl),
                    this.emailSelectDropdown(ctrl),
                    m('button.btn.btn-success[type="button"]', [
                        m('span.glyphicon.glyphicon-credit-card'),
                        ' Get It!'
                    ])
                ])
            ])
        ])
    ]);
};

getThat.view = function(ctrl) {
    return m('.container', [
        this.header(ctrl),
        this.input(ctrl)
    ]);
};

//initialize
m.module(document.body, getThat);
