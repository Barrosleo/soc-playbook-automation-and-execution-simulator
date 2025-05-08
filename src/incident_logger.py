def log_incident(responses, notifications):
    """
    Combine response actions and notifications into a single incident log.
    """
    log_entries = []
    for res, note in zip(responses, notifications):
        entry = {
            "alert_id": res['alert_id'],
            "action_taken": res['action'],
            "notification": note
        }
        log_entries.append(entry)
    return log_entries

if __name__ == '__main__':
    sample_responses = [
        {'alert_id': 1, 'action': "isolate account, escalate to security"},
        {'alert_id': 2, 'action': "notify team, log for review"}
    ]
    sample_notifications = [
        "Notification sent for alert 1",
        "No notification required for alert 2"
    ]
    log = log_incident(sample_responses, sample_notifications)
    print(log)
