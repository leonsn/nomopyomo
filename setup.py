from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setup(
    name='nomopyomo',
    version='0.0.1',
    author='Tom Brown (KIT)',
    author_email='brown@fias.uni-frankfurt.de',
    description='Perform PyPSA LOPF without using pyomo',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/PyPSA/nomopyomo',
    license='GPLv3',
    packages=find_packages(exclude=['doc', 'test']),
    include_package_data=True,
    install_requires=[
        'pypsa',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ])