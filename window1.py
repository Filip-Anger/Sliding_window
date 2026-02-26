import pandas as pd
import numpy as np

with open("dataset/ec2_cpu_utilization_53ea38.csv") as f:
    series = pd.read_csv(f)


incidents = ["2014-02-19 19:10:00", "2014-02-23 20:05:00"]
incident_windows = ["2014-02-19 10:50:00.000000", "2014-02-20 03:30:00.000000"]

series['is_incident'] = series["timestamp"].isin(incidents).astype(int)

w_size = 5
h_size = 3
X = []
y = []
# Pandas magic making lables
series['target'] = series['is_incident'].rolling(window=h_size).sum().shift(-h_size)

for i in range(w_size, len(series) - h_size):
    # 1. Grab the window of 'value' from i-W to i
    window = series['value'].iloc[i-w_size : i].values
    X.append(window)
    
    # 2. Grab the target we calculated for this point
    label = series['target'].iloc[i]
    y.append(label)