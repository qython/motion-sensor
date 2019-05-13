import json
from urllib.request import urlopen, urlretrieve
import os

class AndroidConnector():
    def __init__(self, config):
        self.url = config.ip_cam_addr
        self.max_measurements_count = config.max_measurements
        self.tmp_dir = config.tmp_folder_location
        self.tmp_file = config.last_photo_file_name
        self.sensor_data_endpoint = config.sensor_data_endpoint
        self.photo_endpoint = config.photo_endpoint
    
    @property
    def path_to_tmp_file(self):
        return os.path.join(self.tmp_dir, self.tmp_file)

    def __fetch_sensor_data_from_server(self):
        return json.loads(urlopen(os.path.join(self.url, self.sensor_data_endpoint)).read().decode('UTF-8'))

    def download_photo_to_tmp_folder(self):
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

        urlretrieve(os.path.join(self.url, self.photo_endpoint), self.path_to_tmp_file)

    def get_motion_sensor_data(self):
        data = []
        
        response = self.__fetch_sensor_data_from_server()
        elements = response['motion']['data']

        for el in reversed(elements):
            data.append(el[1][0])
            if len(data) >= self.max_measurements_count:
                break
        
        return data
