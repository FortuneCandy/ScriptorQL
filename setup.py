import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="data_to_sql_insert",
    version="0.0.1",
    author="Arne Goossens",
    author_email="/",
    description=("Generates SQL insert values script for data"),
    license="GNU GENERAL PUBLIC LICENSE Version 3",
    keywords="Generate SQL insert values script",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FortuneCandy/data-to-sql-insert",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)
