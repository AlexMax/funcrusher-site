CONFIG = {
    'mode': 'wsgi',
    'environment': {
        'PYTHONPATH': '/tmp/funcrusher/lib/python2.6/site-packages',
    },
    'python': '/usr/bin/python',
    'working_dir': '/vagrant',
    'user': 'www-data',
    'group': 'www-data',
    'args': (
        '--bind=127.0.0.1:8000',
        'funcrusher.wsgi:application',
    ),
}
