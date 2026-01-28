resource "kubernetes_service_account_v1" "backend_ksa" {
  metadata {
    name      = local.ksa_name
    namespace = var.namespace

    annotations = {
      "iam.gke.io/gcp-service-account" = local.gsa_email
    }
  }
}

resource "google_service_account_iam_member" "workload_identity_user" {
  service_account_id = google_service_account.backend_sa.name
  role               = "roles/iam.workloadIdentityUser"

  member = "serviceAccount:${var.project_id}.svc.id.goog[${var.namespace}/${local.ksa_name}]"
}
