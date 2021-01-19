from app.db import db, metadata, sqlalchemy
from sqlalchemy.types import Date
from sqlalchemy import and_

owidCovidData = sqlalchemy.Table(
    "owid_covid_data",
    metadata,
    sqlalchemy.Column("iso_code", sqlalchemy.String),
    sqlalchemy.Column("continent", sqlalchemy.String),
    sqlalchemy.Column("location", sqlalchemy.String),
    sqlalchemy.Column("date", Date),

    sqlalchemy.Column("total_cases", sqlalchemy.Numeric),
    sqlalchemy.Column("new_cases", sqlalchemy.Numeric),
    sqlalchemy.Column("new_cases_smoothed", sqlalchemy.Numeric),
    sqlalchemy.Column("total_deaths", sqlalchemy.Numeric),
    sqlalchemy.Column("new_deaths", sqlalchemy.Numeric),
    sqlalchemy.Column("new_deaths_smoothed", sqlalchemy.Numeric),
    sqlalchemy.Column("total_cases_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("new_cases_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("new_cases_smoothed_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("total_deaths_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("new_deaths_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("new_deaths_smoothed_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("icu_patients", sqlalchemy.Numeric),
    sqlalchemy.Column("icu_patients_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("hosp_patients", sqlalchemy.Numeric),
    sqlalchemy.Column("hosp_patients_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("weekly_icu_admissions", sqlalchemy.Numeric),
    sqlalchemy.Column("weekly_icu_admissions_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("weekly_hosp_admissions", sqlalchemy.Numeric),
    sqlalchemy.Column("weekly_hosp_admissions_per_million", sqlalchemy.Numeric),
    sqlalchemy.Column("total_tests", sqlalchemy.Numeric),
    sqlalchemy.Column("new_tests", sqlalchemy.Numeric),
    sqlalchemy.Column("total_tests_per_thousand", sqlalchemy.Numeric),
    sqlalchemy.Column("new_tests_per_thousand", sqlalchemy.Numeric),
    sqlalchemy.Column("new_tests_smoothed", sqlalchemy.Numeric),
    sqlalchemy.Column("new_tests_smoothed_per_thousand", sqlalchemy.Numeric),
    sqlalchemy.Column("tests_per_case", sqlalchemy.Numeric),
    sqlalchemy.Column("positive_rate", sqlalchemy.Numeric),
    sqlalchemy.Column("tests_units", sqlalchemy.Numeric),
    sqlalchemy.Column("stringency_index", sqlalchemy.Numeric),
    sqlalchemy.Column("population", sqlalchemy.Numeric),
    sqlalchemy.Column("population_density", sqlalchemy.Numeric),
    sqlalchemy.Column("median_age", sqlalchemy.Numeric),
    sqlalchemy.Column("aged_65_older", sqlalchemy.Numeric),
    sqlalchemy.Column("aged_70_older", sqlalchemy.Numeric),
    sqlalchemy.Column("gdp_per_capita", sqlalchemy.Numeric),
    sqlalchemy.Column("extreme_poverty", sqlalchemy.Numeric),
    sqlalchemy.Column("cardiovasc_death_rate", sqlalchemy.Numeric),
    sqlalchemy.Column("diabetes_prevalence", sqlalchemy.Numeric),
    sqlalchemy.Column("female_smokers", sqlalchemy.Numeric),
    sqlalchemy.Column("male_smokers", sqlalchemy.Numeric),
    sqlalchemy.Column("handwashing_facilities", sqlalchemy.Numeric),
    sqlalchemy.Column("hospital_beds_per_thousand", sqlalchemy.Numeric),
    sqlalchemy.Column("life_expectancy", sqlalchemy.Numeric),
    sqlalchemy.Column("human_development_index", sqlalchemy.Numeric),
)


class OwidCovidData:
    @classmethod
    async def get(cls, iso_code, continent, location, date):
        query = owidCovidData.select().where(and_(owidCovidData.c.iso_code == iso_code,
                                                  owidCovidData.c.continent == continent,
                                                  owidCovidData.c.location == location,
                                                  owidCovidData.c.date == date))
        data = await db.fetch_one(query)
        return data

    @classmethod
    async def create(cls, **data):
        query = owidCovidData.insert().values(**data)
        await db.execute(query)
        return {"status": "OK"}

    @classmethod
    async def update(cls, **data):
        query = owidCovidData.update().where(and_(owidCovidData.c.iso_code == data["iso_code"],
                                             owidCovidData.c.continent == data["continent"],
                                             owidCovidData.c.location == data["location"],
                                             owidCovidData.c.date == data["date"])).values(**data)

        await db.execute(query)

        return {"status": "OK"}



