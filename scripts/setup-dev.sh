set -e

py -3.8 -m pip install --user pre-commit

# ADD C:\Users\<user>\AppData\Roaming\Python\Python312\site-packages to PATH
# Change Python 312 to your python version

where pre-commit
pre-commit --version

pre-commit install
pre-commit install --hook-type commit-msg
pre-commit install --install-hooks
