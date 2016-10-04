import json

class FilterModule:

    def filters(self):
        return {
            'influxdb_tag': self.influxdb_tag,
        }

    def influxdb_tag(self, raw_data):
        """This filter extracts the tag values from a request.
        Example request: SHOW TAG VALUES WITH KEY = "host"
        """
        json_data = json.loads(raw_data)
        return [x[1] for x in json_data['results'][0]['series'][0]['values']]
