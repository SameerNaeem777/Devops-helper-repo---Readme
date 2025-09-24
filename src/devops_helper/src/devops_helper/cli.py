"""DevOps Helper CLI


Simple click-based CLI with build, docker-build, and clean commands.
"""
import click
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


@click.group()
def cli():
"""DevOps Helper CLI"""


@cli.command()
def build():
"""Run project build steps (tests)"""
click.echo('Running tests...')
res = subprocess.run([sys.executable, '-m', 'pytest', '-q'])
raise SystemExit(res.returncode)


@cli.command('docker-build')
@click.option('--tag', default='devops-helper:latest', help='Docker image tag')
def docker_build(tag):
"""Build docker image"""
click.echo(f'Building Docker image {tag}...')
res = subprocess.run(['docker', 'build', '-t', tag, '.'])
raise SystemExit(res.returncode)


@cli.command()
def clean():
"""Clean artifacts"""
click.echo('Cleaning build artifacts...')
paths = ['dist', 'build', '__pycache__', '.pytest_cache']
for p in paths:
subprocess.run(['bash', '-c', f'rm -rf {p}'])
click.echo('Done.')


if __name__ == '__main__':
cli()
