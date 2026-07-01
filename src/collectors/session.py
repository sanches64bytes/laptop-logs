from time import sleep
import subprocess


def get_locked() -> bool:
    """Checks if the screen is locked."""
    result = subprocess.run(
        ["loginctl", "show-session", "2", "-p", "LockedHint", "--value"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip() == "yes"


def listen(callback):
    """
    It monitors session events; whenever an event occurs, we will notify you
    via the callback.
    """
    
    is_locked = get_locked()

    while True:
        current = get_locked()
        if current ^ is_locked:
            is_locked = current
            callback(3 if is_locked else 4)
        sleep(.5)