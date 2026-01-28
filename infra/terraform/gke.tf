resource "google_container_cluster" "primary" {
  name     = var.cluster_name
  location = var.region

  depends_on = [
    google_project_service.container_api
  ]

  # Убираем дефолтный node pool
  remove_default_node_pool = true
  initial_node_count       = 1

  # Включаем Workload Identity
  workload_identity_config {
    workload_pool = "${var.project_id}.svc.id.goog"
  }
}
