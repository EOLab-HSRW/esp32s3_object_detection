import cv2
import requests
from pathlib import Path # handle better relative paths
import time
from loguru import logger
URL = "http://192.168.2.230"


def test_connection():
    try:
        requests.get(URL + "/status", timeout=10)
        return True
    except:
        return False

def set_resolution(selected_resolution):
    try:
        """
        Available resolutions:
        10: UXGA(1600x1200)
        9: SXGA(1280x1024)
        8: XGA(1024x768)
        7: SVGA(800x600)
        6: VGA(640x480)
        5: CIF(400x296)
        4: QVGA(320x240)
        3: HQVGA(240x176)
        0: QQVGA(160x120)
        """

        if selected_resolution in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(URL + "/control?var=framesize&val={}".format(selected_resolution))
        else:
            logger.debug("Not available index")
    except:
        logger.debug("SET_RESOLUTION: something went wrong")

def showWindow():
    if __name__ == '__main__':
        cv2.namedWindow("frame", cv2.WINDOW_AUTOSIZE)
        while True:
            if cap.isOpened():
                ret, frame = cap.read()

                cv2.imshow("frame", frame)

                key = cv2.waitKey(1)

                for i in range(9):
                    if key == ord(str(i)):
                        save_path = images_path / str(i)
                        cv2.imwrite('{}/{}-{}.jpg'.format(save_path.resolve(), i, time.time() * 1000), frame)
                        logger.debug("saved picture of class: {}".format(i))

                if key == ord('q'):
                    break

        cv2.destroyAllWindows()
        cap.release()

logger.debug("Starting EZ Images.")
logger.debug("Testing Connection.")
if test_connection():
    logger.debug("Connection successful.")
    cap = cv2.VideoCapture(URL + ":81/stream")
    images_path = Path("../data/raw/images")
    if not images_path.resolve().exists():
        images_path.resolve().mkdir(parents=True)
    set_resolution(4)
    showWindow()
else:
    logger.debug("Connection not successful. Aborting.")