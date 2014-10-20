var m = require('mithril');

var header = function() {
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

var emailSelectBtn = function(ctrl) {
    return m('button[data-toggle="dropdown"]', {
        class: 'btn btn-default dropdown-toggle',
        type: 'button',
        style: 'border-bottom-right-radius: 0px;border-top-right-radius: 0px'
    }, [
        '@' + ctrl.currentDomain() + ' ',
        m('span.caret'),
    ]);
};

var emailSelectDropdown = function(ctrl) {
    return m('ul.dropdown-menu[role="menu"]', ctrl.domains.map(function(domain, index) {
        return m('li', [
            m('a[href="#"]', {onclick: m.withAttr('text', ctrl.currentDomain)}, domain)
        ]);
    }));
};

var input = function(ctrl) {
    return m('.row', [
        m('.col-md-offset-1.col-md-10', [
            m('.input-group', [
                m('input.form-control[type="text"'),
                m('.input-group-btn', [
                    emailSelectBtn(ctrl),
                    emailSelectDropdown(ctrl),
                    m('button.btn.btn-success[type="button"]', [
                        m('span.glyphicon.glyphicon-credit-card'),
                        ' Get It!'
                    ])
                ])
            ])
        ])
    ]);
};

module.exports = function(ctrl) {
    return m('.container', [
        header(ctrl),
        input(ctrl)
    ]);
};
