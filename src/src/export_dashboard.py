import os
import matplotlib.pyplot as plt
from utils import get_env, log

def export_dashboard(df):
    output_dir = get_env("OUTPUT_DIR", "./reports")
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(10,6))
    plt.bar(df["namespace"], df["total_cost"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Kubernetes Cost by Namespace")
    plt.ylabel("Cost (USD)")
    plt.tight_layout()
    chart_path = os.path.join(output_dir, "namespace_costs.png")
    plt.savefig(chart_path)
    log(f"Dashboard chart exported to {chart_path}")
