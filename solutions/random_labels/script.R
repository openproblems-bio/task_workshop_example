library(anndata)

## VIASH START
par <- list(
  input_train = "resources_test/task_template/train.h5ad",
  input_test = "resources_test/task_template/test.h5ad",
  input_solution = "resources_test/task_template/solution.h5ad",
  output = "output.h5ad"
)
meta <- list(
  name = "random_labels"
)
## VIASH END

cat("Reading training data...\n")
input_train <- anndata::read_h5ad(par[["input_train"]])
print(input_train)

cat("Reading test data...\n")
input_test <- anndata::read_h5ad(par[["input_test"]])
print(input_test)

cat("Assign random labels...\n")
label_categories <- unique(input_train$obs[["label"]])
cat("Found, ", length(label_categories), "labels\n")
random_labels <- sample(label_categories, size = input_test$n_obs, replace = TRUE)

cat("Writing output AnnData to file...\n")
output <- anndata::AnnData(
  obs = data.frame(
    row.names = input_test$obs_names,
    label_pred = random_labels
  ),
  uns = list(
    dataset_id = input_test$uns[["dataset_id"]],
    normalization_id = input_test$uns[["normalization_id"]],
    method_id = meta$name
  ),
  shape = c(input_test$n_obs, 0L),
)
print(output)
output$write_h5ad(par[["output"]], compression = "gzip")

cat("Done!\n")
