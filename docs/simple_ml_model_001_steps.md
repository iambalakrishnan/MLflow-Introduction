# Section: 1 MLflow Introduction

## Introduction to MLflow

### What is [MLflow](https://mlflow.org/)?
MLflow is an open source platform for managing the machine learning lifecycle from start to finish.

MLflow is organized into four components: Tracking, Projects, Models, and Model Registry.Each of these components can be used independently. That means we can still track the model’s performance without exporting models in MLflow’s model format.

MLflow is designed to put as few constraints as possible and make codebase written in its format reproducible and reusable by multiple data scientists.


### MLflow Components
<img src="https://github.com/iambalakrishnan/MLflow-Introduction/blob/main/docs/images/index.jpg">


## Installation and first trial of MLflow

* First create the conda environment by the following command -

```bash
conda create --prefix ./env python=3.7 -y
```

* activate environment

```bash
conda actiavate ./env
```

* To use MLflow as a Python library, install it using `pip`. You can install MLflow by running: 

```bash
pip install mlflow
```

* Create the files as mentioned in the video lecture.
[Source code](## Installation and first trial of MLflow

* First create the conda environment by the following command -

```bash
conda create --prefix ./env python=3.7 -y
```

* activate environment

```bash
conda actiavate ./env
```

* To use MLflow as a Python library, install it using `pip`. You can install MLflow by running: 

```bash
pip install mlflow
```

* Create the files as mentioned .
[Source code](https://github.com/iambalakrishnan/MLflow-Introduction/blob/main/mlflow-codebase/simple-ML-model/simple_ML_model.py)