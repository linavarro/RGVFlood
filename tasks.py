#!/usr/bin/env python3

from invoke import task
import os
from os import system, getenv
import sys, shutil
from dotenv import load_dotenv
from invoke import Responder

IS_ANDROID: bool = hasattr(sys, 'getandroidapilevel')

if IS_ANDROID:
    IN_STREAM_ARG = False
else:
    IN_STREAM_ARG = None

sudopass = Responder(
     pattern=r'\[sudo\] password:',
     response=str(getenv('PASSWORD'))+'\n'
     )

load_dotenv()

if not os.path.exists("src/docker/.env"):
    shutil.copy("src/docker/template.env", "src/docker/.env")

@task
def install_latex(c):
    """
    Install the package
    """
    c.sudo("apt-get -y update", watchers=[sudopass])
    c.sudo("apt-get -y upgrade", watchers=[sudopass])
    c.sudo("apt-get -y install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk", watchers=[sudopass])
    c.run("pip install --upgrade -e .", in_stream = IN_STREAM_ARG)

@task
def install_reondj(c):
    """ Install the REONdj app in the docker container
    """
    c.run('docker exec django4rgvflood sh -c "mkdir -p -m 0600 ~/.ssh"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "ssh-keyscan -H github.com bitbucket.org >> ~/.ssh/known_hosts"', in_stream = IN_STREAM_ARG)
    c.run('docker cp ~/.ssh/id_rsa django4rgvflood:/root/.ssh/', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "pip install git+ssh://git@github.com/RATESResearch/REONapp"', in_stream = IN_STREAM_ARG)

@task
def add_reondj(c):
    """ Add the REONdj appd to GeoNode
    """
    c.run('docker cp base.html django4rgvflood:/usr/src/geonode/geonode/templates/', in_stream = IN_STREAM_ARG)
    c.run('docker cp urls.py django4rgvflood:/usr/src/geonode/geonode/', in_stream = IN_STREAM_ARG)
    c.run('docker cp settings.py django4rgvflood:/usr/src/geonode/geonode/', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py makemigrations --noinput"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py migrate --noinput"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py collectstatic --noinput"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "touch /usr/src/geonode/geonode/wsgi.py"', in_stream = IN_STREAM_ARG)

@task
def provision_reondj(c):
    """ Provision REONdj
    """
    c.run('docker cp theme.json django4rgvflood:/usr/src/geonode', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "mkdir -p /mnt/volumes/statics/uploaded/img/2021/12/"', in_stream = IN_STREAM_ARG)
    c.run('docker cp background.jpg django4rgvflood:/mnt/volumes/statics/uploaded/img/2021/12/', in_stream = IN_STREAM_ARG)
    c.run('docker cp logo.png django4rgvflood:/mnt/volumes/statics/uploaded/img/2021/12/', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py loaddata /usr/src/geonode/theme.json"', in_stream = IN_STREAM_ARG)

@task
def clean(c):
    """
    Clean the docs _build directory
    """
    c.run("make clean", in_stream = IN_STREAM_ARG)

@task
def html(c):
    """
    Make html documents
    """
    c.run("make html --debug", in_stream = IN_STREAM_ARG)

@task
def slides(c):
    """
    Make slides
    """
    c.run("make slides --debug", in_stream = IN_STREAM_ARG)

@task
def single(c):
    """
    Make slides
    """
    c.run("make singlefile-slides --debug", in_stream = IN_STREAM_ARG)

@task
def latexpdf(c):
    """
    Make pdf
    """
    c.run("make latexpdf --debug", in_stream = IN_STREAM_ARG)

@task
def pdf(c):
    """
    Make pdf
    """
    c.run("make pdf --debug", in_stream = IN_STREAM_ARG)

@task
def build_no_cache(c):
    """
    Run docker-compose build --no-cache
    """
    html(c)
    c.run("docker; docker-compose build --no-cache", in_stream = IN_STREAM_ARG)

@task
def up(c):
    """
    Run docker-compose
    """
    html(c)
    c.run("docker; docker-compose up -d", in_stream = IN_STREAM_ARG)

@task
def down(c):
    """
    Bring down docker images
    """
    c.run("docker-compose down", in_stream = IN_STREAM_ARG)

@task
def delete(c):
    """
    Bring down docker images and delete the volume
    """
    c.run("docker-compose down -v --rmi local", in_stream = IN_STREAM_ARG)

@task
def docs_for_docker(c):
    """
    Build docs for docker
    """
    #c.run("cd src/docker; docker-compose down -v --rmi local", in_stream = IN_STREAM_ARG)
    clean(c)
    html(c)
    single(c)
    #latexpdf(c)
    #up(c)
    #pdf(c)

@task
def all(c):
    """
    Do it all
    """
    clean(c)
    #pdf(c)
    #html(c)
    single(c)



if __name__ == "__main__":

    #system("inv install_reondj")
    #system("inv html")
    #system("inv slides")
    #exit()

    ans=True
    while ans:
        system("inv --list")
        ans=input("What would you like to do? ")
        system("inv "+ans)
