print("*****************BEGIN*****************")
Topology = 'mesh88_lat'
injection_rate_list = [0.0050,0.0069,0.0088,0.0107,0.0126,0.0144,0.0163,0.0182,0.0201,0.0220]
routing_func_list = ['dor', 'valiant', 'romm', 'min_adapt']
print('-----initializing finished-----')
progress = 0
print(f'\r-----current progress {progress}%-----', end="")
store_file = '%s_res' % Topology
data_file = open(store_file, 'w')

for routing_func in routing_func_list:
    data_file.writelines(['----------', routing_func, '----------', '\n'])

    for injection_rate in injection_rate_list:
        data_file.writelines(['\n*************overall results************\n', 'injection_rate = %s\n' % injection_rate])
        injection_rate = int(injection_rate * 10000)
        file_name = '%s_%s_%s' % (Topology,routing_func,injection_rate)
        with open(file_name, 'r') as file:
            contents = file.readlines()
            # configuration = contents[24:29]
            # configuration.append('\n')
            # data_file.writelines(configuration)
            if '====== Overall Traffic Statistics ======\n' in contents: 
                result_start = contents.index('====== Overall Traffic Statistics ======\n')
            else:
                continue
            contents = contents[result_start:]
            average_packet_latency = contents[2]
            average_network_latency = contents[5]
            average_flit_latency = contents[8]
            hop_average = contents[28]
            total_runtime = contents[29]
            data_file.writelines(['// Statistic Results\n',average_packet_latency,average_network_latency,average_flit_latency,hop_average,total_runtime])
        file.close()
        progress += 2.5
        print(f'\r-----current progress {progress}%-----', end="")
    data_file.writelines(['\n'])
data_file.writelines(['\n\n'])
data_file.close()
print("\n*****************FINISH****************")