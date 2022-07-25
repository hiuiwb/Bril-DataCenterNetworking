import os

print("*****************SIMULATION BEGIN*****************")
Topology = 'mesh88_lat'
injection_rate_list = [0.0050,0.0069,0.0088,0.0107,0.0126,0.0144,0.0163,0.0182,0.0201,0.0220]
routing_func_list = ['dor', 'valiant', 'romm', 'min_adapt']
print('-----initializing finished-----')
progress = 0
print(f'current progress {progress}%', end="")
for routing_func in routing_func_list:
    with open('projects/mesh88_lat','r') as file:
        config = file.readlines()
    file.close()
    config[10]='routing_function = %s;\n' % routing_func
    with open('projects/mesh88_lat', 'w') as file:
        file.writelines(config)
    file.close()

    for injection_rate in injection_rate_list:
        with open('projects/mesh88_lat','r') as file:
            config = file.readlines()
        file.close()
        # config[10]='routing_function = %s;\n' % routing_func
        config.pop()
        
        add_injection_rate = 'injection_rate = %s;\n' % injection_rate
        config.append(add_injection_rate)

        with open('projects/mesh88_lat', 'w') as file:
            file.writelines(config)
        file.close()
        injection_rate = int(injection_rate * 10000)
        command = './booksim projects/%s >projects/results/mesh88_lat_dir/%s_%s_%s' % (Topology,Topology,routing_func,injection_rate)
        os.system(command)
        progress += 2.5
        print(f'\r-----current progress {progress}%-----', end="")
print("\n*****************SIMULATION FINISH****************")