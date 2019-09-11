# SumoTclMobilityGen
Tcl mobility generation using sumo fcd output

This Python 3 module is used to generate a mobility Tcl file from a SUMO Simulator FCD (Floating Car Data) file.
The structure of the output file is in the form described by the NS-2 / NS-3 documentation.

$node_(0) set X_ 998.53
$node_(0) set Y_ 1247.06
$ns_ at 0.00 "$node_(0) setdest 998.53 1247.06 0.00"
$ns_ at 0.50 "$node_(0) setdest 999.00 1247.39 1.14"
$node_(1) set X_ 1966.55
$node_(1) set Y_ 2244.43
$ns_ at 1.00 "$node_(1) setdest 1966.55 2244.43 0.00"
$ns_ at 1.50 "$node_(0) setdest 1001.24 1248.95 3.08"

In order to run the module you need to define the filename with the path if necessary for both the input and the output file.

i.e. 

python sumotclmobilitygen.py --input fcd.txt --output test.tcl

It uses the minidom and argparse libraries.