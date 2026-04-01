set -e

pre-commit clean
pre-commit uninstall
py -3.8 -m pip freeze > r.txt && py -3.8 -m pip uninstall -r r.txt -y && rm -f r.txt
