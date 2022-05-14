import os
import shutil
import subprocess

folder = os.getcwd()

if not "{{cookiecutter.writing_docs}}" == "yes":
    shutil.rmtree(os.path.join(folder, "docs"))
    os.remove(os.path.join(folder, "mkdocs.yml"))

message = "initial commit from gh:zehengl/cookiecutter-py-package"

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", message])
