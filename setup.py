from setuptools import setup, find_packages

setup(
    name='digitalocean_spaces',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'python-dotenv',
    ],
    url='https://github.com/lupin-oomura/digitalocean_spaces.git',
    author='Shin Oomura',
    author_email='shin.oomura@gmail.com',
    description='functions for digitalocean_spaces',
)
