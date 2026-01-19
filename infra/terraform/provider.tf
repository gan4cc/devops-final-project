terraform {
  required_version = ">= 1.6"
  backend "gcs" {
    bucket  = "devops-final-project-uploads-bd5be"
    prefix  = "terraform/state"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}
provider "google" {
  project = "project-bd5be697-574d-46e6-9b8"
  region  = "us-central1" 
}
provider "kubernetes" {
  host  = "https://${google_container_cluster.primary.endpoint}"
  token = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(
    google_container_cluster.primary.master_auth[0].cluster_ca_certificate
  )
}
data "google_client_config" "default" {}
