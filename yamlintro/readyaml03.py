#!/usr/bin/env python3

import yaml

def main():
    ## Open YAML file
    yammyfile = open("/home/student/mycode/yamlintro/myYAML.yml", "r")

    pyyammy = yaml.load(yammyfile)

    print(pyyammy)


main()
