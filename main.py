from io import StringIO
import os
from utils import parse_cli_args, load_yml_file
from validator import validate_yml_file


def generate_env_files(yml_file, yml_file_dir, output_file_name):
    buffers = [StringIO() for _ in yml_file['paths']]

    # Output env variable in desired buffers
    for env_var in yml_file['env_vars']:
        for i in range(len(env_var['destination'])):
            if env_var['destination'][i]:
                buffers[i].write(env_var['name']+"="+env_var['value'] + "\n")

    # Create env files with bufferizes content
    for i in range(len(yml_file['paths'])):
        env_path = os.path.join(
            yml_file_dir, yml_file['paths'][i], output_file_name + ".env")
        with open(env_path, "w") as f:
            f.write(buffers[i].getvalue())
            f.close()
            buffers[i].close()


yml_file_path, output_file_name = parse_cli_args()
yml_file = load_yml_file(yml_file_path)
yml_file_dir = os.path.dirname(yml_file_path)

validate_yml_file(yml_file, yml_file_dir)
generate_env_files(yml_file, yml_file_dir, output_file_name)
