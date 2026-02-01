
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
resource "google_storage_bucket_iam_member" "backend_storage_viewer" {
  bucket = "swagger-uploads"
  role   = "roles/storage.objectViewer"
  member = google_service_account.backend_sa.member
}

resource "google_storage_bucket_iam_member" "backend_storage_creator" {
  bucket = google_storage_bucket.uploads.name
  role   = "roles/storage.objectCreator"
  member = google_service_account.backend_sa.member
}