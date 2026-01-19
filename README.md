# DevOps Final Project

## Облачное DevOps веб-приложение на Kubernetes (GKE)

## 📌 Описание проекта

Данный проект демонстрирует полный DevOps-цикл разработки, развертывания
и эксплуатации веб-приложения в облаке.

Проект представляет собой backend-приложение на FastAPI, развернутое в
Google Kubernetes Engine (GKE), с возможностью загрузки файлов в Google
Cloud Storage, автоматическим CI/CD, инфраструктурой как код (Terraform)
и мониторингом (Prometheus + Grafana).

Проект реализован с использованием cloud-native best practices, включая
Workload Identity (без хранения сервисных ключей).

## 🧱 Архитектура решения

Пользователь → FastAPI Backend (Docker) → Kubernetes (GKE) → Workload
Identity (IAM) → Google Cloud Storage\
Параллельно: Prometheus → Grafana

## 🛠 Используемые технологии

-   Backend: Python 3.11, FastAPI, Uvicorn\
-   Контейнеризация: Docker\
-   Оркестрация: Kubernetes, Helm\
-   Облако: GCP, GKE, GCS\
-   Infrastructure as Code: Terraform\
-   CI/CD: GitHub Actions\
-   Мониторинг: Prometheus, Grafana

## 🔐 Безопасность

Аутентификация реализована через Workload Identity.\
JSON-ключи и Kubernetes Secrets для доступа к GCP не используются.

## ⚙️ Функциональность

-   REST API
-   /health --- health check
-   /upload --- загрузка файлов в GCS
-   Мониторинг pod и нод в Grafana

## 📁 Структура репозитория

    devops-final-project/
    ├── backend/
    ├── k8s/helm/backend/
    ├── infra/terraform/
    ├── .github/workflows/
    ├── .gitignore
    └── README.md

## ▶️ Запуск проекта (кратко)

1.  gcloud auth application-default login\
2.  gcloud container clusters get-credentials devops-final-gke\
3.  helm upgrade --install backend ./k8s/helm/backend\
4.  kubectl port-forward svc/backend 8000:8000

## 🎓 Назначение проекта

Учебный DevOps-проект для демонстрации навыков Kubernetes, CI/CD,
Terraform, мониторинга и cloud security.
