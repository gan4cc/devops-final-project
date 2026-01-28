locals {
  gsa_name = "backend-gcs-sa"
  ksa_name = "backend-ksa"

  gsa_email = "${local.gsa_name}@${var.project_id}.iam.gserviceaccount.com"
}
