import os

import orjson

def check_license(name: str) -> bool: 
    result = os.path.isfile(os.path.join(os.path.dirname(__file__), r"spdx\\json\\details\\" + name + ".json"))
    if name in ["Proprietary", "none"]:
        result = True
    return result