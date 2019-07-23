#!/usr/bin/env python3

#yaml is not standard
#python3 -m pip install pyyaml

import yaml

def main():
    ##create data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
            {"name": "Arther Dent", "species": "Human"}]

    print(hitchhikers)

    ## Opening a new file to write to
    zfile = open("galaxyguide.yaml", "w")

    ## use the YAML library
    ## yaml uses .dump() to create YAML strings and write files
    ## json uses .dump() to create a string and dumps to write files
    yaml.dump(hitchhikers, zfile)

    ## close the file when finished
    zfile.close()

main()
