import os
from setuptools import setup

def read(*paths):
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#","-","git+", '"'))
    ]

setup(
    name = "dundie",
    version = "0.1.0" ,
    description = "Reward Point System for Dunder Mifflin",
    author = "Thiago Beppe" ,
    packages = ["dundie"],
    entry_points = {
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ],

    },
    install_requires = read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.dev.txt"),
        "dev":  read_requirements("requirements.test.txt")
    }
)
