## Motivation

To find difference between two long json files on the cli itself, instead of downloading files and copy pasting on some website to find the difference. Helpful when comparing production env data with the admin dashboard data during the debugging process.

## Installation

``pip install jdif``

## Quickstart

* if a key appears in first file but not in second file OR the key appears in second file but not in first file,
color of the key changes to red

* if a value of a specific key is different in both the files, 
color of that key-value pair changes to green:

Combination of above 2 example

[![Example](https://raw.githubusercontent.com/Shivani-20/json-diff-cli/main/visuals/jdif_cli.png)]

## Caveats

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
```
**order** of the keys might change within an object because we are first processing values then modified keys:

suppose if j1.json has:
```json
{
    "key1": true,
    "key3": "abcd"
}
```
j2.json:
```json
{
    "key4": false,
    "key3": ""
}
```
``` python
>>> jdif j1.json j2.json
```

[![Example](https://raw.githubusercontent.com/Shivani-20/json-diff-cli/main/visuals/order.png)]


## Features

* Takes care of unicode, windows1252 characters, so the strings could be in any language or represent a symbol
* Takes care of long descriptive values or keys
* Takes care of empty valued strings
* Instead of dumping into some other file, it displays the differences on the console itself 