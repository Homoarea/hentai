import os
from codecs import open
from setuptools import setup

requires=[
    "click",
    "curl_cffi",
    "beautifulsoup4",
    "lxml",
    "pillow"
]

about={}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here,'src','ehentai','__version__.py'),'r','utf-8') as f:
    exec(f.read(),about)
print(about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    license=about["__license__"],

    packages=["ehentai"],
    package_dir={"":"src"},
    package_data={"":["LICENSE","NOTICE"]},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=requires,
    entry_points="""
        [console_scripts]
        eh=ehentai.eh:cli
    """,
    project_urls={
        "Source":"https://github.com/Homoarea/hentai"
    }
)