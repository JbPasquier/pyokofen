import os
import setuptools


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="PyOkofen",
    version="1.0.0",
    author="Jean-Baptiste Pasquier",
    author_email="contact@jbpasquier.eu",
    description="JSON to python API for Okofen boilers",
    license="Apache 2.0",
    url="https://github.com/JbPasquier/pyokofen",
    packages=("pyokofen",),
    python_requires=">=3.8.0",
    install_requires=["requests"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
