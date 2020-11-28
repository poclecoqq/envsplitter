import os
import sys
import yaml
import argparse


def _maps_to_file(path):
    return os.path.exists(path) and os.path.isfile(path)


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="Name of the output file ", type=str)
    parser.add_argument("inputFile", help="Path to the input file", type=str)

    args = parser.parse_args()
    if not _maps_to_file(args.inputFile):
        print("Provided path: " + os.path.abspath(args.inputFile))
        exit('No file found. Should map to a config file. Exiting.')

    return args.inputFile, args.o


def load_yml_file(yml_path):
    with open(yml_path, 'r') as stream:
        return yaml.load(stream, Loader=yaml.FullLoader)
