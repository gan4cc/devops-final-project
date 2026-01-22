# Architecture Overview

## Application Architecture

![Application Architecture](docs/images/1.png)

The application follows a classic cloud-native architecture:
Frontend → Backend → Cloud Storage.

- Frontend: Swagger UI
- Backend: Stateless FastAPI service running in Kubernetes Pods
- Data Storage: Google Cloud Storage (GCS)
- The backend service is built with FastAPI and follows a modular Python application structure (backend/app)

---

## CI/CD Pipeline

![CI/CD Pipeline](docs/images/2.png)

The CI pipeline includes a pre-build validation stage to ensure code quality and container best practices.

CI/CD is implemented using GitHub Actions:
- Build Docker image
- Push image to GitHub Container Registry (GHCR)
- Deploy to Kubernetes using Helm

---

## Monitoring

![Monitoring Architecture](docs/images/3.png)

Monitoring stack includes:
- Prometheus for metrics collection
- Grafana for visualization and dashboards
