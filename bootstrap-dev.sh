#!/usr/bin/env bash

pip install --no-index --find-links=/internal/wheels -r requirements-dev.txt
pre-commit install


# #!/usr/bin/env bash

# echo "Setting up development environment..."

# # ensure pre-commit exists
# python -m pip install --upgrade pip
# python -m pip install pre-commit

# # install hooks
# pre-commit install --install-hooks

# echo "Dev environment ready."