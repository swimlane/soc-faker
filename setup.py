from setuptools import setup, find_packages
import os

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

def parse_data_files():
    return_list = []
    path = 'data/sysmon'
    for (dirpath, dirnames, filenames) in os.walk(path):
        for item in filenames:
            return_list.append('{}/{}'.format(dirpath.split('/')[1],item))
    path = 'data/filenames'
    for (dirpath, dirnames, filenames) in os.walk(path):
        for item in filenames:
            return_list.append('{}/{}'.format(dirpath.split('/')[1],item))
    path = 'data/windows-event'
    for (dirpath, dirnames, filenames) in os.walk(path):
        for item in filenames:
            return_list.append('{}/{}'.format(dirpath.split('/')[1],item))
    return_list.append('nessus-plugin-samples.json')
    return_list.append('useragent.json')
    return_list.append('alert_names.txt')
    return_list.append('country.txt')
    return_list.append('words.txt')
    return return_list

setup(
    name='soc-faker',
    version='1.0.1',
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
        'socfaker':  ['data/*.txt', 'data/*.json', 'data/filenames/*.txt', 'data/sysmon/*.txt', 'data/windows-event/*.md']
    }
)