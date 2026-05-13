# Production-Ready Flask Travel Platform Deployment on AWS EKS using Terraform, Docker, Kubernetes, Prometheus & Grafana 🚀

A production-style cloud-native deployment project demonstrating how to provision and manage an Amazon EKS (Elastic Kubernetes Service) cluster using Terraform, deploy a containerized Python Flask application on Kubernetes, and implement monitoring using Prometheus and Grafana.

---

# 📌 Project Overview

This project demonstrates an end-to-end Kubernetes deployment workflow on AWS using Infrastructure as Code (IaC), containerization, Kubernetes orchestration, and observability tools.

The project includes:

- AWS EKS Cluster Provisioning using Terraform
- Dockerized Python Flask Travel Platform Application
- Kubernetes Deployment & LoadBalancer Service
- Monitoring Stack using Prometheus & Grafana
- Kubernetes Cluster & Application Metrics Monitoring

---

# 🏗️ Architecture

```text
Users
   |
AWS LoadBalancer
   |
Amazon EKS Cluster
   |
Flask Travel Platform Pods
   |
Prometheus
   |
Grafana Dashboard
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| AWS EKS | Managed Kubernetes Cluster |
| Terraform | Infrastructure as Code |
| Docker | Containerization |
| Kubernetes | Container Orchestration |
| Python Flask | Web Application |
| Prometheus | Metrics Collection |
| Grafana | Monitoring Dashboard |
| DockerHub | Container Registry |
| kubectl | Kubernetes CLI |
| Helm | Kubernetes Package Manager |

---

# 📂 Project Structure

```bash
terraform-eks-travel-platform/
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── provider.tf
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── templates/
│   └── static/
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── travel-platform-monitor.yaml
│
├── grafana/
│   └── travel-platform-dashboard.json
│
├── screenshots/
│
└── README.md
```

---

# 🚀 Features Implemented

## ✅ Infrastructure Provisioning using Terraform

- Provisioned AWS EKS Cluster
- Created VPC, Subnets, IAM Roles
- Configured EC2 Node Groups
- Managed Infrastructure using Terraform HCL

---

## ✅ Dockerized Flask Application

- Built a Python Flask-based Travel Platform
- Created Docker Image
- Pushed Image to DockerHub Registry

---

## ✅ Kubernetes Deployment

- Created Kubernetes Deployment Manifest
- Created Kubernetes Service of type LoadBalancer
- Deployed Application on Amazon EKS

---

## ✅ Monitoring & Observability

- Integrated Prometheus Metrics Endpoint (`/metrics`)
- Installed kube-prometheus-stack using Helm
- Configured Prometheus ServiceMonitor
- Built Grafana Dashboard for:
  - Application Request Metrics
  - Pod CPU Usage
  - Pod Memory Usage
  - Pod Restart Count
  - Cluster Monitoring

---

# 🐳 Docker Commands

## Build Docker Image

```bash
docker build -t <dockerhub-username>/travel-platform:v1 .
```

## Push Docker Image

```bash
docker push <dockerhub-username>/travel-platform:v1
```

---

# ☁️ Terraform Commands

## Initialize Terraform

```bash
terraform init
```

## Preview Infrastructure

```bash
terraform plan
```

## Provision EKS Cluster

```bash
terraform apply
```

---

# ☸️ Kubernetes Deployment

## Apply Kubernetes Manifests

```bash
kubectl apply -f k8s/
```

## Verify Resources

```bash
kubectl get pods
kubectl get svc
kubectl get nodes
```

---

# 📊 Monitoring Stack Setup

## Install kube-prometheus-stack

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
```

---

# 📈 Grafana Dashboard Metrics

The Grafana dashboard monitors:

- Total HTTP Requests
- Request Rate
- Pod CPU Usage
- Pod Memory Usage
- Pod Restart Count
- Kubernetes Cluster Metrics

---

# 📸 Screenshots to Include

Create a `screenshots/` folder and include the following:

| Screenshot | Description |
|---|---|
| grafana-dashboard.png | Grafana Monitoring Dashboard |
| prometheus-targets.png | Prometheus Targets showing app status UP |
| eks-pods.png | Kubernetes Pods running in EKS |
| flask-homepage.png | Flask Travel Platform Homepage |
| terraform-apply.png | Terraform Infrastructure Provisioning |
| loadbalancer-service.png | Kubernetes LoadBalancer Service |

---

# 🔍 Prometheus Metrics Endpoint

```text
/metrics
```

Example metric:

```text
app_requests_total
```

---

# 📚 Key Learnings

Through this project, I gained hands-on experience with:

- Infrastructure as Code (Terraform)
- Kubernetes & Amazon EKS
- Docker Containerization
- Kubernetes Networking & LoadBalancers
- Monitoring & Observability
- Prometheus & Grafana Integration
- Kubernetes Deployments & Services
- Cloud-Native Application Deployment

---

# 🚧 Future Improvements

- CI/CD using GitHub Actions
- HTTPS using AWS ACM
- ALB Ingress Controller
- Horizontal Pod Autoscaler (HPA)
- Fluent Bit + CloudWatch Logging
- ArgoCD GitOps
- Terraform Modules
- OpenTelemetry & Jaeger Tracing

---

# 👨‍💻 Author

Biswarup Basak

---

# ⭐ If you found this project useful, consider giving it a star!
