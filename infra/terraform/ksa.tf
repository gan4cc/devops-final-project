resource "kubernetes_service_account_v1" "backend_ksa" {
  metadata {
    name      = "backend-ksa"
    namespace = "default"

    annotations = {
      "iam.gke.io/gcp-service-account" = google_service_account.backend_sa.email
    }
  }
}
