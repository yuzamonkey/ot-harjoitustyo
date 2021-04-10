from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/index.py")

@task
def test(ctx):
  print("Run tests here")
  ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
  print("Make coverage report")
  ctx.run("coverage html")

