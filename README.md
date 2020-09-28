# envsplitter

Generates env files in directories specified by user.

# Motivation

Docker containers in a docker-compose setup need to share some environment variables (exp: ports). These environment variable may need to reside in a env_file, not be in the environment. Some program may read configuration variable from a file. Instead of managing multiple .env file in each container, have one config file that will generate the .env for each container. By having one source of truth for your env variables, you don't have to bother the consistency between each .env file.

# How to use

## General steps
1. Write a config file following schema [definition](# Schema definition)
2. Generate .env files

## Call from the CLI
```
python3 main.py [PATH TO CONFIG FILE]
```
## Call from python project
```
import generate_env_files from envsplitter.main
generate_env_files(PATH_TO_CONFIG_FILE)
```
# Schema

## Schema definition

```
paths:

- string

env_vars:

- name: string
  destination: [Boolean]
  value: any

```

## Field definition

- paths: List of paths where .env files should be generated. Paths are relative to config file.
- env_vars: List of all environment variables
  - name: Name of the environment variable
  - destination: Specify which .env file should contain this environment variable. Each indexed boolean maps to the corresponding .env file as described in "paths" array. For example: a destination of [False, True, False] with paths of [".","..","..."] will include this environment variable in the .env of parent directory ("..")
  - value: value of the environment variable
