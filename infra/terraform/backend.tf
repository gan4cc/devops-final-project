terraform {
    backend "gcs" {
        bucket = "terraform-state-devops-final"
        prefix = "terraform/state"
    }
}