output "bucket_name" {
  value = google_storage_bucket.uploads.name
}

output "service_account_email" {
  value = google_service_account.backend_sa.email
}
