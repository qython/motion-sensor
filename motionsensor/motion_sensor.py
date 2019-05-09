#!/usr/bin/python

import json, numpy as np
from urllib.request import urlopen
from decimal import Decimal
from time import sleep

class MotionSensor(object):

    def __init__(self, ip_cam_addr, max_measurements_count, tries_count, interval, treshold_weight, drift_weight, move_min, move_max):
        self.__ip_cam_addr = ip_cam_addr
        self.__max_measurements_count = max_measurements_count
        self.__tries_count = tries_count
        self.__interval = interval
        self.__treshold_weight = treshold_weight
        self.__drift_weight = drift_weight
        self.__move_min = move_min
        self.__move_max = move_max

    def get_url_to_sensor_data(self) :
        return self.__ip_cam_addr + "/sensors.json?sense=motion"

    def get_response(self, url):
        return json.loads(urlopen(url).read().decode('UTF-8'))

    def get_motion_sensor_data(self, url):
        data = []
        
        response = self.get_response(url)
        elements = response['motion']['data']

        for el in reversed(elements):
            data.append(el[1][0])
            if len(data) >= self.__max_measurements_count:
                break
        
        return data

    def count_drift(self, data):
        diff = 0
        for counter in range(1, len(data) // 2):
            diff = diff + abs(data[len(data) - counter] - data[0 + counter])
        diff = abs(diff) / len(data)
        return round(diff, 2)

    def count_summary(self, data):
        summary = (np.mean(data) * self.__treshold_weight + self.count_drift(data) * self.__drift_weight) / self.__treshold_weight + self.__drift_weight
        return round(summary, 2)

    def is_motion_detected(self, summary):
        return (summary > self.__move_min) and (summary < self.__move_max)

    def detect(self):
        url = self.get_url_to_sensor_data()
        data = []

        for _ in range(self.__tries_count):
            data.extend(self.get_motion_sensor_data(url))
            sleep(self.__interval)

        summary = self.count_summary(data)

        print(summary)

        return self.is_motion_detected(summary)