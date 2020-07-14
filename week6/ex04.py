#!/usr/bin/env python

from pathlib import Path
from os import chdir

path = Path('..')

print(f'Current working directory: {path.cwd()}')

chdir(path)

print(f'Current working directory: {path.cwd()}')

chdir('..')

print(path.cwd())

path = Path.home()

docs = path / 'Documents'
pictures = path / 'Pictures'

print(docs)
print(pictures)
