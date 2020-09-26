import yaml
import argparse
from io import StringIO
from cerberus import Validator
import os

from schema import schema


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Path to config file")

    args = parser.parse_args()
    config = args.config
    if not config:
        exit('Please provde a path to config file with -c. Exiting.')
    if not maps_to_file(config):
        exit('Provided config path should map to a config file. Exiting.')
    return config


def load_yml_file(yml_path):
    with open(yml_path, 'r') as stream:
        return yaml.load(stream, Loader=yaml.FullLoader)


def maps_to_file(path):
    return os.path.exists(path) and os.path.isfile(path)


def maps_to_folder(path):
    return os.path.exists(path) and os.path.isdir(path)


def validate_yml_file(yml_file):
    v = Validator(schema)
    if not v.validate(yml_file):
        print(v.errors)
        exit('Please follow schema definition as declared in schema.py. Exiting.')
    if not all([maps_to_folder(path) for path in yml_file['paths']]):
        exit("All provided paths in config file should exists and be directories. Exiting.")


def generate_env_files(yml_file):
    buffers = [StringIO() for _ in yml_file['paths']]
    for env_var in yml_file['env_vars']:
        for i in range(len(env_var['destination'])):
            if env_var['destination'][i]:
                buffers[i].write(env_var['name']+"="+env_var['value'] + "\n")
    for i in range(len(yml_file['paths'])):
        env_path = os.path.join(yml_file['paths'][i], ".env")
        with open(env_path, "w") as f:
            f.write(buffers[i].getvalue())
            f.close()
            buffers[i].close()


config = parse_cli_args()
yml_file = load_yml_file(config)
validate_yml_file(yml_file)
generate_env_files(yml_file)
