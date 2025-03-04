import json
import requests

class DBService:
    def __init__(self):
        self.url_domain = 'https://trek.nasa.gov/moon/DSBservice/'

    def get_domain(self):
        return self.url_domain

    def query_by_bbox(self, ul_lon, ul_lat, lr_lon, lr_lat):
        param_str = str(ul_lon) + "," + str(ul_lat) + "," + str(lr_lon) + "," + str(lr_lat)
        endpoint = self.url_domain + "webapi/lroc/CUMINDEX/labels/ptif?bbox=" + param_str
        print("get {}".format(endpoint))
        response = requests.get(endpoint)
        response.raise_for_status()
        return json.loads(response.content.decode('utf-8'))
    
requester = DBService()

#Apollo 12 LM descent stage	Crewed Landing	   19 November 1969   	   3.0128 S, 23.4219 W   	   -3.0128, 336.5781   	d
response = requester.query_by_bbox(336.57, -3.0, 336.58, -3.015)
print(response)