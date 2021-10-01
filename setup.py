from setuptools import find_packages, setup

setup(
    name="sample-sphinx-integrations",
    version="0.0.1",
    description="Sample Project.",
    author="Vadym Hevlich",
    install_requires=[
    ],
    python_requires=">=3.7.0",
    extras_require={
        "sphinx": [
            "Jinja2~=3.0",
            "MarkupSafe~=2.0",
            "Pygments~=2.10",
            "Babel~=2.9",
            "docutils~=0.17",
            "imagesize~=1.2",
            "packaging~=21.0",
            "pyparsing~=2.4",
            "pytz~=2021.1",
            "snowballstemmer~=2.1",
            "Sphinx~=4.2",
            "sphinxcontrib-applehelp~=1.0",
            "sphinxcontrib-devhelp~=1.0",
            "sphinxcontrib-htmlhelp~=2.0",
            "sphinxcontrib-jsmath~=1.0",
            "sphinxcontrib-qthelp~=1.0",
            "sphinx-rtd-theme~=1.0",
            "sphinxcontrib-serializinghtml~=1.1",
        ]
    },
)
