import anndata as ad
from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder

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

# Check obs_names are consistent
assert (input_prediction.obs_names == input_solution.obs_names).all(), "obs_names not the same in prediction and solution inputs"

print("Encoding labels...", flush=True)
cats = list(input_solution.obs["label"].dtype.categories) + list(input_prediction.obs["label_pred"].dtype.categories)
encoder = LabelEncoder().fit(cats)
input_solution.obs["label"] = encoder.transform(input_solution.obs["label"])
input_prediction.obs["label_pred"] = encoder.transform(input_prediction.obs["label_pred"])

print("Calculating macro F1 score...", flush=True)
f1_macro = f1_score(
    input_solution.obs["label"],
    input_prediction.obs["label_pred"],
    average="macro",
)

print("Calculating weighted F1 score...", flush=True)
f1_weighted = f1_score(
    input_solution.obs["label"],
    input_prediction.obs["label_pred"],
    average="weighted",
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
