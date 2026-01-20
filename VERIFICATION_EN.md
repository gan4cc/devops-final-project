# Application Verification Guide

1. Check pod status
```
kubectl get pods
```

2. Verify the health endpoint
```
kubectl port-forward svc/backend 8000:8000
curl http://localhost:8000/health
```

3. Open Swagger UI
```
http://localhost:8000/docs
```

4. Verify monitoring
- Open Grafana
- Check Kubernetes dashboards