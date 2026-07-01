import subprocess


def listen(callback):
    """
    It monitors lid events; whenever an event occurs, we will notify you via
    the callback.
    """

    process = subprocess.Popen(
        ["journalctl", "-f"],
        stdout=subprocess.PIPE,
        text=True,
    )

    for line in process.stdout:
        line = line.strip().lower()

        if "lid closed" in line:
            callback(1)
        elif "lid opened" in line:
            callback(2)
