#!/bin/bash

VENV_PATH="$HOME/.venv"

if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH"
fi

# Активируем окружение
source "$VENV_PATH/bin/activate"
pip install -r requirements.txt
python3 data_creation.py
python3 data_preprocessing.py
python3 model_preparation.py
python3 model_testing.py