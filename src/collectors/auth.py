import subprocess


def listen(callback):
    """Monitor for invalid authentication attempts."""
    process = subprocess.Popen(["journalctl", "-f"], stdout=subprocess.PIPE, text=True)

    for line in process.stdout:
        if "authentication failure" in line:
            callback(5)
