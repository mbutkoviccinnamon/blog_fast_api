from pydantic import BaseModel
import datetime


class OwidCovidData(BaseModel):
    iso_code: str = None
    continent: str = None
    location: str = None
    date: datetime.date = None
    total_cases:  float = None
    new_cases:  float = None
    new_cases_smoothed:  float = None
    total_deaths:  float = None
    new_deaths:  float = None
    new_deaths_smoothed:  float = None
    total_cases_per_million:  float = None
    new_cases_per_million:  float = None
    new_cases_smoothed_per_million:  float = None
    total_deaths_per_million:  float = None
    new_deaths_per_million:  float = None
    icu_patients:  float = None
    new_deaths_smoothed_per_million:  float = None
    icu_patients_per_million:  float = None
    hosp_patients:  float = None
    hosp_patients_per_million:  float = None
    weekly_icu_admissions:  float = None
    weekly_icu_admissions_per_million:  float = None
    weekly_hosp_admissions:  float = None
    weekly_hosp_admissions_per_million:  float = None
    total_tests:  float = None
    new_tests:  float = None
    total_tests_per_thousand:  float = None
    new_tests_per_thousand:  float = None
    new_tests_smoothed:  float = None
    new_tests_smoothed_per_thousand:  float = None
    tests_per_case:  float = None
    positive_rate:  float = None
    tests_units:  float = None
    stringency_index:  float = None
    population:  float = None
    population_density:  float = None
    median_age:  float = None
    aged_65_older:  float = None
    aged_70_older:  float = None
    gdp_per_capita:  float = None
    extreme_poverty:  float = None
    cardiovasc_death_rate:  float = None
    diabetes_prevalence:  float = None
    female_smokers:  float = None
    male_smokers:  float = None
    handwashing_facilities:  float = None
    hospital_beds_per_thousand:  float = None
    life_expectancy:  float = None
    human_development_index:  float = None

    class Config:
        orm_mode = True