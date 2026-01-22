
resource "google_service_account" "backend_sa" {
  account_id   = "backend-gcs-sa"
  display_name = "Backend GCS Service Account"
}
