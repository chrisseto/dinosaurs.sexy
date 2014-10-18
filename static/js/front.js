var getThat = {};

getThat.controller = function() {

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

getThat.input = function() {
    return m('.row', [
        m('.col-md-10', [
            m('.input-group', [
                m('input.form-control[type="text"'),
                m('.input-group-btn', [
                    m('button.btn.btn-success[type="button"', [
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
