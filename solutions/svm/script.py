import anndata as ad
import sklearn.svm

## VIASH START
par = {
  "input_train": "resources_test/task_template/train.h5ad",
  "input_test": "resources_test/task_template/test.h5ad",
  "output": "output.h5ad",
  "kernel": "rbf"
}
meta = {
  "name": "svm"
}
## VIASH END

print("Reading training data...", flush=True)
input_train = ad.read_h5ad(par['input_train'])
print(input_train, flush=True)

print("Reading test data...", flush=True)
input_test = ad.read_h5ad(par['input_test'])
print(input_test, flush=True)

print("Training SVM model...", flush=True)
classifier = sklearn.svm.SVC(kernel=par["kernel"])
classifier.fit(input_train.obsm["X_pca"], input_train.obs["label"].astype(str))

print("Predicting labels for test data...", flush=True)
obs_label_pred = classifier.predict(input_test.obsm["X_pca"])

print("Writing output AnnData to file...", flush=True)
output = ad.AnnData(
  obs={
    "label_pred": obs_label_pred
  },
  uns={
    "dataset_id": input_train.uns["dataset_id"],
    "normalization_id": input_train.uns["normalization_id"],
    "method_id": meta["name"]
  }
)
output.obs_names = input_test.obs_names
print(output, flush=True)

output.write_h5ad(par["output"], compression="gzip")

print("Done!", flush=True)
