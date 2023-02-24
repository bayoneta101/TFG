import sys
from wrlparser import parse


with open(file) as f:
    l = "".join(f.readlines())
    f.close()

scene = parse(l)