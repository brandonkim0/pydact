import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pydact',
    version='0.1.0',
    description='Tools for removing Protected Health Information',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kind-lab/pydact',
    author='Alistair Johnson, Brandon Kim',
    author_email='alistair.johnson@sickkids.ca, brandon.kim@sickkids.ca',
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)
