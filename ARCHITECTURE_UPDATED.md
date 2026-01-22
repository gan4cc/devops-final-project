# Project Architecture Diagram

## Application Architecture

```
+-----------------------------+
| Frontend                    |
| Swagger UI                  |
+-------------+---------------+
              |
              v
+-----------------------------+
| Backend                     |
| Stateless Service           |
| FastAPI                     |
| Kubernetes Pods             |
+-------------+---------------+
              |
              v
+-----------------------------+
| Data Storage                |
| Google Cloud Storage (GCS)  |
+-----------------------------+
```

The frontend layer is represented by **Swagger UI**, which is used to interact with the backend API.
The backend is implemented as a **stateless FastAPI service** running inside **Kubernetes pods**.
Uploaded files are stored in **Google Cloud Storage (GCS)**, which acts as the data storage layer.

---

## CI/CD Pipeline

```
CI/CD
  |
  v
GitHub Actions
  |
  v
Docker
  |
  v
Docker Image
  |
  v
GitHub Container Registry (GHCR)
  |
  v
Helm
  |
  v
Kubernetes Deployment
```

- **GitHub Actions** performs Continuous Integration
- **Docker** builds container images
- Images are pushed to **GitHub Container Registry (GHCR)**
- **Helm** deploys the application into **Kubernetes**

---

## Monitoring Architecture

```
Monitoring
   |
   v
Prometheus
   |
   v
Grafana
```

- **Prometheus** collects metrics from Kubernetes
- **Grafana** visualizes metrics using dashboards
