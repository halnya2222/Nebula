"""
import fire

def hello(name="World"):
    return "Hello %s!" % name


def add(int1, int2):
    return int1 + int2


def main():
    fire.Fire({"hello": hello, "add": add})
"""
from cli.project import init

init()