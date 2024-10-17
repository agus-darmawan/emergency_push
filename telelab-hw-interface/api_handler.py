import requests

class APIHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, nrp, password):
        url = f"{self.base_url}:3333/api/auth/login"
        try:
            response = requests.post(url, json={"nrp": nrp, "password": password})
            if response.status_code == 200:
                return response.json()['data']
            else:
                return None
        except requests.RequestException as e:
            print(f"Error during login: {e}")
            return None

    # Method untuk mengambil input dari API (GET request)
    def get_input(self, module_number, user_id):
        url = f"{self.base_url}:3335/api/input/modul/{module_number}/{user_id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to get input. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error getting input from API: {e}")
            return None

    def send_output(self, module_number, data, user_id):
        url = f"{self.base_url}:3335/api/output/modul/{module_number}"
        try:
            response = requests.post(url, json={"data": data, "user_id": user_id})
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to send output. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending output to API: {e}")
