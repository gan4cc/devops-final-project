# DevOps Final Project

## 📌 Project Overview

This project is a **training DevOps project** that demonstrates the full lifecycle of a modern web application:
from development and containerization to Kubernetes deployment, monitoring, and infrastructure management.

The project is built using **open-source and cloud technologies** and closely follows real-world DevOps practices.

---

## 🎯 Project Goals

- Build a full **CI/CD pipeline**
- Containerize a backend application
- Deploy the application to Kubernetes
- Use Infrastructure as Code (IaC)
- Implement monitoring and observability
- Demonstrate hands-on DevOps skills

---

## 🧩 Project Architecture

### Backend
- **FastAPI (Python)**
- REST API
- Health checks (`/health`)
- File uploads to object storage

### Containerization
- Docker
- Docker image published to **GitHub Container Registry (GHCR)**

### Orchestration
- Kubernetes (GKE / local)
- Helm charts
- Deployment + Service
- Liveness / Readiness probes

### Cloud
- Google Cloud Platform
- Google Kubernetes Engine (GKE)
- Google Cloud Storage (Object Storage)

---

## 🔄 CI / CD

### Continuous Integration (CI)

CI is fully automated using **GitHub Actions**.

Pipeline:
- automatically runs on `push` to the `main` branch
- triggered **only when backend files change**
- builds a Docker image
- publishes the image to GHCR

Manual pipeline execution is also supported via `workflow_dispatch`.

---

### Continuous Delivery (CD)

The project uses **controlled (manual) Continuous Delivery**.

- deployment is done using **Helm**
- Kubernetes performs rolling updates
- application health is monitored via health checks
- rollback is possible using Kubernetes tools

Automatic deployment from GitHub Actions is **intentionally not enabled**
due to cloud security limitations and to maintain release control.

---

## 🏗 Infrastructure as Code

Infrastructure is managed using **Terraform**:

- Kubernetes cluster provisioning
- Service Accounts management
- IAM permissions
- Cloud resource configuration

---

## 🔐 Secrets and Security

- secrets are not stored in the codebase
- the following are used:
  - GitHub Secrets
  - Kubernetes Secrets
- role-based access control is applied

---

## 📊 Monitoring and Observability

- **Prometheus** — Kubernetes metrics collection
- **Grafana** — dashboards and visualization
- Kubernetes health checks

---

## 📁 Project Structure

```
backend/
k8s/helm/backend/
.github/workflows/
terraform/
```

---

## ✅ Summary

This project implements a **complete DevOps pipeline** with automated CI,
controlled CD, Kubernetes deployment, cloud infrastructure, and monitoring.

The project is ready for presentation and further development.