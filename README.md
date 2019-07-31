# Quotes API

A simple API that responds back with motivational quotes. Because we can all use a little motivation in our lives!

### What is this

A learning project to dabble with FastAPI and Kubernete Deployment Manifests.

### Getting Started

For easy deployment into a Kubernetes cluster, simple clone this repository, create the kubernetes secrets (see `k8s/readme.md`) and run the following from the repository root:

```shell
kubectl apply -f k8s/
```

If you want to build your own image with the provided Dockerfile, remember to replace the container `image:` keys.

Alternatively, if you want to run this locally for hacking:

```shell
# install your python requirements
pip install -r app/requirements.txt

# prepare your environment
source hack/prepare-env.sh

# run the local server
uvicorn hack/app:app --reload
```

