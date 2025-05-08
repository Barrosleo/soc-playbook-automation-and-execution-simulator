def execute_playbook(alerts_df):
    """
    Simulates execution of a SOC playbook for each alert.
    For each alert, it creates a response action.
    """
    responses = []
    for index, alert in alerts_df.iterrows():
        action = {}
        action['alert_id'] = alert['alert_id']
        # simulate action based on severity
        if alert['severity'] == "high":
            action['action'] = "isolate account, escalate to security"
        elif alert['severity'] == "medium":
            action['action'] = "notify team, log for review"
        else:
            action['action'] = "log as informational"
        responses.append(action)
    return responses

if __name__ == '__main__':
    import pandas as pd
    data = {'alert_id': [1,2,3], 'severity': ['high','medium','low']}
    alerts_df = pd.DataFrame(data)
    actions = execute_playbook(alerts_df)
    print(actions)
