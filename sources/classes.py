#!/bin/python3
import os

from sources.intra_api import API


class User:
    def __init__(self, json_content: dict):
        user_infos: dict = API.get_user_infos(json_content["login"])
        self.login: str = user_infos["login"]
        self.firstname: str = user_infos["firstname"]
        self.lastname: str = user_infos["lastname"]
        self.city: str = user_infos["location"]
        self.gpa: int = user_infos["gpa"][0]["gpa"]
        self.year: str = os.getenv("year")

    def to_json(self) -> dict:
        return {
            "login": self.login,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "city": self.city,
            "gpa": self.gpa
        }

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __lt__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __ne__(self, other):
        return not self.__eq__(other)
