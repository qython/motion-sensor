#!/usr/bin/python

import json, numpy as np
from urllib.request import urlopen
from decimal import Decimal
from time import sleep
dane_obrobione = []

class MotionSensor(object):

    def __init__(self, ipwebcam_address, ile_ostatnich_pomiarow, how_many_tries, interval, treshold_weight, drift_weight, min_final_move, max_final_move):
        self.__ipwebcam_address = ipwebcam_address
        self.__ile_ostatnich_pomiarow =ile_ostatnich_pomiarow
        self.__how_many_tries=how_many_tries
        self.__interval=interval
        self.__treshold_weight=treshold_weight
        self.__drift_weight=drift_weight
        self.__min_final_move=min_final_move
        self.__max_final_move=max_final_move
        self.__ile_danych_obrobionych=0
        self.__dane_obrobione=[]

    def read_from_url(self):
        for y in range(0, self.__how_many_tries):
            request_url="http://" + self.__ipwebcam_address + ":8080/sensors.json?sense=motion"
            json_data=urlopen(request_url).read().decode('UTF-8')
            print(json_data)
            data = json.loads(json_data)
            number_of_elements = len(data[u'motion'][u'data'])
            print("Number of elements", number_of_elements)
            print("Ile pomiarow", (number_of_elements - self.__ile_ostatnich_pomiarow))
            for x in range(number_of_elements - self.__ile_ostatnich_pomiarow, number_of_elements):
                self.__dane_obrobione.append(float(str(data[u'motion'][u'data'][x][1]).replace('[', '').replace(']', '')))
            #  print(data[u'motion'][u'data'][x][1]) #wyswietlanie danych pomiarowych

            sleep(self.__interval)
        self.__ile_danych_obrobionych = int(len(self.__dane_obrobione))

    def counting_average(self):
        srednia = np.mean(self.__dane_obrobione)
        return srednia

    def counting_drift(self):
        diff = 0
        for licznik in range(1, self.__ile_danych_obrobionych // 2):
            diff = diff + abs(
				self.__dane_obrobione[self.__ile_danych_obrobionych - licznik] - self.__dane_obrobione[0 + licznik])
        diff = abs(diff) / self.__ile_danych_obrobionych
        if (diff == 0): diff = 0.1
        return diff

    def summary(self):
        summary = (self.counting_average() * self.__treshold_weight + self.counting_drift() * self.__drift_weight) / self.__treshold_weight + self.__drift_weight
        return summary

    def motion_detect(self):
        summary=self.summary()

        if ((summary > self.__min_final_move) and (summary < self.__max_final_move)):
            print("Motion detected: 1")
        else:
            print("Motion detected: 0")

ms = MotionSensor("192.168.0.221",40,3,1,1,10,1200,3000)
ms.read_from_url()
ms.motion_detect()
