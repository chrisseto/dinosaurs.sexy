var m = require('mithril');

var header = function(contents) {
    return m('.row', [
        m('br'),
        m('.col-md-offset-1.col-md-10', [
            m('.jumbotron[style="text-align:center"]', [
                contents()
            ])
        ])
    ]);
};

var footer = function() {
    return m('footer', [
        m('.container', [
            m('.row', [
                m('.col-md-offset-1.col-md-10', [
                    m('.well.well-sm', 'Footer')
                ])
            ])
        ])
    ]);
};


module.exports = function(headerContents, contents) {
    return [
        m('.container', [
            header(headerContents),
            contents(),
        ]),
        m('br'),
        m('br'),
        footer()
    ];
};
