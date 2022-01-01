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

if __name__ == "__main__":

    #system("inv make-html")
    #exit()

    ans=True
    while ans:
    	system("inv --list")
    	ans=input("What would you like to do? ")
    	system("inv "+ans)
