import pandas as pd

with open("dataset/ec2_cpu_utilization_53ea38.csv") as f:
    series = pd.read_csv(f)


incidents = ["2014-02-19 19:10:00", "2014-02-23 20:05:00"]
incident_windows = ["2014-02-19 10:50:00.000000", "2014-02-20 03:30:00.000000"]

series['is_incident'] = series["timestamp"].isin(incidents).astype(int)
print(series)

w_size = 5
window = series[0: w_size]
h_size = 3
prediction = series[w_size: w_size + h_size]
present_incidents = prediction['is_incident'].sum()

for i in range(w_size, len(series) - h_size):
    labels[window] = present_incidents
    
    window.popleft()
    window.append(series[i])
    
    poped = prediction.popleft()
    if poped['is_incident'] == 1:
        present_incidents -= 1
    prediction.append(series[h_size + i])
    if series[h_size + i]['is_incident'] == 1:
        present_incidents += 1