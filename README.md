# Python - K8s

## Description

This is a repository to learn how to use Kubernetes and deploy a simple web application.

### What I used
+ Docker
+ Kubernetes
+ Minikube
+ Python & FastAPI
+ Argocd

## How to use it

### Run the application in Docker locally

To run the app in Docker, you can use the following commands:

```bash
docker build -t python-k8s .
docker run -d -p 8000:8000 python-k8s
```

### Run the application in Kubernetes locally

To run the app in Kubernetes, you can use the following commands:

```bash
make start
```

This command will:
+ Check the dependencies
+ Setup the environment
+ Apply the Kubernetes manifests


### Run the application in Kubernetes with ArgoCD

To run the app in Kubernetes with ArgoCD, you can use the following commands:

```bash
make setup-argocd
```

To create an application in ArgoCD, you can:

#### Create the application using the CLI

```bash
argocd app create python-k8s \
    --repo https://github.com/leoneldgg/python-k8s
    --path kubernetes \
    --dest-server https://kubernetes.default.svc \
    --dest-namespace default \
    --sync-policy automated \
    --auto-prune \
    --self-heal \
    --auto-rollback \
```

#### Create the application using the UI

Using minikube, you can access the UI with the following command:

```bash
minikube service -n argocd argocd-server
```

To login, use the user **admin** and get the password with the following command:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Then, follow the steps:

1. Click on **New App**
2. Fill the **App Name** with **python-k8s**
3. Fill the **Project** with **default**
4. Fill the **Repository URL** with **https://github.com/leoneldgg/python-k8s**
5. Fill the **Path** with **kubernetes**
6. Fill the **Cluster URL** with **https://kubernetes.default.svc**
7. Fill the **Namespace** with **default**
8. Click on **Create**

This gonna take a while, but you can check the status of the application in the **Applications** tab.

### Access the application

To access the application, you can use the following commands:

```bash
minikube service python-k8s
```
