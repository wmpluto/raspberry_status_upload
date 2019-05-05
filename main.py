#!/usr/bin/python3

import os, sys, requests

def get_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temp = float(file.read()) / 1000
    return temp

def set_data(token, series, value):
    url = f"https://iot.espressif.cn/v1/datastreams/{series}/datapoint/"
    r = requests.post(url,
        data = '{"datapoint":{"x":%0.2f}}' % (value),
        headers = {
            "Authorization": f"token {token}"
        }
    )

def main():
    cwd = sys.path[0]
    token_path = os.path.join(cwd, 'token')
    with open(token_path, "r") as file:
        token = file.readline().strip()
    set_data(token, 'Temperature', get_temp())
    set_data(token, 'Network', 1)

if __name__ == '__main__':
    main()