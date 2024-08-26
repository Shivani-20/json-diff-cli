import jdif
from termcolor import colored
from pathlib import Path

def test_same_json(capsys):
    p1 = Path(__file__).with_name('j1.json')
    p2 = Path(__file__).with_name('j2.json')
    jdif.findJsonDifference(p1,p2)
    out,err = capsys.readouterr()
    assert out == colored("JSON is same in both the files","green")+"\n"