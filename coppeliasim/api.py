from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from get_state import CoppeliaState

def main():
    state = CoppeliaState()
    print(state.get_state())

if __name__ == "__main__":
    main()

# client = RemoteAPIClient
# sim = client.require("sim")

# sim.setStepping(True)

# sim.startSimulation()
# while (t := sim.getSimulationTime()) < 60:
#     print(f'Simulation time: {t:.2f} [s]')
#     sim.step()
# sim.stopSimulation()


# objectHandle = sim.getObjects(0, sim.handle_all)
# print(objectHandle)

# i = 1
# while objectHandle is not None:
#     objectHandle = sim.getObjects(i, sim.handle_all)
#     print(objectHandle)
#     i+=1
