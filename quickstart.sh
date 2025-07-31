#!/bin/bash

set -e

echo "Stating Diag Test Setup."
ROOT=$(pwd)

SUPPORTED_PYTHON=("python3.10"  "python3.6")

for py in "${SUPPORTED_PYTHON[@]}"; do
    if command -v $py >/dev/null 2>&1; then
        SELECTED_PYTHON=$py
        break
    fi
done

if [ -z "$SELECTED_PYTHON" ]; then
    echo "Error: No compatible Python version found. Supported versions are: ${SUPPORTED_PYTHON[*]}"
    exit 1
fi
echo "Using Python version: $SELECTED_PYTHON"

py=$SELECTED_PYTHON
echo "python version: ${py}"

VENV="${ROOT}/.venv"

# Create virtual environment
echo "Setting up Python virtual environment."
python3 -m venv .venv
source .venv/bin/activate

# Create test data directory if not exists
mkdir -p results reports/allure-reports/ reports/pytest-reports

# Install requirements
PIP_CACHED=${ROOT}/.pip_download_cache
echo "Installing requirements"


if ! python -m pip install --upgrade "pip==22.0.4" -i https://pypi.org/simple; then
    echo "Official Source not OK, trying mirror which is default"
    python -m pip install --upgrade "pip==22.0.4"
fi

if ! pip install --no-cache-dir -r requirements.txt -i https://pypi.org/simple; then
    echo "Official Source not OK, trying mirror which is default"
    pip install --no-cache-dir -r requirements.txt
fi

pip install -e .

export PYTHONPATH=$PYTHONPATH:${ROOT}

echo "Test Setup Complete"
deactivate