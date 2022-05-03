#!/bin/python3
from json import load, dump
from os import path
from pathlib import Path


def create_dir(folder: str):
    """
    Create a directory if it doesn't exist

    Args:
      folder (str): str
    """
    Path(folder).mkdir(parents=True, exist_ok=True)


def write_json(json_data, filename):
    """ Write supposed json data into a file

    Args:
        json_data (Any): supposed json data
        filename (String): name of the file where to write the data
    """
    with open(filename, "w") as file:
        dump(json_data, file, indent=4)


def get_json_from_file(filename) -> dict:
    """ Parse a file containing a json

    Args:
        filename (String): name of the file to parse

    Raises:
        ValueError: file doesn't exist or is not a file

    Returns:
        Any: json parsed
    """
    if path.exists(filename) and path.isfile(filename):
        file = open(filename, "r")
        json_data = load(file)
        file.close()
        return json_data
    else:
        raise FileExistsError(f"Wrong filename: {filename} doesn't exist")
