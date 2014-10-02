from setuptools import setup

setup(
    name='sibl',
    version='0.1.0',
    author='David Greisen',
    author_email='dgreisen@gmail.com',
    packages=['sibl'],
    package_dir={'sibl': 'sibl'},
    scripts=['sibl/sibl'],
    url='http://pypi.python.org/pypi/sibl/',
    license='LICENSE',
    description='Ansible skeleton generator.',
    long_description=open('README.md').read(),
    install_requires=[
        "click >= 0.7.0",
        "Jinja2>=2.7.0",
    	"PyYAML>=3",
    ],
    include_package_data=True,
    package_data={ 'sibl': [ 'templates/*.yml', 'sibl'] },
)
