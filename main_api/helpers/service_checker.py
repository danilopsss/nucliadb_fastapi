import os


def evaluate_service_health(*args) -> bool:
    services_statuses = [os.system(f"ping -c 1 {service}") for service in args]
    return len(set(services_statuses)) == 1
