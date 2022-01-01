from invoke import task
from os import system

@task
def install_package(c):
    """
    Install the package
    """
    c.run("pip install --upgrade -e .")

if __name__ == "__main__":

    #system("inv runserver")
    #exit()

    ans=True
    while ans:
    	system("inv --list")
    	ans=input("What would you like to do? ")
    	system("inv "+ans)
