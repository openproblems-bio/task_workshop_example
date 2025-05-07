import anndata as ad
from sklearn.metrics import f1_score

## VIASH START
par = {
  "input_solution": "resources_test/task_template/solution.h5ad",
  "input_prediction": "resources_test/task_template/prediction.h5ad",
  "output": "output.h5ad"
}
meta = {
  "name": "f1"
}
## VIASH END

print("Reading input solution...", flush=True)
input_solution = ad.read_h5ad(par["input_solution"])
print(input_solution, flush=True)

print("Reading input prediction...", flush=True)
input_prediction = ad.read_h5ad(par["input_prediction"])
print(input_prediction, flush=True)

print("Calculating macro F1 score...", flush=True)
f1_macro = f1_score(
    input_solution.obs["label"],
    input_prediction.obs["label_pred"],
    average="macro",
    labels=input_solution.obs["label"].cat.categories,
)

print("Calculating weighted F1 score...", flush=True)
f1_weighted = f1_score(
    input_solution.obs["label"],
    input_prediction.obs["label_pred"],
    average="weighted",
    labels=input_solution.obs["label"].cat.categories,
)

uns_metric_ids = ["f1_macro", "f1_weighted"]
uns_metric_values = [f1_macro, f1_weighted]

print("Writing output AnnData to file...", flush=True)
output = ad.AnnData(
  uns={
    "dataset_id": input_prediction.uns["dataset_id"],
    "normalization_id": input_prediction.uns["normalization_id"],
    "method_id": input_prediction.uns["method_id"],
    "metric_ids": uns_metric_ids,
    "metric_values": uns_metric_values
  }
)
print(output, flush=True)
output.write_h5ad(par['output'], compression="gzip")

print("Done!", flush=True)
