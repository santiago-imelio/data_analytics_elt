from setuptools import find_packages, setup

setup(
    name="analytics_pipeline",
    packages=find_packages(exclude=["analytics_pipeline_tests"]),
    install_requires=[
        "dagster==1.8.1",
        "dagster-airbyte",
        "dagster-dbt",
        "pandas"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
