name = "hal_server"
version = "1.0.0"
author = "felix benicourt"

description = ""

build_command = False
requires = ['python-3.10']

def commands():
    env.PYTHONPATH.append(this.root)
    env.PYTHONPATH.append("{root}/hal_server")
    env.PATH.append(this.root)
    env.PATH.append("{root}/hal_server")
    alias("echoInstances", "python {root}/hal_server/echoDccInstances.py")


