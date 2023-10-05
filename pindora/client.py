import requests
from multipledispatch import dispatch

class Pindora:

    def __init__(self, key) -> None:
        self._secretAPIKey = key
        self._base_url = "https://admin.pindora.fi/api/integration/"

    def get_headers(self)-> dict[str, str]:
        return {"Pindora-Api-Key": self._secretAPIKey, "Accept": "application/json"}

    def list_pindoras(self) -> dict[str, any]:
        """List Pindoras"""
        response = requests.get(self._base_url + "pindoras", headers=self.get_headers())
        return response.json()

    def read_pindora(self, id):
        """Read Pindora"""
        response = requests.get(self._base_url + "pindora/" + id, headers=self.get_headers())
        return response.json()

    def update_pindora(self, id, name, party_mode):
        """Update Pindoras"""
        json = { "name": name, "party_mode": party_mode }
        response = requests.post(self._base_url + "pindora/" + id, json=json, headers=self.get_headers())
        return response.json()

    @dispatch(str, str, str)
    def open_pindora(self, url1, url2, code) -> None:
        """Update Pindoras"""
        url = "https://pindora.fi/" + url1 +"/" + url2 + "/pin"
        return self.open_pindora(url, code)
    
    @dispatch(str, str)
    def open_pindora(self, url, code) -> None:
        """Update Pindoras"""
        json = {"pin": int(code)}
        response = requests.post(url, json=json, headers=self.get_headers())
        return response.json()
        
    def list_pins(self):
        """List pin codes"""
        response = requests.get(self._base_url + "pins", headers=self.get_headers())
        return response.json()
    
    def create_pin(self, code, name):
        """Create Pin"""
        json = { "code": code, "name": name , "validity_rules": []}
        response = requests.post(self._base_url + "pins", json=json , headers=self.get_headers())
        return response.json()

    def update_pin(self, code, name):
        """Update Pin"""
        json = { "name": name , "validity_rules": []}
        response = requests.post(self._base_url + "pin/" + code, json=json, headers=self.get_headers())
        return response.json()

    def delete_pin(self, code):
        """Delete Pin"""
        response = requests.delete(self._base_url + "pin/" + code, headers=self.get_headers())
        if response.status_code == 204:
            return {"status": "OK", "pin_deleted": code}
        return response.json()