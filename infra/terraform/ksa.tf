resource "kubernetes_service_account_v1" "backend_ksa" {
  metadata {
    name      = "backend-ksa"
    namespace = "default"

    annotations = {
      "iam.gke.io/gcp-service-account" = google_service_account.backend_sa.email
    }
  }
}
resource "google_service_account_iam_member" "workload_identity_user" {
  service_account_id = google_service_account.backend_sa.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "serviceAccount:charismatic-sum-485115-k9.svc.id.goog[default/backend-ksa]"
}