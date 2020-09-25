
import math
import json
import base64

## Read raw file and convert binary characters to ASCII
raw = open('002-ppb.bin.log').read().split(' ')
text = ''.join([chr(int(b, 2)) for b in raw])

data = json.loads(text)

contaminant_sum_dates = []
contaminant_sum_series = []

for day in data:
    date = day['date']
    for reading in day['readings']:
        id   = reading['id']
        time = reading['time']
        contaminant_sum = 0.
        for contaminant in reading['contaminants']:
            value = reading['contaminants'][contaminant]
            contaminant_sum += value
        contaminant_sum_dates.append([date, time, id])
        contaminant_sum_series.append(contaminant_sum)

mean = sum(contaminant_sum_series) / len(contaminant_sum_series)
stddev = math.sqrt((1./(len(contaminant_sum_series)-1)) * sum([(v-mean)**2 for v in contaminant_sum_series]))

for i in range(len(contaminant_sum_series)):
    if abs(contaminant_sum_series[i] - mean) > stddev:
        print(base64.b16decode(contaminant_sum_dates[i][-1]).decode())


