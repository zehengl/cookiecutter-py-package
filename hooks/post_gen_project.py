import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'initial commit from gh:zehengl/cookiecutter-py-package'])
