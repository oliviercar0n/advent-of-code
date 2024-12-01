import numpy as np
import re

with open("day-20.txt", "r") as f:
    input_data = f.read().strip()

C = {}
for line in input_data.split('\n'):
    module, dest = line.split(' -> ')
    if module.startswith(('%','&')):
        t = module[0]
        n = module[1:]
    else:
        t = None
        n = module

    C[n] = {"type": t, "dest": dest.strip().split(', ')}

for v in C.values():
    for d in v['dest']:
        if d not in C.keys():
            print(d)