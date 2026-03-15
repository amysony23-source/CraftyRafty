**<u>CraftyRafty:</u>**

A cybersecurity monitoring and incident response lab built with Python and Docker.  
CraftyRafty simulates real-world attacks on a vulnerable Flask web application and demonstrates security monitoring, vulnerability scanning, SIEM log analysis, and automated incident response.

**<u>Features:</u>**

- Vulnerable Flask web application for attack simulation
- Containerized deployment using Docker
- Network intrusion detection using Suricata IDS
- Centralized log monitoring using ELK Stack (Elasticsearch, Logstash, Kibana)
- Vulnerability scanning using Nmap
- Automated incident response with dynamic IP blocking
- Security event logging and analysis

**<u>System Architecture:</u>**

User / Attacker → Vulnerable Flask Application (Docker) → Suricata IDS  
↓  
Logstash → Elasticsearch → Kibana Dashboards  
↓  
Incident Response Script → Auto-block malicious IPs  

**<u>Technologies Used:</u>**

- Python  
- Flask  
- Docker  
- Suricata IDS  
- ELK Stack (Elasticsearch, Logstash, Kibana)  
- Nmap  
- Git & GitHub  

**<u>Project Structure:</u>**

```
CraftyRafty/
│
├── app.py
├── database.py
├── craftyratfy.db
├── Dockerfile
├── docker-compose.yml
│
├── templates/
├── suricata/
├── logstash/
│
├── incident_response.py
├── blocked_ips.txt
├── incident_alerts.log
│
├── nmap-report.txt
└── nmap-vuln-report.txt
```
