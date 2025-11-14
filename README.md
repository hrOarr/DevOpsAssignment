# DevOpsAssignment

A complete end-to-end DevOps environment built with **Vagrant**, **Ansible**, **Docker**, **Nginx**, **Prometheus**, **Grafana**, and **GitHub Actions CI/CD**.  
This project creates multiple VMs, deploys a containerized application, sets up load balancing, and implements real-time monitoring.

---

## 🔍 Project Overview  
In this project, I constructed a fully automated infrastructure pipeline where:

- ✔ Infrastructure is provisioned automatically  
- ✔ Applications are deployed uniformly across multiple servers  
- ✔ Traffic is load balanced across backend servers  
- ✔ System telemetry is collected and visualized  
- ✔ Code changes trigger automatic builds, image pushes, and deployments  

---

---

## 🚀 How to Run This Project  

### 1. Bring up the virtual machines  
```bash
vagrant up
```

### 2. Bootstrap all servers (install Docker etc.)
```bash
ansible-playbook -i ansible/inventory.ini ansible/bootstrap.yml
```

### 3. Deploy the web application
```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy_app.yml \
  --extra-vars "image_name=<your-dockerhub-user>/simple-web-app image_tag=<tag-or-sha>"
```

### 4. Configure reverse proxy / load balancing
```bash
ansible-playbook -i ansible/inventory.ini ansible/configure_nginx.yml
```

### 5. Install monitoring stack
```bash
ansible-playbook -i ansible/inventory.ini ansible/install_node_exporter.yml
ansible-playbook -i ansible/inventory.ini ansible/install_prometheus_grafana.yml
```
- Prometheus: http://192.168.123.14:9090
- Grafana: http://192.168.123.14:3000 (default login: admin/admin)

#### What This Setup Monitors
- CPU usage across all servers
- Memory utilization
- Disk usage and I/O
- Network throughput

### What You’ll Learn
- Infrastructure automation with Vagrant & VirtualBox
- Configuration management and deployment with Ansible
- Packaging applications using Docker
- Load balancing using Nginx
- Setting up monitoring using Prometheus + Node Exporter
- Visualizing metrics with Grafana
- CI/CD pipeline automation with GitHub Actions
