# Project Deployment Guide (From Scratch)

## Requirements
- Git
- Docker
- Kubernetes (Minikube or GKE)
- Helm
- kubectl

## Steps

1. Clone the repository
```
git clone https://github.com/gan4cc/devops-final-project.git
cd devops-final-project
```

2. Start a Kubernetes cluster
```
minikube start
```

3. Deploy the backend
```
helm upgrade --install backend ./k8s/helm/backend
```

4. Verify pod status
```
kubectl get pods
```