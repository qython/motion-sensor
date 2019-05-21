import os
from motionsensor.motion_sensor import MotionSensor
from motionsensor.android_connector import AndroidConnector
from motionsensor.config import load_config

PROPS_FILE = os.path.join(os.path.dirname(__file__), os.path.normpath("resources/props.json"))

DATA_FROM_SERVER = [4.0, 3.2, 6.4, 3.5, 7.3, 2.5, 4.2]
EXPECTED_DRIFT = 0.7
EXPECTED_SUMMARY = 21.44

SUMMARY_BELOW_MINIMUM = 300
SUMMARY_ABOVE_MAXIMUM = 3400
SUMMARY_IN_RANGE = 1400

config = load_config(PROPS_FILE)
android_connector = AndroidConnector(config.get_android_connector_config())
motion_sensor = MotionSensor(config.get_motion_config(), android_connector)

def test_count_drift():
    res = motion_sensor.count_drift(DATA_FROM_SERVER)
    assert res == EXPECTED_DRIFT

def test_count_summary():
    res = motion_sensor.count_summary(DATA_FROM_SERVER)
    assert res == EXPECTED_SUMMARY

def test_is_motion_detected():
    assert motion_sensor.is_motion_detected(SUMMARY_ABOVE_MAXIMUM) == False
    assert motion_sensor.is_motion_detected(SUMMARY_BELOW_MINIMUM) == False
    assert motion_sensor.is_motion_detected(SUMMARY_IN_RANGE) == True
