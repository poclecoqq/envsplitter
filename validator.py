from cerberus import Validator
from schema import schema
import os


def _maps_to_folder(path):
    return os.path.exists(path) and os.path.isdir(path)


def validate_yml_file(yml_file, yml_file_dir):
    v = Validator(schema)
    if not v.validate(yml_file):
        print(v.errors)
        exit('Please follow schema definition as declared in schema.py. Exiting.')

    hasErrors = False
    for path in yml_file['paths']:
        if not _maps_to_folder(os.path.join(yml_file_dir, path)):
            hasErrors = True
            print("Provided path: " +
                  os.path.abspath(os.path.join(yml_file_dir, path)))
    if hasErrors:
        exit('No directory found for previous paths. Exiting.')
