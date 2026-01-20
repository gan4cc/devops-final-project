# Application Verification Guide

1. Check pod status
```
kubectl get pods
```

2. Verify the health endpoint
```
kubectl port-forward svc/backend 8000:8000
http://localhost:8000/health
```

3. Open Swagger UI
```
http://localhost:8000/docs
```

4. Verify monitoring
- Open Grafana 
- kubectl port-forward svc/monitoring-grafana \-n monitoring 3000:80
login: admin
Password:
kubectl get secret monitoring-grafana -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 --decode

http://localhost:3000/

- Check Kubernetes dashboards:
  Kubernetes / Compute Resources / Pod
  Kubernetes / Compute Resources / Node (Pods)
  Kubernetes / Networking / Pod
etc.