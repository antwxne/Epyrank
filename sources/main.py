#!/bin/python3
import os

from sources.intra_api import API
from sources.excel import EXCEL
from sources.classes import User
from tqdm import tqdm


def sort_by_city(users: list[User]) -> dict:
    dest: dict = {}
    for user in tqdm(users, desc="Sorting users by city", unit="User"):
        if user.city not in dest:
            dest[user.city] = [user]
        else:
            dest[user.city].append(user)
    return dest


def get_user_list(trombi: list) -> list[User]:
    users: list[User] = []
    for elem in tqdm(trombi, desc="Getting users informations", unit="User"):
        users.append(User(elem))
    users.sort(reverse=True)
    return users


def main():
    print("Getting infos from trombi...")
    trombi: list = API.get_trombi(os.getenv("cities"), os.getenv("year"), os.getenv("promo"))
    users: list[User] = get_user_list(trombi)
    print("Adding all user to excel...")
    EXCEL.add_all_users(users)
    sorted_by_city: dict = sort_by_city(users)
    print("Adding ranking by city to excel...")
    EXCEL.add_cities(sorted_by_city)
    print("Adding city ranking to excel...")
    EXCEL.cities_rank(sorted_by_city)
    EXCEL.save()


if __name__ == "__main__":
    main()
