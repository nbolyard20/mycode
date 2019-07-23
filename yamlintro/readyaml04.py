#!/usr/bin/env python3

import yaml

def main():
    ## Open YAML file
    yammyfile = open("/home/student/mycode/yamlintro/myYAML.yml", "r")

    pyyammy = yaml.load(yammyfile)

    print(pyyammy)

    pyyammy[0]['apps'].append('minecraft')
    print(pyyammy)

    yammyfile2 = open("/home/student/mycode/yamlintro/myYAML.yml.updated", "w")

    yaml.dump(pyyammy, yammyfile2)

    yammyfile2.close()


main()
