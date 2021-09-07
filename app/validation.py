import sqlalchemy.orm as orm
from fastapi import HTTPException


from app.services import (
    continent as continent_service,
    city as city_service,
    country as country_service,
)
from app.schemas import country as country_schema, city as city_schema


class validate:
    def __init__(self) -> None:
        pass

    @classmethod
    def validate_country(cls, db: orm.Session, country: country_schema):
        """
        This function checks if the area and population of the newly created country satisfies the conditions
        """
        print("in validation 1", getattr(country, "continent_id"), country)

        parentcontinent = continent_service.get_continent_by_id(
            db, getattr(country, "continent_id")
        )
        print("in validation 2")

        country_list = country_service.get_countries_by_continentid(
            db, getattr(country, "continent_id")
        )
        print("in validation 3")
        total_area = 0
        total_population = 0
        for temp_country in country_list:
            total_area += temp_country.area
            total_population += temp_country.population

        if (
            total_population + country.population > parentcontinent.population
            and total_area + country.area > parentcontinent.area
        ):
            raise HTTPException(
                "Population and the Area both exceed continent's population and area"
            )
        elif total_population + country.population > parentcontinent.population:
            raise HTTPException(
                "Population exceeds the total population of continent, update population of continent or reduce the population of the country"
            )
        elif total_area + country.area > parentcontinent.area:
            raise HTTPException(
                "Area exceeds the total area of continent update area of continent or reduce the are of the country"
            )
        else:
            return True

    @classmethod
    def validate_city(cls, db: orm.Session, city: city_schema.City):
        """
        This function checks if the area and population of the newly created city satisfies the conditions
        """
        parentcountry = country_service.get_country_by_id(
            db, getattr(city, "country_id")
        )
        city_list = city_service.get_cities_by_countryid(
            db, getattr(city, "country_id")
        )
        total_area = 0
        total_population = 0
        for temp_city in city_list:

            total_area += temp_city.area
            total_population += temp_city.population

        if (
            total_population + city.population > parentcountry.population
            and total_area + city.area > parentcountry.area
        ):
            raise HTTPException(
                "Population and the Area both exceed continent's population and area"
            )
        elif total_population + city.population > parentcountry.population:
            raise HTTPException(
                "Population exceeds the total population of continent, update population of continent or reduce the population of the country"
            )
        elif total_area + city.area > parentcountry.area:
            raise HTTPException(
                "Area exceeds the total area of continent update area of continent or reduce the are of the country"
            )
        else:
            return True
