from setuptools import setup
setup(
    name="jdif",
    version="1.0.4",
    description="To find json differences",
    author="shivani",
    entry_points={
        'console_scripts': [
            'jdif = jdif:start',
        ]
    },
    package_dir={"": "src"},
    packages=["jdif"],
    install_requires=[
        'termcolor>=2.4.0',
        'deepdiff>=7.0.1',
        'terminaltables>=3.1.10'
    ])
