import requests
import pandas as pd
from utils import get_env, log

def fetch_kubecost_data():
    url = get_env("KUBECOST_API")
    time_window = get_env("TIME_WINDOW", "7d")
    params = {"window": time_window, "aggregate": "namespace"}

    log(f"Fetching Kubecost data for {time_window}...")
    response = requests.get(url, params=params)
    data = response.json()["data"]

    records = []
    for ns, values in data.items():
        records.append({
            "namespace": ns,
            "cpu_cost": values.get("cpuCost", 0),
            "ram_cost": values.get("ramCost", 0),
            "pv_cost": values.get("pvCost", 0),
            "total_cost": values.get("totalCost", 0)
        })

    df = pd.DataFrame(records)
    log(f"Fetched {len(df)} namespace cost records.")
    return df
