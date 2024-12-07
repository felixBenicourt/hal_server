import socket
import threading
import json
import maya.utils
import os

BACKLOG = 5

def execute_python_code(script_content, variables=None):
    try:
        if variables is None:
            variables = {}

        exec_globals = globals().copy()
        exec_globals.update({'variables': variables})

        def maya_exec():
            try:
                print("Executing code in Maya:")
                print(script_content)
                exec(script_content, exec_globals)
            except Exception as e:
                print("Error executing Python code in Maya:", e)

        maya.utils.executeDeferred(maya_exec)
    except Exception as e:
        print("Error setting up Python code execution:", e)

def receive_complete_data(conn):
    buffer_size = 4096
    data = b""
    while True:
        part = conn.recv(buffer_size)
        data += part
        if len(part) < buffer_size:
            break
    return data.decode()

def start_server(port):
    HOST = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen(BACKLOG)
    print("Waiting for connection on port", port)
    while True:
        conn, addr = s.accept()
        print("Connected by:", addr)
        try:
            received_data = receive_complete_data(conn)
            print("Received data:", received_data)

            data_dict = json.loads(received_data)
            script_content = data_dict['script']
            variables = data_dict.get('variables', {})

            execute_python_code(script_content, variables)
        except Exception as e:
            print("Error processing connection:", e)
        finally:
            conn.close()

def get_maya_instance_id():
    maya_pid = os.getpid()
    return maya_pid

maya_instance_id = get_maya_instance_id()
port = maya_instance_id
server_thread = threading.Thread(target=start_server, args=(port,))
server_thread.start()
