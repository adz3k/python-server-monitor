def get_status_label(status):
    if status == 'running':
        return 'Healthy'
    elif status == 'stopped':
        return 'Down'
    elif status == 'maintenance':
        return 'Unknown'
    else:
        return 'Unknown'
