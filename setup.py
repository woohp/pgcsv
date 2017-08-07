from setuptools import setup, find_packages

setup(
    name="pgcsv",
    packages=find_packages(),
    version="0.0.1",
    description="Execute .sql files with postgresql and output the results in CSV.",
    author="Hui Peng Hu",
    author_email="woohp135@gmail.com",

    scripts=["scripts/pgcsv"],
    install_requires=['click >= 6.7', 'psycopg2 >= 2.7.3']
)
