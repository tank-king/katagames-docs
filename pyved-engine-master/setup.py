import os
from pathlib import Path

lib_folder = os.path.dirname(os.path.realpath(__file__))

requirements_file = lib_folder + '/runtime-req.txt'
whats_required = []  # Here we'll get content of requirements.txt
if os.path.isfile(requirements_file):
    with open(requirements_file) as fp:
        whats_required = fp.read().splitlines()

# need sys so we can include pyved_engine
import sys

sys.path.append('src')
from pyved_engine.__version__ import ENGI_VERSION
from setuptools import setup

pck_list = [
    "pyved_engine",
    "pyved_engine.foundation",
    "pyved_engine.compo",
    "pyved_engine.core",
    "pyved_engine.looparts",  # to be sure we get looparts/rogue.py, looparts/tabletop.py, etc.
    "pyved_engine.looparts.ai",
    "pyved_engine.looparts.demolib",
    "pyved_engine.looparts.gui",
    "pyved_engine.looparts.isometric",
    "pyved_engine.looparts.polarbear",
    "pyved_engine.looparts.tmx",
    "pyved_engine.looparts.tmx.pytiled_parser",
    "pyved_engine.looparts.tmx.pytiled_parser.parsers",
    "pyved_engine.looparts.tmx.pytiled_parser.parsers.json",
    "pyved_engine.looparts.tmx.pytiled_parser.parsers.tmx",
]

this_directory = Path(__file__).parent
long_desc = (this_directory / "README.md").read_text()

setup(
    name='pyved-engine',
    version=str(ENGI_VERSION),

    description='Custom game engine built upon python/pygame',
    long_description=long_desc,
    long_description_content_type='text/markdown',

    keywords=['Python', 'Pygame', 'Game Engine'],
    author='moonb3ndr et al.',
    author_email='thomas.iw@kata.games',
    license='LGPL3',
    package_dir={'': 'src'},
    packages=pck_list,
    url="https://github.com/gaudiatech/pyved-engine",
    install_requires=whats_required,
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'pyv-cli = cmdline.__main__:main'
        ]
    }
)
