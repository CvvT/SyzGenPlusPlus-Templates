import os
import re

dirpath = "pixel6"

def get_syscalls(filepath):
    syscalls = []
    with open(filepath, "r") as fp:
        for line in fp:
            m = re.search(r'^([\w$]+)\(', line)
            if m:
                call = m.group(0)[:-1]
                syscalls.append(call)
    return syscalls

syscalls = []
for file in os.listdir(dirpath):
    if file.endswith("_gen.txt"):
        syscalls.extend(get_syscalls(os.path.join(dirpath, file)))

if "close" not in syscalls:
    syscalls.append("close")

for each in syscalls:
    print("\"%s\"," % each)

