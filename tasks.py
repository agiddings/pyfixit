from invoke import run, task

@task
def test():
   run("nosetests pyfixit/test")

