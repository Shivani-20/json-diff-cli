## Motivation

To find difference between two long json files on the cli itself, instead of downloading files and copy pasting on some website to find the difference. Helpful when comparing production env data with the admin dashboard data during the debugging process.

![alt text](visuals/jdif_cli.png)

## Installation

``pip install jdif``

## Quickstart

```python

>>> jdif
usage: jdif [-h] jsonFilePath1 jsonFilePath2
jdif: error: the following arguments are required: jsonFilePath1, jsonFilePath2
Arguments absent: please specify file paths as shown in the example below:
jdif example_1.json example_2.json

>>> jdif /../ /.../
Unable to read file in '\..', please verify the path and filename alongwith the extension

>>> jdif a1.json b1.json 
Invalid json in 'b1.json'

>>> jdif a1.json b1.json
Empty json in 'b1.json'

>>> jdif a1.json b1.json
JSON is same in both the files

