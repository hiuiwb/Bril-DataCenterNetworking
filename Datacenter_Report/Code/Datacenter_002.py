import os

print("*****************SIMULATION BEGIN*****************")
Topology = 'torus88_lat'
injection_rate_list = [0.0050,0.0069,0.0088,0.0107,0.0126,0.0144,0.0163,0.0182,0.0201,0.0220]
routing_func_list = ['dim_order', 'valiant', 'min_adapt']
print('-----initializing finished-----')
progress = 0
print(f'current progress {progress}%', end="")
for routing_func in routing_func_list:
    with open('projects/torus88_lat','r') as file:
        config = file.readlines()
    file.close()
    config[9]='routing_function = %s;\n' % routing_func
    with open('projects/torus88_lat', 'w') as file:
        file.writelines(config)
    file.close()

    for injection_rate in injection_rate_list:
        with open('projects/torus88_lat','r') as file:
            config = file.readlines()
        file.close()
        # config[10]='routing_function = %s;\n' % routing_func
        config.pop()
        
        add_injection_rate = 'injection_rate = %s;\n' % injection_rate
        config.append(add_injection_rate)

        with open('projects/torus88_lat', 'w') as file:
            file.writelines(config)
        file.close()
        injection_rate = int(injection_rate * 10000)
        command = './booksim projects/%s >projects/results/torus88_lat_dir/%s_%s_%s' % (Topology,Topology,routing_func,injection_rate)
        os.system(command)
        progress += round(float(3+(1/3)),2)
        print(f'\r-----current progress {progress}%-----', end="")
print("\n*****************SIMULATION FINISH****************")