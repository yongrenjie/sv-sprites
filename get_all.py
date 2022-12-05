# this should really be a bash script, but heck

import os
from pathlib import Path

this_dir = Path(__file__).parent.absolute()
os.chdir(this_dir)

# os.system("mkdir original")

# # Regular mons
# for i in range(906, 1011):
#     print(i)
#     os.system(f"curl https://www.serebii.net/pokedex-sv/icon/{i}.png -o original/{i}.png")

# # Tatsugiri and Squawkabilly
# for i in ["960-b", "960-y", "960-w",  # squawkabilly
#           "952-d", "952-s",  # tatsugiri
#           "194-p",   # wooper
#           "128-p", "128-b", "128-a",   # tauros
#           ]:
#     print(i)
#     os.system(f"curl https://www.serebii.net/pokedex-sv/icon/{i}.png -o original/{i}.png")


# Rename
with open("names.txt") as file:
    for line in file:
        num, name = line.split()
        os.system(f"cp original/{num}.png {name}.png")

# Trim
os.system("sh trim_dir.sh .")
