from os import listdir
from os.path import abspath, expanduser, isdir, isfile
from pathlib import Path
from typing import List


def resolvePath(path: Path) -> Path:
    """
    resolvePath

    Convert path from a relative path of the Python program execution to an absolute path

    :param path: Path to resolve to an absolute path
    :type path: Path
    :return: An absolute path
    :rtype: Path
    """
    return Path(abspath(path=expanduser(path=path)))


def isFile(path: Path) -> bool:
    """
    isFile

    An extension of the os.path.isfile() function that uses the absolute value of a path rather than the relative path

    :param path: Path to check if it is a file
    :type path: Path
    :return: True if the absolute path is a file; else return False
    :rtype: bool
    """
    return isfile(path=resolvePath(path=path))


def isDirectory(path: Path) -> bool:
    """
    isDirectory

    An extension of the os.path.isdir() function that uses the absolute value of a path rather than the relative path

    :param path: Path to check if it is a directory
    :type path: Path
    :return: True if the absolute path is a directory; else return False
    :rtype: bool
    """
    return isdir(s=resolvePath(path=path))


def listDirectory(path: Path) -> List[Path]:
    """
    listDirectory

    An extension of the os.listdif() function that returns the absolute value of a path rather than the relative path of files within a directory

    :param path: Path to list files from
    :type path: Path
    :return: List[Path] of files in the directory; is empty if the directory does not exist.
    :rtype: List[Path]
    """
    absolutePath: Path = resolvePath(path=path)
    if isDirectory(path=absolutePath):
        return [
            resolvePath(path=Path(absolutePath, file))
            for file in listdir(path=absolutePath)
        ]
    else:
        return []
