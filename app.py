import sys
import os
import requests
import yaml


def get_api_key():
    # Read YAML file
    with open("config.yaml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded['apikey']['macaddress']


def run(mac_address):
    """
    mac_address: accept value from command line arg, if not present will ask you to enter value
    and return company name related to mac address
    """
    api_key = get_api_key()

    url = f"https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac_address}"

    resp = requests.get(url)
    json_resp = resp.json()

    if 'error' in json_resp:
        print("Error while executing operation...", json_resp)
        return json_resp
    else:
        company_name = json_resp["vendorDetails"]["companyName"]
        print(company_name)
        return company_name


if __name__ == "__main__":
    if len(sys.argv) == 2:
        mac_address = sys.argv[1]
    else:
        print("Provide Mac Address. E.g. 44:38:39:ff:ef:57")
        return
    run(mac_address)

