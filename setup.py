from setuptools import setup, find_packages
import os

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

setup(
    name='soc-faker',
    version='2.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to fake SOC (Security Operations Center) data',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['faker', 'soc', 'security', 'swimlane'],
    url='https://github.com/swimlane/soc-faker',
    author='Swimlane',
    author_email='info@swimlane.com',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    package_data={
        'socfaker':  ['data/*.txt', 'data/*.csv', 'data/*.json', 'data/filenames/*.txt', 'data/sysmon/*.txt', 'data/windows-event/*.md']
    },
    entry_points={
          'console_scripts': [
              'soc-faker = socfaker.__main__:main'
          ]
    }
)