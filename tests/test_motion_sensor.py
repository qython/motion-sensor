import os
from motionsensor.motion_sensor import MotionSensor

EXPECTED_URL_ENDPOINT = "/sensors.json?sense=motion"
IP_CAM_ADDRESS = "http://192.168.0.13:8080"

MOVE_MIN = 1000
MOVE_MAX = 3000

DATA_FROM_SERVER = [4.0, 3.2, 6.4, 3.5, 7.3, 2.5, 4.2]
EXPECTED_DRIFT = 0.7
EXPECTED_SUMMARY = 21.44

SUMMARY_BELOW_MINIMUM = 300
SUMMARY_ABOVE_MAXIMUM = 3400
SUMMARY_IN_RANGE = 1400

motion_sensor = MotionSensor(ip_cam_addr=IP_CAM_ADDRESS, max_measurements_count=40, tries_count=3, interval=1, treshold_weight=1, drift_weight=10, move_min=MOVE_MIN, move_max=MOVE_MAX)

def test_get_url():
    assert motion_sensor.get_url_to_sensor_data() == (IP_CAM_ADDRESS + EXPECTED_URL_ENDPOINT)

def test_count_drift():
    res = motion_sensor.count_drift(DATA_FROM_SERVER)
    assert res == EXPECTED_DRIFT

def test_count_summary():
    res = motion_sensor.count_summary(DATA_FROM_SERVER)
    assert res == EXPECTED_SUMMARY

def test_is_motion_detected():
    assert False == motion_sensor.is_motion_detected(SUMMARY_ABOVE_MAXIMUM)
    assert False == motion_sensor.is_motion_detected(SUMMARY_BELOW_MINIMUM)
    assert True == motion_sensor.is_motion_detected(SUMMARY_IN_RANGE)
