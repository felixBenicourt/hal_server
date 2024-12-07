
"""
import socket
import threading
import json
import hou

BACKLOG = 5

def execute_python_code(script_content, variables=None):
    try:
        # Ensure variables is a dictionary
        if variables is None:
            variables = {}

        # Prepare the execution context with the provided variables
        exec_globals = globals().copy()
        exec_globals.update({'variables': variables})  # Update the exec_globals with the 'variables' dictionary

        # Execute the code within Houdini's main thread
        hou.ui.addEventLoopCallback(lambda: exec(script_content, exec_globals))
    except Exception as e:
        print("Error executing Python code in Houdini:", e)

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
            data = conn.recv(4096)  # Increased buffer size
            if not data:
                break
            received_data = data.decode()
            print("Received data:", received_data)

            # Deserialize the data
            data_dict = json.loads(received_data)
            script_content = data_dict['script']
            variables = data_dict.get('variables', {})

            # Execute the script with the provided variables
            execute_python_code(script_content, variables)
        conn.close()

def get_houdini_instance_id():
    # Use a fixed port or dynamically determine one
    return 5000

houdini_instance_id = get_houdini_instance_id()
port = houdini_instance_id
server_thread = threading.Thread(target=start_server, args=(port,))
server_thread.start()
