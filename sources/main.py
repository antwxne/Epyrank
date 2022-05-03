#!/bin/python3
import os

from sources.intra_api import API
from sources.classes import User
from sources.utils import create_dir, write_json, get_json_from_file

# plop = {
#     "year": "2022",
#     "cities": [
#         {
#             "city": "Paris",
#             "users": [
#                 {
#                     "login": "toto"
#                 }
#             ]
#         }
#     ]
# }


def sort_by_city(users: list[User]) -> dict:
    dest: dict = {}
    for user in users:
        if user.city not in dest:
            dest[user.city] = [user]
        else:
            dest[user.city].append(user)
    return dest


def save_infos(cities_infos: dict):
    for city in cities_infos:
        path = f'./data/{os.getenv("year")}/{city}'
        create_dir(path)
        json_data: list[dict] = []
        for user in cities_infos[city]:
            json_data.append(user.to_json())
        write_json(json_data, f'{path}/data.json')


def main():
    # trombi: dict = API.get_trombi(os.getenv("cities"), os.getenv("year"), os.getenv("promo"))
    trombi: dict = get_json_from_file("./data/trombi.json")
    users: dict = get_json_from_file("./data/2021/FR/MLH/data.json")
    # write_json(trombi, "./data/trombi.json")
    # users: list[User] = [User(elem) for elem in trombi["items"]]
    # sorted_by_city: dict = sort_by_city(users)
    # save_infos(sorted_by_city)


if __name__ == "__main__":
    main()
