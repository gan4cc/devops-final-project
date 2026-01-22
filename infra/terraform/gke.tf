resource "google_container_cluster" "primary" {
  name     = "devops-final-gke"
  project  = var.project_id
  location = var.region

  depends_on = [
    google_project_service.container_api
  ]

  remove_default_node_pool = true
  initial_node_count       = 1

  node_config {
    disk_size_gb = 30
  }

  workload_identity_config {
    workload_pool = "${var.project_id}.svc.id.goog"
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "primary-nodes"
  project    = var.project_id
  cluster    = google_container_cluster.primary.name
  location   = var.region
  node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 30
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
