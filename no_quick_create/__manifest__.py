{
    "name": "No Quick Edit / Create",
    "version": "16.0.0.0.0",
    "category": "Web",
    'description': """This Module allow quick create and edit depend on user group""",
    "author": "ComposerCodes",
    "website": "",
    "license": "LGPL-3",
    "price": 5.00,
    "currency": "EUR",
    "depends": ["web"],
    'data': [
        'security/security.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "no_quick_create/static/src/components/relational_utils.esm.js",
        ]
    },
    "installable": True,
}
