from invoke import task
from os import system

@task
def install(c):
    """
    Install the package
    """
    c.run("pip install --upgrade -e .")

@task
def clean(c):
    """
    Clean the docs _build directory
    """
    c.run("make clean")

@task
def html(c):
    """
    Make html documents
    """
    c.run("make html --debug")

@task
def slides(c):
    """
    Make slides 
    """
    c.run("make slides --debug")
    
@task
def up(c):
    """
    Run docker-compose
    """
    html(c)
    c.run("cd src/docker; docker-compose up -d")
    
@task
def down(c):
    """
    Bring down docker images
    """
    c.run("cd src/docker; docker-compose down")
    
@task
def dall(c):
    """
    Do it all with docker
    """
    c.run("cd src/docker; docker-compose down -v --rmi all")
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
    #up(c)



if __name__ == "__main__":

    #system("inv make-html")
    #exit()

    ans=True
    while ans:
    	system("inv --list")
    	ans=input("What would you like to do? ")
    	system("inv "+ans)
