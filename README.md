# Intro

This project helps to provision and maintain a performance monitoring
system based on collectd, InfluxDB, and Grafana. It comes with a 2-nodes
VirtualBox/Vagrant test environment.

## Notes

- Clients send signed/encrypted metrics to the servers for security.
- Clients send metrics to all the servers for redundancy.
- Grafana uses HTTP. For production please setup HTTPS.

# Setup

    vagrant up
    ansible-playbook -i environments/vagrant.py playbooks/site.yml
