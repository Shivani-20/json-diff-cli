from setuptools import setup

setup(
    name="jdif",
    version="2.0.5",
    description="To find json differences on CLI, please visit the following url",
    long_description="https://github.com/Shivani-20/json-diff-cli/blob/main/readme.md",
    author="shivani",
    license='MIT',
    entry_points={
        'console_scripts': [
            'jdif = jdif:start',
        ]
    },
    project_urls={
        "Source": "https://github.com/Shivani-20/json-diff-cli"
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Topic :: File Formats :: JSON",
        "Topic :: File Formats :: JSON :: JSON Schema",
        "Topic :: Software Development :: Debuggers"
    ],
    package_dir={"": "src"},
    packages=["jdif"],
    python_requires='>=3.8',
    install_requires=[
        'termcolor>=2.4.0',
        'deepdiff>=7.0.1',
        'charade>=1.0.3',
        'pyparsing>=3.1.2'
    ])
