import pandas as pd

data = pd.read_csv('Flows.csv')

shape = data.shape

rows = shape[0]
columns = shape[1]


src_ip_addresses = data['src_ip']
dst_ip_addresses = data['dst_ip']
flow_durations = data['flowDuration']
flow_sizes = data['octetTotalCount']

src_dict = {}
dst_dict = {}

for i in range(rows):
    src_ip = src_ip_addresses[i]
    dst_ip = dst_ip_addresses[i]

    if src_ip in src_dict:
        src_dict[src_ip] += 1
    else:
        src_dict[src_ip] = 1

    if dst_ip in dst_dict:
        dst_dict[dst_ip] += 1
    else:
        dst_dict[dst_ip] = 1

sorted_src_keys = sorted(src_dict, key=lambda x: src_dict[x], reverse=True)
sorted_dst_keys = sorted(dst_dict, key=lambda x: dst_dict[x], reverse=True)


max_duration = flow_durations.max()
max_duration_index = flow_durations.idxmax()
max_duration_src = src_ip_addresses[max_duration_index]
max_duration_dst = dst_ip_addresses[max_duration_index]

max_size = flow_sizes.max()
max_size_index = flow_sizes.idxmax()
max_size_src = src_ip_addresses[max_size_index]
max_size_dst = dst_ip_addresses[max_size_index]

print("".join(['Number of records: ', str(rows), '\n\nNumber of fields: ', str(columns), '\n']))

print('Source IPs with most records')
for key in sorted_src_keys[:10]:
    print(key, ': ', src_dict[key])

print('\nDestination IPs with most records')
for key in sorted_dst_keys[:10]:
    print(key, ': ', dst_dict[key])

print("".join(['\nLongest duration flow:\n', max_duration_src, ' to ', max_duration_dst, ': ', str(max_duration), ' seconds\n'])) 

print("".join(['Largest flow:\n', max_size_src, ' to ', max_size_dst, ': ', str(max_size), ' bytes'])) 
