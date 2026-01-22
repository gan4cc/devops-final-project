terraform {
  backend "gcs" {
    bucket = "terraform-state-devops-final-bucket"
    prefix = "terraform/state"
  }
}