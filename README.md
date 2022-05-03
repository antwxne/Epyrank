# Epyrank

## Description

Script to rank EPITECH students by promotion using GPA and export it to an .xlsx file.

## Requirements

- Docker
- Docker-compose
- Autologin link

## Configuration

Template:
```text
autologin=
cities=
year=
promo=
```


### Autologin

Place your autologin link in the `.env` file.

> exemple:
> ```text
> autologin=< your autologin link >
> ```


### Cities

Place one or more of the following cities in the `.env` file (values must be separated by `,`). 

```text
Tirana
Bruxelles
Cotonou
Bordeaux
La Réunion
Lille
Lyon
Marseille
Montpellier
Moulins
Mulhouse
Nancy
Nantes
Nice
Paris
Rennes
Strasbourg
Toulouse
Berlin
Barcelone
```

> exemple:
> ```text
> cities=Paris
> cities=Paris,Lille,Nice
> cities=All> exemple:
> ```

### Year

Place one of the following year in the `.env` file. 

> It corresponds to a scholar year

```text
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
```

> exemple:
> ```text
> year=2021
> ```

### Promotion

Place one of the following promotion in the `.env` file. 

```text
Tek1
Tek2
Tek3
Tek4
Tek5
```

> exemple:
> ```text
> promo=tek1
>```
