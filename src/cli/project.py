import os
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from __internal.license import check_license

def init():
    basename = os.path.basename(os.getcwd())
    name = input("package name ({}): ".format(basename))
    version = input("version (0.1.0): ")
    version = input("description: ")
    version = input("repository: ")
    author = input("author: ")
    while True:
        license = input("license: ")
        if license == "":
            license = "none"
        if check_license(license):
            break
        print('Invalid license. The license can only be set to a license listed in the SPDX Open Source License Registry or "Proprietary" or "none".')
    print('License is set to "{}".'.format(license))
    if name == "":
        name = basename
    if version == "":
        version = "0.1.0"