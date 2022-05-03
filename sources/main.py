#!/bin/python3
import os

from sources.intra_api import API
from sources.excel import EXCEL
from sources.classes import User


def sort_by_city(users: list[User]) -> dict:
    dest: dict = {}
    for user in users:
        if user.city not in dest:
            dest[user.city] = [user]
        else:
            dest[user.city].append(user)
    return dest


def main():
    trombi: list = API.get_trombi(os.getenv("cities"), os.getenv("year"), os.getenv("promo"))
    users: list[User] = [User(elem) for elem in trombi]
    users.sort(reverse=True)
    EXCEL.add_all_users(users)
    sorted_by_city: dict = sort_by_city(users)
    EXCEL.add_cities(sorted_by_city)
    EXCEL.cities_rank(sorted_by_city)
    EXCEL.save()


if __name__ == "__main__":
    main()
