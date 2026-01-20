
# Инструкция по проверке работоспособности

1. Проверить состояние pod'ов
```
kubectl get pods
```

2. Проверить health endpoint
```
kubectl port-forward svc/backend 8000:8000
curl http://localhost:8000/health
```

3. Открыть Swagger UI
```
http://localhost:8000/docs
```

4. Проверить мониторинг
- Открыть Grafana
- Проверить Kubernetes dashboards
