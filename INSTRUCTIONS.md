# Introduction

This repository is designed as example of creating a new task for use in workshops.
It is based on the [`task_template` repository](https://github.com/openproblems-bio/task_template) but some components/files have been removed/edited so that they can re-created during the workshop.
**NOTE:** This means that the task is incomplete and some normal commands will fail until the steps below have been created.
Example solution files are included in the `solutions/` directory.

## Proof of concept

The `proof-of-concept.py` script contains a minimal label projection task.
This is the base that we we want to turn into proper components connected by a workflow.
Show the script and output to demonstrate what we want to do.

## Update the task `_viash.yaml` config file

- Briefly explain and fill in the sections of the file
- Skip the test resources as this has already be configured to be the minimum needed for the example

## Complete API files

- Copy the `comp_control_method.yaml` API file and modify it to create `comp_method.yaml` as an example of a component config file
  - Remove the `--input-solution` argument
  - Update the description
- Copy the `file_train.yaml` API file and modify it to create `comp_method.yaml` as an example of a component config file
  - Remove the `label` `obs` field
  - Update the description
