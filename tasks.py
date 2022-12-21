from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def coverage_report(ctx):
    #ctx.run("rm -r test_data", pty=True)
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)
    ctx.run("rm -r test_data", pty=True)

@task
def test(ctx):
    #ctx.run("rm -r test_data", pty=True)
    ctx.run("pytest src", pty=True)
    ctx.run("rm -r test_data", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src --max-line-length 100")