from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="aicmt",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,  # Include i file extra definiti in MANIFEST.in
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "aicmt=aicmt.cli:cli",
        ],
    },
    url="https://github.com/capimichi/aicmt",
    author="Michele Capicchioni",
    author_email="capimichi@gmail.com",
    description="AICMT - Automatic commit via artificial intelligence",
)