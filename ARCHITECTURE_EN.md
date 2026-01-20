# Project Architecture Diagram

```
+-------------------+
|    Frontend       |
|  (Swagger UI)     |
+---------+---------+
          |
          v
+-------------------+
|    Backend        |
|  FastAPI          |
|  Kubernetes Pod   |
+---------+---------+
          |
          v
+-------------------+
| Data Storage      |
| Google Cloud      |
| Storage (GCS)     |
+-------------------+

CI:
GitHub Actions -> Docker Image -> GHCR

CD:
Helm -> Kubernetes
