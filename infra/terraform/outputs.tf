output "service_account_email" {
  description = "GCP Service Account email"
  value       = local.gsa_email
}

output "cluster_name" {
  description = "GKE cluster name"
  value       = var.cluster_name
}
