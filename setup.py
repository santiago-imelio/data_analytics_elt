from setuptools import find_packages, setup

setup(
    name="analytics_pipeline",
    packages=find_packages(exclude=["analytics_pipeline_tests"]),
    install_requires=[
        "dagster",
        "pandas",
        "pymongo",
        "psycopg2"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
