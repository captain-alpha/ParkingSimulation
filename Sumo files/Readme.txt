Steps to launch and view simulation: 

Download and install the latest version of Python:
https://www.python.org/downloads/
Download and install the latest version of SUMO to your computer:
https://sumo.dlr.de/docs/Downloads.php
Open the Parking Simulation folder and open sumo file.

These are necessary steps to launch the simulation with the provided map.

However, if you want to create a simulation with a different map you choose, open OSMWebWizard to select a specific area and generate a simulation. Then, you need to use 2 tools (located in tools folder) to generate random parking areas and generate parking area routes for cars:

1) Execute generateParkingAreas.py in your simulation folder created with OSM using this command:
python generateParkingAreas.py -n <my network>
(<my network> is your osm.net.xml.gz file)
2) Then execute generateParkingAreaRerouters.py in your simulation folder created with OSM using this command: 
python generateParkingAreaRerouters.py -n <net-file> -a <parkingArea-file> -o <output-file>
(<net-file> is your osm.net.xml.gz file, <parkingArea-file> is the file you created using the first tool, <output-file> is your output file that you can give any name.)