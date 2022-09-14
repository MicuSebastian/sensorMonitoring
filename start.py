import requests
import serial
import time

port = "/dev/ttyACM0"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "microbit"
VARIABLE_LABEL_1 = "temperature"
VARIABLE_LABEL_2 = "light"
VARIABLE_LABEL_3 = "sound"
TOKEN = "BBFF-RPBvqi1TiphOUZVU9XdrJyhKxYY1Mh"
DELAY = 1


def post_var(payload, url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}".format(url, device)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Sending data, attempt number: {}".format(attempts))
            req = requests.post(url=url, headers=headers,
                                json=payload)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        print("[INFO] Results:")
        print(req.text)
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))


def main():
    data = s.readline()
    data = int(data)
    data2 = s.readline()
    data2 = int(data2)
    data3 = s.readline()
    data3 = int(data3)

    payload = {VARIABLE_LABEL_1: data,
               VARIABLE_LABEL_2: data2,
	       VARIABLE_LABEL_3: data3
              }

    post_var(payload)


if __name__ == "__main__":
    while True:
        main()
        #time.sleep(DELAY)