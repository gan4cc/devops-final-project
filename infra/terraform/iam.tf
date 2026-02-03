resource "google_storage_bucket" "uploads" {
  name     = var.uploads_bucket_name
  location = var.region
}

resource "google_storage_bucket_iam_member" "backend_storage_viewer" {
  bucket = google_storage_bucket.uploads.name
  role   = "roles/storage.objectViewer"
  member = google_service_account.backend_sa.member
}

resource "google_storage_bucket_iam_member" "backend_storage_creator" {
  bucket = google_storage_bucket.uploads.name
  role   = "roles/storage.objectCreator"
  member = google_service_account.backend_sa.member
}
