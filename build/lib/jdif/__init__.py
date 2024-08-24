import argparse
from pathlib import Path, PurePath
import json
from deepdiff import DeepDiff
from termcolor import colored
from copy import deepcopy
import sys
from display import print_side_by_side

# to present json differences side by side
def formatOutput(json1,json2,file1,file2):
    print("\n\n")
    json_str1=json.dumps(json1,indent=2).encode().decode('unicode_escape')
    json_str2=json.dumps(json2,indent=2).encode().decode('unicode_escape')
    print_side_by_side(file1,file2)
    print("\n")
    print_side_by_side(json_str1,json_str2)


# to delete paths which are different
def del_by_path(d, keys):
  for k in keys[:-1]:
    d = d[k]
  return d.pop(keys[-1])


# to append deleted paths again but with colors on the text
def append_by_path(d, path, value, colorKey=False, colorValue=False):
    new_key = colored(path[-1],"red") if(colorKey) else colored(path[-1],"green")
    new_path = deepcopy(path)
    del new_path[-1]
    curr = d
    for key in new_path:
        curr=curr[key]
    curr[new_key] = colored(value,"green") if(colorValue) else value


# mark the keys and and the respective values in both json
def markChangedValues(changedValues,json1,json2):
    for k,v in changedValues.items():
        keyPath = k[4:]
        keyPath = keyPath.replace("][",",")
        keyPath=eval(keyPath)
        value1 = v["old_value"]
        value2 = v["new_value"]
        del_by_path(json1,keyPath)
        del_by_path(json2,keyPath)
        append_by_path(json1,keyPath,value1,colorValue=True)
        append_by_path(json2,keyPath,value2,colorValue=True)


# mark the keys that are present in one file but not in other      
def markChangedKeys(itemsAdded,d):
    for k in itemsAdded:
        keyPath = k[4:]
        key = "d"+keyPath
        value = eval(key)
        keyPath = keyPath.replace("][",",")
        keyPath=eval(keyPath)
        del_by_path(d,keyPath)
        append_by_path(d,keyPath,value,colorKey=True)


def findJsonDifference(path1: Path,path2: Path):
    # extract json contents from specified file path
    try:
        with path1.open() as f1:
            json_str1 = f1.read()
    except:
        print(colored(f"Unable to read file in '{path1}', please verify the path and filename alongwith the extension","red"))
        sys.exit()

    try:    
        with path2.open() as f2:
            json_str2 = f2.read()
    except:
        print(colored(f"Unable to read file in '{path2}', please verify the path and filename alongwith the extension","red"))
        sys.exit()

    # check if file contains an actual json
    try:
        json1 = json.loads(json_str1)
    except:
        print(colored(f"Invalid json in '{path1}'","red"))
        sys.exit()

    try:
        json2 = json.loads(json_str2)
    except:    
        print(colored(f"Invalid json in '{path2}'","red"))
        sys.exit()
    
    # check if the actual json is not empty
    if(not json1):
        print(colored(f"Empty json in '{path1}'","yellow"))
        sys.exit()
    if(not json2):
        print(colored(f"Empty json in '{path2}'","yellow"))
        sys.exit()
    
    diff=DeepDiff(json1,json2)
    result=dict(diff)
    
    # result=empty dict if both jsons are same
    if(not result):
        print(colored(f"JSON is same in both the files","green"))
        sys.exit()
    
    if("values_changed" in result):
        markChangedValues(result["values_changed"],json1,json2)
    if("dictionary_item_added" in result):
        markChangedKeys(result["dictionary_item_added"],json2)
    if("dictionary_item_removed" in result):
        markChangedKeys(result["dictionary_item_removed"],json1)
    formatOutput(json1,json2,path1.name,path2.name)

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonFilePath1", help="json file location path", type=Path)
    parser.add_argument("jsonFilePath2", help="json file location path", type=Path)

    try:
        args=parser.parse_args()
    except:
        print(colored("Arguments absent: please specify file paths as shown in the example below:","yellow"))
        print(colored("jdif example_1.json example_2.json","yellow"))
        sys.exit()
    else:
        if not isinstance(args.jsonFilePath1, PurePath):
            print(colored(f"'{args.jsonFilePath1}' not a valid file path","red"))
            sys.exit()
        if not isinstance(args.jsonFilePath2, PurePath):
            print(colored(f"'{args.jsonFilePath2}' not a valid file path","red"))
            sys.exit()
        findJsonDifference(args.jsonFilePath1, args.jsonFilePath2)


if __name__ == "__main__":
    start()