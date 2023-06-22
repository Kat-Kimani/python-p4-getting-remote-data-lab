import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        data = json.loads(response_body)
        return data


url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)
json_data = requester.load_json()
print(json_data)  # Print or use the JSON data as needed
