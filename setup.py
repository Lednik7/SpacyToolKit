from setuptools import setup, find_packages

with open("SpacyToolKit/README.md", 'r') as f:
    long_description = f.read()

setup(
   name='SpacyToolKit',
   version='2.7',
   description='It is a small library dedicated to the fast Spacy model stack, preparing data for training and training models.',
   license="MIT",
   long_description=long_description,
   author='Maxim Gerasimov',
   url="https://github.com/Lednik7/SpacyToolKit",
   packages=find_packages(),
   install_requires=['spacy>=2.0', 'googletrans>=3.1.0a0', "pymorphy2>=0.8", "sklearn>=0.00.0", "numpy>=1.19.4"],
)