command = '/home/qualitas/website/venv/bin/gunicorn'
pythonpath = '/home/qualitas/website/qualitas_store/'
bind = '127.0.0.1:8001'
workers = 3
user = 'qualitas'
limit_request_fields = 32000
limit_request_fields_size = 0
rav_env = 'DJANGO_SETTINGS_MODULE=config.settings'
