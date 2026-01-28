# DevOps Final Project

## 📌 Project Overview

This project is a **training DevOps project** that demonstrates the full lifecycle of a modern web application:
from development and containerization to Kubernetes deployment, monitoring, and infrastructure management.

The project is built using **open-source and cloud technologies** and closely follows real-world DevOps practices, including Infrastructure as Code and CI/CD automation.

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
- FastAPI (Python)
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
- Rolling updates

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
- Dependency validation during dependency installation
- Dockerfile best practices check Hadolint
- Container vulnerability scanning using Trivy (non-blocking, informational)

After successful validation, the pipeline:
- automatically runs on `push` to the `main` branch
- is triggered only when backend-related files change
- builds a Docker image for the backend service
- publishes the image to GitHub Container Registry (GHCR)
- deploys the application to Kubernetes using Helm

Manual pipeline execution is also supported via `workflow_dispatch`.

---

### Continuous Delivery (CD)

The project uses **controlled (manual) Continuous Delivery**.

- application deployment is performed using **Helm**
- deployment is executed from GitHub Actions
- Kubernetes performs rolling updates
- application health is monitored using liveness and readiness probes
- rollback is supported via Helm and Kubernetes mechanisms

Deployment is automated but remains controlled through CI/CD pipelines.

---

## 🏗 Infrastructure as Code

Infrastructure is managed using **Terraform**.

Terraform is responsible for:
- Google Kubernetes Engine (GKE) cluster provisioning
- Node pool management
- Service Accounts and IAM permissions
- Workload Identity configuration
- Cloud resource configuration

---

## Terraform CI/CD

Infrastructure changes are handled via a dedicated **Terraform CI pipeline**:
- terraform init
- terraform fmt
- terraform validate
- terraform plan

terraform apply is executed only in GitHub Actions
and only after merge to the main branch.

Local usage is limited to terraform init and terraform plan.
Local terraform apply is intentionally disabled by process.

Terraform state is stored remotely in Google Cloud Storage.


## 🔐 Secrets and Security

- Secrets are not stored in the codebase
- The following are used:
  - GitHub Secrets
  - Kubernetes Secrets
- Authentication to Google Cloud from CI/CD uses Workload Identity
- No static JSON service account keys are used
- Role-based access control (RBAC) is applied

---

## 📊 Monitoring and Observability

- **Prometheus** — Kubernetes metrics collection
- **Grafana** — dashboards and visualization
- Kubernetes health checks
- Application-level health endpoint

---

## 📁 Project Structure

DEVOPS_FINAL_PROJECT/
│
├── .github/
│   └── workflows/
│       ├── backend-ci.yml          # CI/CD для backend (build, scan, deploy)
│       └── terraform-ci.yml        # CI/CD для Terraform (init, plan, apply)
│
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI application
│   │   ├── health.py               # Health endpoint
│   │   └── __pycache__/             # (gitignored)
│   │
│   ├── Dockerfile                  # Backend Docker image
│   └── requirements.txt            # Python dependencies
│
├── infra/
│   └── terraform/
│       ├── apis.tf                 # Enable required GCP APIs
│       ├── backend.tf              # Terraform backend (GCS state)
│       ├── gke.tf                  # GKE cluster definition
│       ├── node_pool.tf            # GKE node pool
│       ├── iam.tf                  # IAM roles and bindings
│       ├── ksa.tf                  # Kubernetes Service Account + WI
│       ├── provider.tf             # Terraform providers
│       ├── variables.tf            # Variable definitions
│       ├── terraform.tfvars        # Environment values
│       ├── locals.tf               # Reusable local values
│       ├── outputs.tf              # Outputs for CI/debug
│       ├── main.tf                 # Root module
│       ├── .terraform.lock.hcl     # Provider lock file
│       └── .terraform/             # Terraform cache (gitignored)
│
├── k8s/
│   └── helm/
│       └── backend/
│           ├── Chart.yaml          # Helm chart metadata
│           ├── values.yaml         # Helm values
│           └── templates/
│               ├── deployment.yaml
│               ├── service.yaml
│
├── docs/
│   └── images/
│       ├── architecture.png
│       ├── cicd.png
│       └── monitoring.png
│
├── ARCHITECTURE.md                 # Architecture description
├── DEPLOYMENT+RUNBOOK.md            # Deployment & operations guide
├── VERIFICATION.md                  # Verification steps
├── README.md                        # Project overview
│
├── .gitignore
└── LICENSE.txt

---

## ✅ Summary

This project implements a complete **DevOps lifecycle**:
- Infrastructure as Code with Terraform
- Automated CI and controlled CD
- Kubernetes-based deployment
- Secure authentication using Workload Identity
- Monitoring and observability

The project follows production-oriented DevOps practices and is ready for presentation and further development.