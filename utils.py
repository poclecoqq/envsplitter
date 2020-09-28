import os
import sys
import yaml


def _maps_to_file(path):
    return os.path.exists(path) and os.path.isfile(path)


def parse_cli_args():
    if len(sys.argv) < 2:
        exit('Please provide a path to a config file.')

    configs_path = sys.argv[1]
    if not _maps_to_file(configs_path):
        print("Provided path: " + os.path.abspath(configs_path))
        exit('No file found. Should map to a config file. Exiting.')

    return configs_path


def load_yml_file(yml_path):
    with open(yml_path, 'r') as stream:
        return yaml.load(stream, Loader=yaml.FullLoader)
