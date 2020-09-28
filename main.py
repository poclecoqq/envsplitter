import yaml
from io import StringIO
from cerberus import Validator
import os
import sys

from schema import schema


def _parse_cli_args():
    config_path = sys.argv[1]
    if not config_path:
        exit('Please provide a path to a config file.')
    return config_path


def _load_yml_file(yml_path):
    with open(yml_path, 'r') as stream:
        return yaml.load(stream, Loader=yaml.FullLoader)


def _maps_to_file(path):
    return os.path.exists(path) and os.path.isfile(path)


def _maps_to_folder(path):
    return os.path.exists(path) and os.path.isdir(path)


def _validate_yml_file(yml_file, yml_file_path):
    v = Validator(schema)
    if not v.validate(yml_file):
        print(v.errors)
        exit('Please follow schema definition as declared in schema.py. Exiting.')

    hasErrors = False
    for path in yml_file['paths']:
        if not _maps_to_folder(os.path.join(yml_file_path, path)):
            hasErrors = True
            print("Provided path: " +
                  os.path.abspath(os.path.join(yml_file_path, path)))
    if hasErrors:
        exit('No directory found for previous paths. Exiting.')

    if not all([_maps_to_folder(os.path.join(yml_file_path, path)) for path in yml_file['paths']]):
        exit("All provided paths in config file should exists and be directories. Exiting.")


def _generate_env_files(yml_file, yml_file_path):
    buffers = [StringIO() for _ in yml_file['paths']]
    for env_var in yml_file['env_vars']:
        for i in range(len(env_var['destination'])):
            if env_var['destination'][i]:
                buffers[i].write(env_var['name']+"="+env_var['value'] + "\n")
    for i in range(len(yml_file['paths'])):
        env_path = os.path.join(yml_file_path, yml_file['paths'][i], ".env")
        with open(env_path, "w") as f:
            f.write(buffers[i].getvalue())
            f.close()
            buffers[i].close()


def generate_env_files(configs_path):
    if not _maps_to_file(configs_path):
        print("Provided path: " + os.path.abspath(configs_path))
        exit('No file found. Should map to a config file. Exiting.')

    yml_file = _load_yml_file(configs_path)
    _validate_yml_file(yml_file, os.path.dirname(configs_path))
    _generate_env_files(yml_file, os.path.dirname(configs_path))


if __name__ == "__main__":
    configs_path = _parse_cli_args()
    generate_env_files(configs_path)
