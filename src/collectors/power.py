import subprocess


def listen(callback):
    """
    It monitors energy events; whenever an event occurs, we will notify you
    via the callback.
    """

    process = subprocess.Popen(["journalctl", "-f"], stdout=subprocess.PIPE, text=True)

    for line in process.stdout:
        line = line.strip()

        if "suspend entry" in line:
            callback(6)
        elif "resume" in line:
            callback(7)
