"""File containing invoke tasks used for development.

Not to be confused with the project1337.tasks which holds the Celery tasks.
"""

import subprocess

from invoke import task


@task
def ruff(c):
    """Run ruff linter."""
    c.run("ruff check", pty=True)


@task
def ruff_format(c):
    """Format using ruff linter."""
    c.run("ruff format", pty=True)


@task
def mypy(c):
    """Run mypy type checks."""
    c.run("mypy .", pty=True)


@task
def black(c):
    """Run black to format code."""
    c.run("black .", pty=True)


@task
def radon_cc(c):
    """Run Radon to compute cyclomatic complexity."""
    c.run("radon cc . -a", pty=True)


@task
def radon_mi(c):
    """Run Radon to compute maintainability index."""
    c.run("radon mi .", pty=True)


@task(pre=[black, ruff_format, mypy, ruff, radon_cc, radon_mi])
def build_local(c):
    """Run all tasks: mypy, black, and radon."""
    print("All checks completed.")


@task
def migrate(c):
    """Run makemigrations and migrate."""
    c.run("python manage.py makemigrations", pty=True)
    c.run("python manage.py migrate", pty=True)


def determine_docker_command():
    """Try 'docker compose' first; fallback to 'docker-compose' if needed."""
    try:
        # Try 'docker compose' to see if it's available
        subprocess.run(
            ["docker", "compose", "--version"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return "docker compose"
    except subprocess.CalledProcessError:
        pass
    except FileNotFoundError:
        pass

    # Fallback to 'docker-compose'
    return "docker-compose"


@task
def buildup(c):
    """Build and run docker image."""
    docker_command = determine_docker_command()
    c.run(f"{docker_command} up --build", pty=True)


@task
def shell(c):
    """Run python shell for docker server instance."""
    docker_command = determine_docker_command()
    c.run(f"{docker_command} exec web poetry run python manage.py shell", pty=True)
