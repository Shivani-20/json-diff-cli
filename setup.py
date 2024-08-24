from setuptools import setup

with open("README.md", "r") as f:
    desc=f.read()

setup(
    name="jdif",
    version="3.0.0",
    description="To find json differences on CLI",
    long_description=desc,
    long_description_content_type="text/markdown",
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
    python_requires='>=3.12',
    install_requires=[
        'termcolor>=2.4.0',
        'deepdiff>=7.0.1',
        'charade>=1.0.3',
        'pyparsing>=3.1.2'
    ])
