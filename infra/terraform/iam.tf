resource "google_service_account_iam_member" "workload_identity" {
  service_account_id = google_service_account.backend_sa.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "serviceAccount:${var.project_id}.svc.id.goog[default/backend-ksa]"

  depends_on = [
    google_container_cluster.primary
  ]
}
