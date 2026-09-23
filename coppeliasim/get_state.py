import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class CoppeliaState:
    def __init__(self):
        self.client = RemoteAPIClient()
        self.sim = self.client.require("sim")
        self.robot = self.sim.getObject("/UR5")
        self.ignore_names = {
            "/Floor",
            "/Camera",
            "/Light"
        }

    def get_state(self):
        robot_position = self.sim.getObjectPosition(self.robot, -1)
        robot_orientation = self.sim.getObjectOrientation(self.robot, -1)
        joints = []
        index = 0
        while True:
            handle = self.sim.getObjects(index,self.sim.handle_all)
            if handle == -1:
                break
            index += 1
            parent = self.sim.getObjectParent(handle)
            if self.sim.getObjectType(handle) == self.sim.sceneobject_joint:
                if self.is_robot_child(handle):
                    joints.append(self.sim.getJointPosition(handle))
        objects = []
        index = 0
        while True:
            handle = self.sim.getObjects(index, self.sim.handle_all)
            if handle == -1:
                break
            index += 1
            name = self.sim.getObjectAlias(handle, 2)
            if name in self.ignore_names:
                continue
            if handle == self.robot:
                continue
            if self.is_robot_child(handle):
                continue
            object_type = self.sim.getObjectType(handle)
            if object_type != self.sim.sceneobject_shape:
                continue
            position = self.sim.getObjectPosition(handle, -1)
            orientation = self.sim.getObjectOrientation(handle, -1)
            objects.append({
                "name": name,
                "position": position,
                "orientation": orientation
            })
        return {
            "robot": {
                "position": robot_position,
                "orientation": robot_orientation,
                "joints": joints
            },
            "objects": objects
        }

    def is_robot_child(self, handle):
        current = handle
        while True:
            parent = self.sim.getObjectParent(current)
            if parent == -1:
                return False
            if parent == self.robot:
                return True
            current = parent


if __name__ == "__main__":
    state = CoppeliaState()
    print(state.get_state())