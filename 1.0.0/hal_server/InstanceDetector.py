# -*- encoding: utf-8 -*-
"""
Module with detect instances functions
"""


import subprocess

houdiniExe = "houdini.exe"
mayaExe = "maya.exe"
unrealExe = "UnrealEditor.exe"
blenderExe = "blender.exe"


class DCCInstanceDetector:
    _maya_instances = []
    _houdini_instances = []
    _unreal_instances = []
    _blender_instances = []

    @classmethod
    def detect_maya_instances(cls):
        cls._maya_instances = cls.list_running_instances(mayaExe)

    @classmethod
    def detect_houdini_instances(cls):
        cls._houdini_instances = cls.list_running_instances(houdiniExe)

    @classmethod
    def detect_unreal_instances(cls):
        cls._unreal_instances = cls.list_running_instances(unrealExe)

    @classmethod
    def detect_blender_instances(cls):
        cls._blender_instances = cls.list_running_instances(blenderExe)

    @classmethod
    def list_running_instances(cls, process_name):
        instances = []
        try:
            result = subprocess.check_output(['tasklist'], text=True)
            lines = result.split('\n')
            for line in lines:
                if process_name.lower() in line.lower():
                    parts = line.split()
                    if len(parts) >= 2:
                        process_id, process_name = int(parts[1]), parts[0]
                        instances.append((process_id, process_name))
        except subprocess.CalledProcessError:
            pass
        return instances

    @property
    def maya_instances(self):
        return DCCInstanceDetector._maya_instances

    @property
    def houdini_instances(self):
        return DCCInstanceDetector._houdini_instances

    @property
    def unreal_instances(self):
        return DCCInstanceDetector._unreal_instances

    @property
    def blender_instances(self):
        return DCCInstanceDetector._blender_instances



