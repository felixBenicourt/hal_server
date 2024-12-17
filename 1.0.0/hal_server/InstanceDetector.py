# -*- encoding: utf-8 -*-
"""
Module with functions to detect instances of various DCC (Digital Content Creation) software.
"""

import subprocess

houdiniExe = "houdini.exe"
mayaExe = "maya.exe"
unrealExe = "UnrealEditor.exe"
blenderExe = "blender.exe"


class DCCInstanceDetector:
    """
    A class responsible for detecting instances of DCC software (Maya, Houdini, Unreal, Blender) 
    running on the system.

    Attributes:
        maya_instances (list): List of running Maya instances.
        houdini_instances (list): List of running Houdini instances.
        unreal_instances (list): List of running Unreal instances.
        blender_instances (list): List of running Blender instances.
    """
    _maya_instances = []
    _houdini_instances = []
    _unreal_instances = []
    _blender_instances = []

    @classmethod
    def detect_maya_instances(cls):
        """
        Detect and update the list of running Maya instances.

        Uses `list_running_instances` to find all currently running Maya processes.
        """
        cls._maya_instances = cls.list_running_instances(mayaExe)

    @classmethod
    def detect_houdini_instances(cls):
        """
        Detect and update the list of running Houdini instances.

        Uses `list_running_instances` to find all currently running Houdini processes.
        """
        cls._houdini_instances = cls.list_running_instances(houdiniExe)

    @classmethod
    def detect_unreal_instances(cls):
        """
        Detect and update the list of running Unreal Engine instances.

        Uses `list_running_instances` to find all currently running Unreal Engine processes.
        """
        cls._unreal_instances = cls.list_running_instances(unrealExe)

    @classmethod
    def detect_blender_instances(cls):
        """
        Detect and update the list of running Blender instances.

        Uses `list_running_instances` to find all currently running Blender processes.
        """
        cls._blender_instances = cls.list_running_instances(blenderExe)

    @classmethod
    def list_running_instances(cls, process_name):
        """
        List running instances of a specific process by its name.

        Args:
            process_name (str): The name of the process to search for (e.g., 'maya.exe').

        Returns:
            list: A list of tuples containing process IDs and names of running instances.
        """
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
        """
        Property that returns the list of running Maya instances.

        Returns:
            list: List of running Maya instances.
        """
        return DCCInstanceDetector._maya_instances

    @property
    def houdini_instances(self):
        """
        Property that returns the list of running Houdini instances.

        Returns:
            list: List of running Houdini instances.
        """
        return DCCInstanceDetector._houdini_instances

    @property
    def unreal_instances(self):
        """
        Property that returns the list of running Unreal Engine instances.

        Returns:
            list: List of running Unreal Engine instances.
        """
        return DCCInstanceDetector._unreal_instances

    @property
    def blender_instances(self):
        """
        Property that returns the list of running Blender instances.

        Returns:
            list: List of running Blender instances.
        """
        return DCCInstanceDetector._blender_instances
