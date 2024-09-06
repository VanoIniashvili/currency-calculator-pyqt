from setuptools import setup

APP = ['currency_calculator.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5', 'requests'],
    'includes': ['requests']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
