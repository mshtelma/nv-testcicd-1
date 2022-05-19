from setuptools import find_packages, setup
from nv_testcicd_1 import __version__

setup(
    name="nv_testcicd_1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
