from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/index.py")

@task
def test(ctx):
	print("Run tests here")

@task
def coverage_report(ctx):
	print("Make coverage report")
