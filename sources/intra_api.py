#!/bin/python3

import requests
from requests import Response
import sources.constants as constants
import os


class IntraApi:
    def __init__(self):
        self.session = requests.session()
        response: Response = self.session.get(os.getenv("autologin"))
        if response.status_code != 200:
            raise ValueError(response.text)

    @staticmethod
    def concat_all_cities() -> str:
        return "|".join([constants.Cities[code] for code in constants.Cities])

    @staticmethod
    def concat_cities(cities: list[str]) -> str:
        return "|".join([constants.Cities[code] for code in cities])

    def get_user_infos(self, login: str) -> dict:
        url: str = f'https://intra.epitech.eu/user/{login}?format=json'
        response: Response = self.session.get(url)
        return response.json()

    def get_trombi(self, cities_params: str, year: str, promo: str) -> dict:
        cities: str = IntraApi.concat_all_cities() if cities_params == "All" else IntraApi.concat_cities(
            cities_params.split(","))
        url: str = f'https://intra.epitech.eu/user/filter/user?format=json&location={cities}&year={year}&active=true&promo={promo}&offset=0'
        response: Response = self.session.get(url)
        return response.json()


API: IntraApi = IntraApi()
