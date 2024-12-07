

from InstanceDetector import DCCInstanceDetector

detector = DCCInstanceDetector()

# Detect instances for each DCC tool
detector.detect_maya_instances()
detector.detect_houdini_instances()
detector.detect_unreal_instances()
detector.detect_blender_instances()

# Print Maya instances
print("Maya Instances:")
for pid, name in detector.maya_instances:
    print(f"PID: {pid}, Name: {name}")

# Print Houdini instances
print("\nHoudini Instances:")
for pid, name in detector.houdini_instances:
    print(f"PID: {pid}, Name: {name}")

# Print Unreal instances
print("\nUnreal Instances:")
for pid, name in detector.unreal_instances:
    print(f"PID: {pid}, Name: {name}")

# Print Blender instances
print("\nBlender Instances:")
for pid, name in detector.blender_instances:
    print(f"PID: {pid}, Name: {name}")