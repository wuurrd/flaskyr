from setuptools import setup, find_packages

version = 0.1

setup(
    name='flask-yr',
    version=version,
    description='YR',
    long_description='',
    # Get strings for classifiers from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers:
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(
        exclude=['ez_setup', 'examples', 'test', 'contrib']),
    package_data={},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    setup_requires=['xmltodict', 'requests', 'Flask'],
    dependency_links=[],
    entry_points={},
    scripts=[])
