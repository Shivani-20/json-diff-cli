from setuptools import setup
setup(
    name="jdif",
    version="1.1.0",
    description="To find json differences",
    author="shivani",
    entry_points={
        'console_scripts': [
            'jdif = jdif:start',
        ]
    },
    project_urls={
        "Source": "https://github.com/Shivani-20/json-diff-cli"
    },
    classifiers=[
        "Programming Language :: Python :: 3.12"
    ],
    package_dir={"": "src"},
    packages=["jdif"],
    install_requires=[
        'termcolor>=2.4.0',
        'deepdiff>=7.0.1',
        'terminaltables>=3.1.10'
    ])
