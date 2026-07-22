from threading import Thread
from datetime import datetime
from event_type import EVENT_TYPE
from collectors import lid, power, session, auth
import cv2
import os


def create_folders():
    if not os.path.exists("photos"):
        os.mkdir("photos")


def take_photo(filename: str):
    """
    Captures a frame from the camera.
    """
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Não foi possivel acessar a camera")
        return

    ret, frame = camera.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Foto salva em: {filename}")
    camera.release()


def take_photo_safe(filename: str):
    """
    If an error occurs during photo capture, it suppresses the error.
    """
    try:
        take_photo(filename)
    except Exception as e:
        return


def event_callback(event_type: int):
    """This callback is called whenever an event occurs."""

    create_folders()
    event_name = EVENT_TYPE[event_type]
    event_now = datetime.now()
    filename = event_now.strftime(f"photos/photo_{event_type}_%d-%m-%Y_%H:%M:%S.jpg")
    take_photo_safe(filename)
    with open("logs.txt", "a") as file:
        file.write(f"[{event_name}] - {event_now} - {filename}\n".upper())


def main():
    Thread(target=lid.listen, args=(event_callback,), daemon=True).start()
    Thread(target=power.listen, args=(event_callback,), daemon=True).start()
    Thread(target=session.listen, args=(event_callback,), daemon=True).start()
    Thread(target=auth.listen, args=(event_callback,), daemon=True).start()

    while 1:
        ...


if __name__ == "__main__":
    main()
