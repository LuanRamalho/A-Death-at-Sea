#!/usr/bin/python3
import sys
import os

if sys.version_info < (3, 5):
    sys.exit("Python 3.5 or later is required.")



from pathlib import Path

Path(__file__).parent.cwd()
os.execvp(sys.executable, [sys.executable, '-m', 'pgzero', 'murder.py'])
