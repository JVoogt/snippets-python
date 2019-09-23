import json
import ast
# from fixedwidth.fixedwidth import FixedWidth
from FixedWidth_mod import FixedWidth
from copy import deepcopy

def readFixedWidth(fqdn):
    '''
        Use layout json file to decode positions in fixedWidth text files
    
    '''
    headers = ['HEAD001', 'HEAD002', 'HEAD005']
    configfile = 'layout.json'

    with open(configfile, 'r') as f:
        config = json.load(f)

    #Create FixedWidth Object
    fw_config = deepcopy(config)
    fw_configFiltered = {x: k for x, k in fw_config.items() if x in (headers)}
    fw_obj = FixedWidth(fw_configFiltered)

    sel = []
    #Read Sample file for imports
    with open(fqdn,"r",encoding="latin_1") as text:
        for lines in text:
            fw_obj.line = lines
            values = fw_obj.data
            sel.append(dict((k, values[k]) for k in (headers)))
    return sel

if __name__ == '__main__':
    fqdn = input('Please enter file name: ')
    file_obj = readFixedWidth(fqdn)
