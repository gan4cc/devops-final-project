terraform {
  backend "gcs" {
    bucket = "terraform-state-devops-final-bucket-v"
    prefix = "terraform/state"
  }
}