import setuptools

setuptools.setup(
    name='GeoPack',
    version='0.0.1',
    description='Package with all geometric operations'
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
     packages=setuptools.find_packages(),
)