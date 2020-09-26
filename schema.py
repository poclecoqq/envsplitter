schema = {
    "paths": {
        'required': True,
        'type': 'list',
        'schema': {'type': 'string'}
    },
    'env_vars': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'name': {
                    'required': True,
                    'type': 'string'
                },
                'destination': {
                    'required': True,
                    'type': 'list',
                    'schema': {'type': 'boolean'}
                },
                'value': {
                    'required': True,
                },
            }
        }
    }

}
