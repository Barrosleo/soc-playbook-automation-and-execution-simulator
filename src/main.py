from playbook_engine import execute_playbook
from notification_system import send_notifications
from incident_logger import log_incident
from report_generator import generate_report
import pandas as pd
import os

def main():
    # ensure necessary directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)

    # load sample alert data
    alerts = pd.read_csv("data/sample_alerts.csv")
    print("Loaded alerts:", len(alerts), "records.")

    # execute playbook on each alert and collect response actions
    responses = execute_playbook(alerts)
    print("Playbook execution complete.")

    # send notifications for high-severity incidents
    notifications = send_notifications(responses)
    print("Notifications sent:", notifications)

    # log the incident response actions
    log = log_incident(responses, notifications)
    print("Incident log created.")

    # generate incident report and save to docs folder
    report = generate_report(log)
    with open("docs/incident_response_log.json", "w") as f:
        f.write(report)
    print("Incident report generated at docs/incident_response_log.json")

if __name__ == '__main__':
    main()
