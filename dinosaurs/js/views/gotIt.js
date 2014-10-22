var m = require('mithril');
var userData = require('../models/index.js');

var header = function() {
    return m('.row', [
        m('br'),
        m('.col-md-offset-1.col-md-10', [
            m('.jumbotron[style="text-align:center"]', [
                m('h1', [
                    'You Got It!',
                    m('br'),
                    m('a[href="mailto:' + userData.email() + '"]', userData.email()),
                ]),
                m('p', [
                    'Your password is "' + userData.password() + '"',
                    m('br'),
                    m('a[href="//mail.' + userData.domain() + '"]', [
                        'Login here'
                    ]),
                    ' and change it.'
                ]),
                m('small', [
                    m('a[href="/"]', 'Get another.')
                ])
            ])
        ])
    ]);
};

module.exports = function(ctrl) {
    if (userData.email() === '') {
        return m.route('/');
    }

    return m('.container', [
        header(),
    ]);
};
