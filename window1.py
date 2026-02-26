import pandas as pd

with open("dataset/ec2_cpu_utilization_53ea38.csv") as f:
    series = pd.read_csv(f)

print(series)