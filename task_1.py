time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_time = 0

normalized_time = time.replace(' ', ',')
time_list = normalized_time.split(',')

for time in time_list:
    if 'h' in time:
        total_time += int(time[:-1])*60
    elif 's' in time:
        total_time += int(time[:-1])//60
    else:
        total_time += int(time[:-1])

print(total_time)
