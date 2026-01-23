
resource "google_service_account" "backend_sa" {
  account_id   = "backend-gcs-sa"
  display_name = "Backend GCS Service Account"
}
resource "google_storage_bucket" "uploads" {
  name     = "swagger-uploads"
  location = var.region

  uniform_bucket_level_access = true

  lifecycle {
    prevent_destroy = false
  }
}
