# envsplitter

Generates env files in folders specified by user.

# Motivation

Docker containers in a docker-compose setup need to share some environnement variables (exp: ports). These environnement variable may need to reside in a env_file, not be in the environnement. Some program may read configuration variable from a file. Instead of managing multiple .env file in each container, have one config file that will generate the .env for each container. By having one source of truth for your env variables, you don't have to bother the consistency between each .env file.

# How to use

1. Write a config file following schema [definition](# Schema definition)
2. Generate .env files

# Schema

## Schema definition

```
paths:

- string

env_vars:

- name: string
  destination: [Boolean] <--- See definition bellow
  value: any

```

## Field definition

- paths: List of paths where .env files should be generated. Paths are relative to config file.
- env_vars: List of all environnement variables
  - name: Name of the environnement variable
  - destination: Specify which .env file should contain this environnement variable. Each indexed boolean maps to the corresponding .env file as described in "paths" array. For example: a destination of [False, True, False] with paths of [".","..","..."] will include this environnement variable in the .env of parent folder ("..")
  - value: value of the environnement variable
