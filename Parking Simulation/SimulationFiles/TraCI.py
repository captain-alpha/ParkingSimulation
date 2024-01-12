import traci
import time
sumoBinary = "C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo-gui.exe"
sumoCmd = [sumoBinary, "-c", "C:\\Users\\abdul\\Desktop\\Sumo files\\LastParkSimulation\\osm.sumocfg"]
traci.start(sumoCmd)

print("Starting SUMO")
traci.gui.setSchema("View #0", "Our_Settings")
j = 0
while(j<3600):
    #this runs one simulation step
    time.sleep(0.02)
    traci.simulationStep()

    vehicles=traci.vehicle.getIDList()
    if (j%500)==0: #every 10 sec....
        for i in range(0,len(vehicles)):
            traci.vehicle.setSpeedMode(vehicles[i],0)
            #sets the speed of vehicles to 15 (m/s)
            traci.vehicle.setSpeed(vehicles[i],15)
            #get actual speed, emission, edge ID and total distance travelled of vehicles
            with open('C:\\Users\\abdul\\Desktop\\Sumo files\\LastParkSimulation\\vehicleData.txt', 'w') as file:
                for i in range(len(vehicles)):
                    vehicle = vehicles[i] + " Parameters"
                    speed_str = "Speed" + ": " + str(traci.vehicle.getSpeed(vehicles[i])) + " m/s"
                    position_str = 'Position' + ": " + str(traci.vehicle.getPosition(vehicles[i]))
                    route_str = 'Route' + ": " + str(traci.vehicle.getRoute(vehicles[i]))
                    co2_str = "CO2Emission" + ": " + str(traci.vehicle.getCO2Emission(vehicles[i])) + " mg/s"
                    lane_id_str = "Lane ID of vehicle" + ": " + str(traci.vehicle.getLaneID(vehicles[i]))
                    distance_str = 'Distance' + ": " + str(traci.vehicle.getDistance(vehicles[i])) + " m"

                    # Write to the file
                    file.write(vehicle + '\n')
                    file.write(speed_str + '\n')
                    file.write(position_str + '\n')
                    file.write(route_str + '\n')
                    file.write(co2_str + '\n')
                    file.write(lane_id_str + '\n')
                    file.write(distance_str + '\n')
                    file.write('\n')


        with open('C:\\Users\\abdul\\Desktop\\Sumo files\\LastParkSimulation\\parkingLotData.txt', 'w') as file:
            file.write('Parkin Area' + '\t' + 'Parked Vehicle Count\n')
            for i in range(0, 49):
                parkingArea = "pa_" + str(i)
                vehicleCount = traci.parkingarea.getVehicleCount("pa_" + str(i))

                file.write(parkingArea + '\t\t' + str(vehicleCount))
                file.write('\n')
        print("Data is saved!!")
    j = j+1

#get network parameters
IDsOfEdges=traci.edge.getIDList()
print("IDs of the edges:", IDsOfEdges)
IDsOfJunctions=traci.junction.getIDList()
print("IDs of junctions:", IDsOfJunctions)
traci.close()