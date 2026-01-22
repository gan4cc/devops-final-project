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

Before building and deploying the application, the pipeline performs the following validation steps:

- Python code linting using flake8
- Dependency validation during depenci installation
- Dockerfile best practices check Hadolint
- Container vulnerability scanning using Trivy (non-blocking, informational)

After successful validation, the pipeline:
- automatically runs on `push` to the `main` branch
- is triggered only when backend-related files change
- builds a Docker image for the backend service
- publishes the image to GitHub Container Registry (GHCR)

Manual pipeline execution is also supported via `workflow_dispatch`.

---

### Continuous Delivery (CD)

The project uses **controlled (manual) Continuous Delivery**.

- deployment is done using **Helm**
- the application is deployed to Kubernetes
- Kubernetes performs rolling updates
- application health is monitored using liveness and readiness probes
- rollback is supported through Kubernetes and Helm mechanisms

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

DEVOPS_FINAL_PROJECT/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── health.py
│   │   └── ...
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/
│   └── helm/
│       └── backend/
│
├── infra/
│   └── terraform/
│       ├── main.tf
│       ├── gke.tf
│       ├── iam.tf
│       ├── ksa.tf
│       ├── variables.tf
│       ├── terraform.tfvars
│       └── outputs.tf
│
├── docs/
│   ├── pictures/
│   │   ├── architecture.png
│   │   ├── cicd.png
│   │   └── monitoring.png
│   └── diagrams.md (опционально)
│
├── .github/
│   └── workflows/
│       └── backend-ci.yml
│
├── ARCHITECTURE.md
├── DEPLOYMENT+RUNBOOK.md
├── VERIFICATION.md
├── README.md
├── .gitignore
└── LICENSE.txt

---

## ✅ Summary

This project implements a **complete DevOps pipeline** with automated CI,
controlled CD, Kubernetes deployment, cloud infrastructure, and monitoring.

The project is ready for presentation and further development.