from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="{{cookiecutter.name}}",
    packages=find_packages(),
    entry_points={"console_scripts": []},
    include_package_data=True,
    package_data={},
    install_requires=requirements,
    setup_requires=["setuptools_scm", "pytest-runner"],
    use_scm_version=True,
    tests_require=["pytest"],
    test_suite="tests",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    maintainer="{{cookiecutter.author}}",
    maintainer_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{cookiecutter.url}}",
)
