# envsplitter

Generates env files in folder specified by user.

# Motivation

Docker container need to share some environnement variables (exp: ports). Instead of managing multiple .env file in each container, have one config file that will generate the config files with shared variables. By having one source of truth for your env variables, you don't have to bother the consistency between each .env file.

# How to use

1. Write a config file following schema [definition](# Schema definition)
2. Generate .env files

# Schema

## Schema definition

"""
paths:

- string

env_vars:

- name: string
  destination: [Boolean] <--- See definition bellow
  value: any

"""

## Field definition

- paths: List of paths where .env files should be generated
- env_vars: List of all environnement variables
  - name: Name of the environnement variable
  - destination: Specify which .env file should contain this environnement variable. Each indexed boolean maps to the corresponding .env file as described in "paths" array. For example: a destination of [False, True, False] with paths of [".","..","..."] will include this environnement variable in the .env of parent folder ("..")
  - value: value of the environnement variable
