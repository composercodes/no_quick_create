{
    "name": "No Quick Edit / Create",
    "version": "16.0.0.0.0",
    "category": "Web",
    "author": "Maged Ibrahim",
    "website": "",
    "license": "AGPL-3",
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
