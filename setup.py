import setuptools

setuptools.setup(
    name='GeoOp',
    version='0.0.2',
    author='Sherin Thomas',
    author_email="tsherin140@gmail.com",
    description='Package with all geometric operations',
    long_description='This is a python library that includes operations on all 1D, 2D and 3D Geometric shapes',
    license='MIT',
    install_requires=[''],
    packages=setuptools.find_packages(where="GeoOp"),
    package_dir={"": "GeoOp"},
)