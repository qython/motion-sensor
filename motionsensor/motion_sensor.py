from decimal import Decimal
from time import sleep
import numpy as np

class MotionSensor(object):

    def __init__(self, config, android_connector):
        self.__tries_count = config.tries
        self.__interval = config.interval
        self.__treshold_weight = config.treshold_weight
        self.__drift_weight = config.drift_weight
        self.__move_min = config.move_min
        self.__move_max = config.move_max
        self.__android_connector = android_connector

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
        data = []

        for _ in range(self.__tries_count):
            data.extend(self.__android_connector.get_motion_sensor_data())
            sleep(self.__interval)

        summary = self.count_summary(data)

        print(summary)

        return self.is_motion_detected(summary)