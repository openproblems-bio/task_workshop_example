# Introduction

This repository is designed as example of creating a new task for use in workshops.
It is based on the [`task_template` repository](https://github.com/openproblems-bio/task_template) but some components/files have been removed/edited so that they can re-created during the workshop.
**NOTE:** This means that the task is incomplete and some normal commands will fail until the steps below have been created.
Example solution files are included in the `solutions/` directory.

## Proof of concept

The `proof-of-concept.py` script contains a minimal label projection task.
This is the base that we we want to turn into proper components connected by a workflow.
Show the script and output to demonstrate what we want to do.

## 1. Update the task `_viash.yaml` config file

- Briefly explain and fill in the sections of the file
- Skip the test resources as this has already be configured to be the minimum needed for the example

## 2. Complete API files

- Copy the `comp_control_method.yaml` API file and modify it to create `comp_method.yaml` as an example of a component config file
  - Remove the `--input-solution` argument
  - Update the description
- Copy the `file_train.yaml` API file and modify it to create `comp_method.yaml` as an example of a component config file
  - Remove the `label` `obs` field
  - Update the description

## 3. Build the README

- Sync the test resource with `./script/sync_resources.sh`
- Build the `README` with `./common/scripts/create_task_readme`
- Show the `README` and explain the sections

## 4. Add a control method

- Run `./common/scripts/create_component -h` to show the options
- Run `./common/scripts/create_component --type control_method --name random_labels --language r`
  - This doesn't have to use R but it's the easiest example to transfer to another language
- Fill in the config file
- Fill in the script file
- Test the new component with `viash test src/control_methods/random_labels/config.vsh.yaml`
  - It can be good to deliberately introduce a minor error here to demonstrate and failed test and how fix it

## 5. Add a method

- Run `./common/scripts/create_component --type method --name svm --language python`
- Fill in the config file
  - Point out the extra references, links fields
  - Add `scikit-learn` as dependency to add to Docker
- Fill in the script file
  - Copy in the code from the proof of concept and show how it can be adapted to a component
- This example can be made more complex by adding an argument to set the kernel to use

## 6. Add a metric

- Run `./common/scripts/create_component --type metric --name f1 --language python`
- Fill in the config file
  - This is structured differently because one metric component can output multiple scores
- Fill in the script with content from the proof of concept
- (Optional) Copy the checks and assertions from the accuracy metric
- (Optional) Add a second F1 score with a different averaging method

## 7. Test the workflow

- Build components using `./scripts/project/build_all_docker_containers.sh`
  - Inspect `target/` with `tree target -L 3`
- Run test workflow with `./scripts/run_benchmark/run_test_local.sh`
- Inspect results folder with `tree temp/results/testrun_*/ `
  - Show metric scores in `temp_results/testrun_*/score_uns.yaml`

## 8. Add new components to the workflow

- Add dependencies to `run_benchmark/config.vsh.yaml`
- Add components to `run_benchmark/main.nf`
- Build components using `./scripts/project/build_all_docker_containers.sh`
- Run test workflow with `./scripts/run_benchmark/run_test_local.sh`
- Show new results

## Extensions

- If there is still time the participants can try to add more components:
- Suggestions
  - Methods: https://scikit-learn.org/stable/supervised_learning.html
  - Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
- Use the script to create a new component
- Complete the component
- Test the component
- Add the component to the workflow
- Run the test workflow

## Things that aren't covered

- Creating a data processor
- Creating test resources
