# Python File System Utils

> Utility functions that replace Python `os` module implementations

## About

`pyfs` is for my personal use in performing file system operations via
Python.

This project came about because a lot of my current work involves dealing with
files stored on my computer, but Python's default file path handling is
disappointing. By *default* it uses the path of the current executing as the
suffix to all other paths, regardless of whether they are absolute or relative.
This has resulted in many head-desk moments which frustrated me.

Thus, rather than writing duplicate code across all of my projects to handle
filepaths, I am compiling my functions here.

`pyfs` is written (at the time of writing) in Python 3.10 native code. There are
zero external dependencies (aside from `poetry` to build the project).

## How to Install

This utility library should be cross compatible across platforms as it only relies on standard Python.
However, this has not been tested. So far only Linux x86-64 has been tested and validated to work with this utility.

### Dependencies

- Python 3.10
- `poetry`

### Installation steps

1. Run `make` in the root directory of this repository

## How to Run

1. Import `pyfs` into your project
