var m = require('mithril');
var userData = require('../models/index.js');

var header = function() {
    return m('.row', [
        m('br'),
        m('.col-md-offset-1.col-md-10', [
            m('.jumbotron[style="text-align:center"]', [
                m('h1', [
                    'Oh No!',
                    m('br'),
                    m('small', [
                        'Someone already has ' + userData.email() + '@' + userData.domain(),
                        m('br'),
                        m('a[href="/"]', 'Try another!')
                    ])
                ]),
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
