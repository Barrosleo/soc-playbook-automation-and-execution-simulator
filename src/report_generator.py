import json
from datetime import datetime

def generate_report(incident_log):
    """
    Generates a JSON report from the incident log.
    """
    report = {
        "report_generated": datetime.now().isoformat(),
        "total_alerts": len(incident_log),
        "details": incident_log
    }
    return json.dumps(report, indent=4)

if __name__ == '__main__':
    sample_log = [
        {"alert_id": 1, "action_taken": "isolate account, escalate to security", "notification": "Notification sent for alert 1"},
        {"alert_id": 2, "action_taken": "notify team, log for review", "notification": "No notification required for alert 2"}
    ]
    report = generate_report(sample_log)
    print(report)
