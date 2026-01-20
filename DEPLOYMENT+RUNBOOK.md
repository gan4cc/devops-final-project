## Runbook: Commands for Launching a DevOps Final Project

## Environment preparations
•	git --version
•	docker --version
•	kubectl version --client
•	helm version
•	terraform version
•	gcloud version

## Work with Git
•	git clone https://github.com/gan4cc/devops-final-project.git
•	cd devops-final-project
•	git status
•	git add .
•	git commit -m "Commit message"
•	git push
•	git pull --rebase origin main

## Autentification GCP
•	gcloud auth application-default login
•	gcloud auth list

## Terraform
•	cd infra/terraform
•	terraform init
•	terraform plan
•	terraform apply

## Connection to  GKE
•	gcloud container clusters get-credentials devops-final-gke --region us-central1 --project PROJECT_ID
•	kubectl get nodes

## Docker
•	docker login ghcr.io -u gan4cc
•	docker build -t ghcr.io/gan4cc/devops-final-project/backend:latest backend
•	docker push ghcr.io/gan4cc/devops-final-project/backend:latest

## Kubernetes & Helm
•	helm upgrade --install backend ./k8s/helm/backend
•	kubectl rollout restart deployment backend
•	kubectl get pods

## API Check
•	kubectl port-forward svc/backend 8000:8000
•	http://localhost:8000/docs
## Monitoring
•	kubectl create namespace monitoring
•	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
•	helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
•   kubectl get pods -n monitoring - Prometheus pods check 
•   kubectl get pods -n monitoring | grep grafana - Grafana pod check
•	kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
•   http://localhost:3000/

