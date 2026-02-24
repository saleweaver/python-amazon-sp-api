from setuptools import setup, find_packages

from sp_api.__version__ import __version__

setup(
    name='python-amazon-sp-api',
    version=__version__,
    install_requires=[
        "httpx>=0.27.0",
        "cachetools>=4.2",
        "confuse>=1.4",
        "typing-extensions"
    ],
    extras_require={
        "aws-caching": ["aws-secretsmanager-caching", "boto3"],
        "aws": ["boto3"]
    },
    packages=find_packages(include=["sp_api*"]),
    scripts=['make_endpoint/make_endpoint'],
    url='https://github.com/saleweaver/python-amazon-sp-api',
    license='MIT',
    author='Michael Primke',
    author_email='primke.michael@gmail.com',
    description='Python wrapper for the Amazon Selling-Partner API'
)
