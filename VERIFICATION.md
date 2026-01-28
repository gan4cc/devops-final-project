# Application Verification Guide

This document describes the steps required to verify that the application,
infrastructure, CI/CD pipelines, and monitoring stack are working correctly.

---

## 1. Application Verification

### Verify that pods are running
```bash
kubectl get pods
```

---

### Verify application health endpoint
```bash
kubectl port-forward svc/backend 8000:8000
```

Open in browser:
http://localhost:8000/health

---

### Verify API via Swagger UI
Open Swagger UI and test available API endpoints.

---

## 2. Kubernetes Verification

### Check deployments and services
```bash
kubectl get deployments
kubectl get services
```

---

### Verify application logs
```bash
kubectl logs <pod-name>
```

---

## 3. CI Verification

- Open GitHub Actions
- Verify successful execution of:
  - Backend CI pipeline
  - Terraform CI pipeline
- Ensure all pipeline steps completed without errors

---

## 4. Monitoring Verification

### Access Grafana
```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

### Get Grafana admin password
```bash
kubectl get secret monitoring-grafana -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 --decode
```

Open in browser:
http://localhost:3000

### Verify dashboards
- Kubernetes / Compute Resources / Pod
- Kubernetes / Compute Resources / Node (Pods)
- Kubernetes / Networking / Pod

---

## Verification Summary

- Application is running and responding correctly
- Kubernetes resources are healthy
- CI pipelines complete successfully
- Monitoring stack is operational
