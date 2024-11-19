@echo off
for /l %%i in (1, 1, 5) do (
    echo. > TP9_%%i\app.py
    echo from flask import Flask > TP9_%%i\app.py
    cd > TP9_%%i\Models\__init__.py
    mkdir TP9_%%i\Models
    mkdir TP9_%%i\Models\Entities
    mkdir TP9_%%i\Models\Repositories
    mkdir TP9_%%i\Data
)