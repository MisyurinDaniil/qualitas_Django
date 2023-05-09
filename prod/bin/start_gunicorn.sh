#!/bin/bash
source /home/qualitas/website/venv/bin/activate
exec gunicorn -c "/home/qualitas/website/qualitas_store/gunicorn_config.py" config.wsgi

