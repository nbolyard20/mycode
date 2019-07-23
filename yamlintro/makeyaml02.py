#!/usr/bin/env python3

#yaml is not standard
#python3 -m pip install pyyaml

import yaml

def main():
    ##create data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
            {"name": "Arther Dent", "species": "Human"}]

    print(hitchhikers)

    ## use the YAML library
    ## yaml uses .dump() to create YAML strings and write files
    ## json uses .dump() to create a string and dumps to write files
    yamlstring = yaml.dump(hitchhikers)

    print(yamlstring)

main()
