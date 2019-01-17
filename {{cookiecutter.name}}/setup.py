from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.name}}",
    packages=find_packages(),
    entry_points={"console_scripts": []},
    include_package_data=True,
    package_data={},
    install_requires=[],
    setup_requires=["setuptools_scm", "pytest-runner"],
    use_scm_version=True,
    tests_require=["pytest"],
    test_suite="tests",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    maintainer="{{cookiecutter.author}}",
    maintainer_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    license="{{cookiecutter.license}}",
    url="{{cookiecutter.url}}",
)
