from xml.dom import minidom
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Specify the input fcd filename")
parser.add_argument("--output", help="Specify the output tcl filename")
args = parser.parse_args()
if args.input and args.output:
    cars=[]
    f = open(args.output, "a")
    mydoc = minidom.parse(args.input)
    items = mydoc.getElementsByTagName('timestep')
    for item in items:
        vectime = item.getAttribute('time')
        vehicles=item.getElementsByTagName('vehicle')
        for vehicle in vehicles:
            if int(vehicle.getAttribute('id')) not in cars:
                f.write("$node_("+str(vehicle.getAttribute('id'))+") set X_ "+str(vehicle.getAttribute('x'))+"\n")
                f.write("$node_("+str(vehicle.getAttribute('id'))+") set Y_ "+str(vehicle.getAttribute('y'))+"\n")
                cars.append(int(vehicle.getAttribute('id')))
            f.write("$ns_ at "+str(vectime)+" \"$node_("+str(vehicle.getAttribute('id'))+") setdest "+str(vehicle.getAttribute('x'))+" "+str(vehicle.getAttribute('y'))+" "+str(vehicle.getAttribute('speed'))+"\"\n")
    f.close()
else:
    if not args.input:
        print("Please define the SUMO fcd input filename")
    if not args.output:
        print("Please define the Tcl output filename")