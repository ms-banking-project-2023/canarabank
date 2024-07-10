def update_server_file(file_name,key,value):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    with open(file_name, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else: 
                file.write(line)
server_config_file_name = 'server.conf'
updated_key = 'TIMEOUT'
updated_value = '30'
update_server_file(server_config_file_name,updated_key,updated_value)
