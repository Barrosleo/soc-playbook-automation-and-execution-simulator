def send_notifications(responses):
    """
    Simulate sending notifications.
    Returns a list of notifications that were 'sent'.
    """
    notifications = []
    for response in responses:
        # simulate sending a notification for high severity alerts
        if "high" in response.get('action', ''):
            notifications.append(f"Notification sent for alert {response['alert_id']}")
        else:
            notifications.append(f"No notification required for alert {response['alert_id']}")
    return notifications

if __name__ == '__main__':
    sample_responses = [
        {'alert_id': 1, 'action': "isolate account, escalate to security"},
        {'alert_id': 2, 'action': "notify team, log for review"}
    ]
    notes = send_notifications(sample_responses)
    print(notes)
