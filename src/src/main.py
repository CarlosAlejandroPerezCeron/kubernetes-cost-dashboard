from fetch_kubecost import fetch_kubecost_data
from process_metrics import process_metrics
from export_dashboard import export_dashboard
from utils import log

def main():
    log("=== Kubernetes Cost Breakdown Dashboard ===")

    df = fetch_kubecost_data()
    top = process_metrics(df)
    export_dashboard(top)

    log("Dashboard generation complete.")

if __name__ == "__main__":
    main()
