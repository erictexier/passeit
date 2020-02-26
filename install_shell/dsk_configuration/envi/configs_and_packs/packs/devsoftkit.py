import os
base_release = "/Users/eric/mnt/dev/eric/packages/devsoftkit"
version = ""


add_path("PYTHONPATH",os.path.join(base_release, version, "python"))
add_path("PATH",os.path.join(base_release, version, "bin"))

