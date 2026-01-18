import pandas as pd
from utils import log

def process_metrics(df):
    df["cpu_share"] = (df["cpu_cost"] / df["total_cost"] * 100).round(2)
    df["ram_share"] = (df["ram_cost"] / df["total_cost"] * 100).round(2)

    top_namespaces = df.sort_values("total_cost", ascending=False).head(10)
    log("Processed cost breakdown and top 10 namespaces.")
    return top_namespaces
