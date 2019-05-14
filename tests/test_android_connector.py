from motionsensor.android_connector import AndroidConnector
from motionsensor.config import load_config
import os

PROPS_FILE = os.path.join(os.path.dirname(__file__), "resources/props.json")
config = load_config(PROPS_FILE)
connector_config = config.get_android_connector_config()

EXPECTED_URL_TO_SENSOR_DATA = "http://192.168.0.13:8080/sensors.json?sense=motion"
EXPECTED_URL_TO_PHOTO = "http://192.168.0.13:8080/shot.jpg"
EXPECTED_TMP_PHOTO_FILE_LOCATION = "tmp/last_photo.jpg"

def test_connector_creation():
    connector = AndroidConnector(connector_config)
    assert connector is not None

def test_urls():
    connector = AndroidConnector(connector_config)
    assert connector.get_url_to_sensor_data() == EXPECTED_URL_TO_SENSOR_DATA
    assert connector.get_url_to_photo() == EXPECTED_URL_TO_PHOTO

def test_path_to_tmp_photo_file():
    connector = AndroidConnector(connector_config)
    assert connector.path_to_tmp_file == EXPECTED_TMP_PHOTO_FILE_LOCATION