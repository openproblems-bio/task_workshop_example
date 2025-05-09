
import anndata as ad

# DATA LOADER ------------------------------------------------------------------

print("Loading data...")
adata = ad.read_h5ad("resources_test/common/cxg_mouse_pancreas_atlas//dataset.h5ad")
print(adata)

# DATA PROCESSOR ---------------------------------------------------------------

print("Creating train/test split...")
holdout_batch = adata.obs["batch"].to_list()[0]
train_adata = adata[adata.obs["batch"] != holdout_batch].copy()
test_adata = adata[adata.obs["batch"] == holdout_batch].copy()

# CONTROL METHODS --------------------------------------------------------------

predictions = {}

## True labels

print("Predicting true labels...")
obs_label_pred = test_adata.obs["cell_type"].to_list()
predictions["true_labels"] = obs_label_pred

## Random labels

import random
import numpy as np
random.seed(0)

print("Predicting random labels...")
obs_label_pred = np.random.choice(
    test_adata.obs["cell_type"].cat.categories,
    size=test_adata.shape[0],
    replace=True,
)
predictions["random_labels"] = obs_label_pred

# METHODS ----------------------------------------------------------------------

## Logistic regression

import sklearn.linear_model

print("Predicting logistic regression labels...")
classifier = sklearn.linear_model.LogisticRegression()
classifier.fit(train_adata.obsm["X_pca"], train_adata.obs["cell_type"].astype(str))
obs_label_pred = classifier.predict(test_adata.obsm["X_pca"])

predictions["logistic_regression"] = obs_label_pred

## SVM

import sklearn.svm

print("Predicting SVM labels...")
classifier = sklearn.svm.SVC()
classifier.fit(train_adata.obsm["X_pca"], train_adata.obs["cell_type"].astype(str))
obs_label_pred = classifier.predict(test_adata.obsm["X_pca"])

predictions["svm"] = obs_label_pred

# METRICS ----------------------------------------------------------------------

metric_scores = {key: {} for key in predictions.keys()}

## Accuracy

import numpy as np

print("Calculating accuracy...")
for method, obs_label_pred in predictions.items():
    accuracy = np.mean(test_adata.obs["cell_type"] == obs_label_pred)
    metric_scores[method]["accuracy"] = float(accuracy)

## F1 score
from sklearn.metrics import f1_score

print("Calculating F1 score...")
for method, obs_label_pred in predictions.items():
    f1 = f1_score(
        test_adata.obs["cell_type"],
        obs_label_pred,
        average="macro",
    )
    metric_scores[method]["f1"] = f1

print("Done!")
print(metric_scores)
