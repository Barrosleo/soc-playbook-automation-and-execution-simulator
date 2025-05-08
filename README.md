# soc playbook automation and execution simulator

this project simulates a soc incident response playbook that automatically executes remediation steps when an alert is detected. it reads sample alert data, triggers predefined actions (like isolating accounts or sending notifications), logs each action, and generates an incident response report.

## key features
- automated playbook execution for incident remediation
- simulated notification system (e.g., slack/email alerts)
- detailed incident logging and reporting

## usage
1. use github codespaces or the online editor to edit and run the project.
2. install dependencies from `requirements.txt`.
3. run the project with: python src/main.py

## repository structure
soc-playbook-automation-and-execution-simulator/
├── README.md
├── requirements.txt
├── docs/
│   └── incident_response_log.json
├── data/
│   └── sample_alerts.csv
└── src/
    ├── main.py
    ├── playbook_engine.py
    ├── notification_system.py
    ├── incident_logger.py
    └── report_generator.py


