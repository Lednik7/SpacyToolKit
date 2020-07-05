from setuptools import setup

setup(
   name='SpacyToolKit',
   version='1.0.0',
   packages=['Tools.py'],
   author='Maxim Gerasimov',
   install_requires=['spacy>=2.0', 'pymorphy2>=0.8', "googletrans=>3.0.0"]
)
