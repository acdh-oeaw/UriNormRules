import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acdh_arche-assets",
    version="0.1.0",
    author="Mateusz Żółtak",
    author_email="mzoltak@oeaw.ac.at",
    description="A set of static assets used (mainly) for ARCHE data preprocessing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acdh-oeaw/arche-assets",
    packages=setuptools.find_packages(),
    package_data={'AcdhArcheAssets': ['uriNormRules.json', 'formats.json']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
