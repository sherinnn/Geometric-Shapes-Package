import setuptools

setuptools.setup(
    name='GeoOpPackage',
    version='0.0.1',
    author='Sherin Thomas',
    author_email="tsherin140@gmail.com",
    description='Geometric operations package',
    long_description='This is a python library that includes operations on all 1D, 2D and 3D Geometric shapes',
    license='MIT',
    install_requires=[''],
    packages=setuptools.find_packages(where="GeoOpPackage"),
    package_dir={"": "GeoOpPackage"},
)