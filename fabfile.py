from fabric.api import run, env, sudo, cd, prefix

env.hosts = ['45.32.202.126']
env.user = 'felipe'

DIR = '/home/felipe/django-exercise'
VENV = 'source /home/felipe/.virtualenvs/dj-exercise/bin/activate && source SECRETS.ENV'

def start ():
  with cd(DIR):
    with prefix(VENV):
      run('pm2 start uwsgi -- --ini uwsgi.ini > start.log')

def stop ():
  run('pm2 stop all > stop.log')

def deploy ():
  with cd(DIR):
    run('git pull')

    with prefix(VENV):
      run('pip install -r requirements.txt  > install.log')

    run('pm2 restart all > restart.log')

def hello ():
  print("Hello")
