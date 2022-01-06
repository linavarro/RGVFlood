from invoke import task
from os import system
import sys

IS_ANDROID: bool = hasattr(sys, 'getandroidapilevel')

if IS_ANDROID:
    IN_STREAM_ARG = False
else:
	IN_STREAM_ARG = None

@task
def install(c):
    """
    Install the package
    """
    c.run("pip install --upgrade -e .", in_stream = IN_STREAM_ARG)

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
def up(c):
    """
    Run docker-compose
    """
    html(c)
    c.run("cd src/docker; docker-compose up -d", in_stream = IN_STREAM_ARG)
    
@task
def down(c):
    """
    Bring down docker images
    """
    c.run("cd src/docker; docker-compose down", in_stream = IN_STREAM_ARG)
    
@task
def dall(c):
    """
    Do it all with docker
    """
    c.run("cd src/docker; docker-compose down -v --rmi all", in_stream = IN_STREAM_ARG)
    clean(c)
    html(c)
    slides(c)
    up(c)
    
@task
def all(c):
    """
    Do it all
    """
    #c.run("cd src/docker; docker-compose down -v --rmi all")
    clean(c)
    html(c)
    slides(c)
    single(c)
    #up(c)



if __name__ == "__main__":

    system("inv all")
    #system("inv html")
    #system("inv slides")
    exit()

    ans=True
    while ans:
    	system("inv --list")
    	ans=input("What would you like to do? ")
    	system("inv "+ans)
