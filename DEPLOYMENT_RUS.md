
# Инструкция по развёртыванию проекта с нуля

## Требования
- Git
- Docker
- Kubernetes (Minikube или GKE)
- Helm
- kubectl

## Шаги
1. Клонировать репозиторий
```
git clone https://github.com/gan4cc/devops-final-project.git
cd devops-final-project
```

2. Запустить Kubernetes кластер (minikube start)

3. Установить backend
```
helm upgrade --install backend ./k8s/helm/backend
```

4. Проверить pod
```
kubectl get pods
```

