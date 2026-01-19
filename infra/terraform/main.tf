resource "google_storage_bucket" "uploads" {
  name          = var.bucket_name
  location      = var.region
  force_destroy = true

  uniform_bucket_level_access = true
}
resource "google_service_account" "backend_sa" {
  account_id   = "backend-gcs-sa"
  display_name = "Backend GCS Service Account"
}
resource "google_storage_bucket_iam_member" "backend_access" {
  bucket = google_storage_bucket.uploads.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.backend_sa.email}"
}
