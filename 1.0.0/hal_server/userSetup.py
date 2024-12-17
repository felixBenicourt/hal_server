

import socket
import threading
import json
import maya.utils
import os

BACKLOG = 5

print("userSetup.py from C:/Users/felix/OneDrive/Documents/maya/2020/scripts loaded !")

def execute_python_script_from_path(script_path, variables=None):
    try:
        if variables is None:
            variables = {}

        if not os.path.exists(script_path):
            raise FileNotFoundError("Script file not found")

        with open(script_path, 'r') as script_file:
            script_content = script_file.read()

        exec_globals = globals().copy()
        exec_globals.update({'variables': variables})

        def maya_exec():
            try:
                print("Executing code in Maya from script:", script_path)
                print(script_content)
                exec(script_content, exec_globals)
            except Exception as e:
                print("Error executing Python code in Maya:", e)

        maya.utils.executeDeferred(maya_exec)
    except Exception as e:
        print("Error setting up Python code execution:", e)

def start_server(port):
    HOST = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen(BACKLOG)
    print("Waiting for connection on port", port)
    while True:
        conn, addr = s.accept()
        print("Connected by:", addr)
        while True:
            data = conn.recv(4096)
            if not data:
                break
            received_data = data.decode()
            print("Received data:", received_data)

            data_dict = json.loads(received_data)
            print("Loaded json data:", data_dict)
            script_path = data_dict['script']
            variables = data_dict.get('variables', {})

            execute_python_script_from_path(script_path, variables)

        conn.close()

def get_maya_instance_id():
    maya_pid = os.getpid()
    return maya_pid


maya_instance_id = get_maya_instance_id()
port = maya_instance_id
server_thread = threading.Thread(target=start_server, args=(port,))
server_thread.start()


