from setuptools import setup

setup(
    name='PostBin',
    version='1.0.6',
    packages=['postbin', "postbin.v2"],
    url='https://github.com/dragdev-studios/postbin',
    python_requires=">=3.8",
    license='MIT',
    author='EEKIM10',
    author_email='eek@clicksminuteper.net',
    description='A simple two-function program that POSTs to hastebin',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown'
)
#
