import sys
import io
import json
import datetime
import os
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LOG_FILE = "suricata/logs/eve.json"
BLOCKED_IPS_FILE = "blocked_ips.txt"
EVIDENCE_DIR = "evidence"
ALERT_LOG = "incident_alerts.log"
THREAT_THRESHOLD = 5

os.makedirs(EVIDENCE_DIR, exist_ok=True)

def log_alert(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {message}"
    print(full_msg)
    with open(ALERT_LOG, "a", encoding="utf-8") as f:
        f.write(full_msg + "\n")

def block_ip(ip):
    with open(BLOCKED_IPS_FILE, "a", encoding="utf-8") as f:
        f.write(ip + "\n")
    log_alert(f"BLOCKED IP: {ip}")

def store_evidence(ip, events):
    filename = f"{EVIDENCE_DIR}/{ip.replace('.', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)
    log_alert(f"Evidence stored: {filename}")

def load_blocked_ips():
    if not os.path.exists(BLOCKED_IPS_FILE):
        return set()
    with open(BLOCKED_IPS_FILE, encoding="utf-8") as f:
        return set(line.strip() for line in f)

def analyze_logs():
    log_alert("CraftyRafty Incident Response System Started")
    log_alert(f"Analyzing: {LOG_FILE}")

    if not os.path.exists(LOG_FILE):
        log_alert("ERROR: Log file not found!")
        return

    blocked_ips = load_blocked_ips()
    alert_counts = defaultdict(int)
    ip_events = defaultdict(list)
    sql_injection_ips = set()
    port_scan_ips = set()
    brute_force_ips = set()
    total_events = 0
    total_alerts = 0

    with open(LOG_FILE, encoding="utf-8") as f:
        for line in f:
            try:
                event = json.loads(line.strip())
                total_events += 1
                src_ip = event.get("src_ip", "unknown")
                event_type = event.get("event_type", "")

                if event_type == "alert":
                    total_alerts += 1
                    alert_counts[src_ip] += 1
                    ip_events[src_ip].append(event)

                    signature = event.get("alert", {}).get("signature", "")

                    if "SQL" in signature.upper():
                        sql_injection_ips.add(src_ip)
                        log_alert(f"SQL Injection detected from {src_ip}: {signature}")

                    if "Port Scan" in signature:
                        port_scan_ips.add(src_ip)
                        log_alert(f"Port Scan detected from {src_ip}")

                    if "Brute Force" in signature:
                        brute_force_ips.add(src_ip)
                        log_alert(f"Brute Force detected from {src_ip}")

            except json.JSONDecodeError:
                continue

    log_alert(f"Analysis Complete - Total events: {total_events} | Alerts: {total_alerts} | Attacking IPs: {len(alert_counts)}")

    for ip, count in alert_counts.items():
        if count >= THREAT_THRESHOLD and ip not in blocked_ips:
            log_alert(f"THREAT THRESHOLD EXCEEDED for {ip} ({count} alerts)")
            store_evidence(ip, ip_events[ip])
            block_ip(ip)

    log_alert("==================================================")
    log_alert("CRAFTYRAFTY INCIDENT RESPONSE REPORT")
    log_alert("==================================================")
    log_alert(f"SQL Injection IPs:  {sql_injection_ips or 'None detected'}")
    log_alert(f"Port Scan IPs:      {port_scan_ips or 'None detected'}")
    log_alert(f"Brute Force IPs:    {brute_force_ips or 'None detected'}")
    log_alert("==================================================")
    log_alert("Incident Response Complete")

if __name__ == "__main__":
    analyze_logs()