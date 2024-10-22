import os

import requests

def list_clusters():
    workspace_url = os.environ['INPUT_WORKSPACE_URL']
    databricks_token = os.environ['INPUT_DATABRICKS_TOKEN']
    
    headers = {"Authorization": f"Bearer {databricks_token}"}

    cluster_list_endpoint = f"{workspace_url}/api/2.1/clusters/list"

    response = requests.get(cluster_list_endpoint, headers=headers)

    if response.status_code == 200:
        cluster_list = response.json()
        print(cluster_list)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    list_clusters()