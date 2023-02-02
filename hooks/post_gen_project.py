import os
import subprocess

folder = os.getcwd()

message = "initial commit from gh:zehengl/cookiecutter-py-package"

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", message])
