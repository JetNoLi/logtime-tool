#! /usr/local/bin/python

import argparse;
from datetime import datetime;
from math import ceil, floor;
from utils import validate_input;
import json;

parser = argparse.ArgumentParser(
    prog="logtime-tool",
    description= "logs time to output file",
)

# First Add positional Arg
parser.add_argument("description", nargs="*")

# Add Flags
parser.add_argument("-d", "--duration", required=False, type=int)
parser.add_argument("-t", "--tag", required=False)
parser.add_argument("-s", "--start", required=False,)
parser.add_argument("-e", "--end", required=False)

args = parser.parse_args()

is_valid, args, missing_values = validate_input(args)

print(args)

if is_valid != True:
    for key in missing_values:
        response = input("What is the " +  key +  "? ")
        args[key] = response

# TODO: Handle Start Plus End Manipulation
if args["start"] == None:
    end = args["end"].split(":") # Will be [hour, min]
    diff = abs( int(end[1]) - args["duration"])
    hour = int(end[0]) - ceil(float(diff) / float(60))
    args["start"] = str(hour) + ":" + str(60 - (diff % 60))

if args["end"] == None:
    start = args["start"].split(":") # Will be [hour, min]
    diff = abs( int(start[1]) + args["duration"])
    hour = int(start[0]) + floor(float(diff) / float(60))
    args["end"] = str(hour) + ":" + str(diff % 60)

print(args)

config = None
config_path = "/Users/jethendricks/Desktop/Projects/Scripts/logtime-tool/config.json"
# TODO: Add Config File
with open(config_path) as config_file:
    config = json.load(config_file)

print(config)

logs_folder="/Users/jethendricks/Desktop/Projects/Scripts/logtime-tool/time-logs/"
create_name = logs_folder + datetime.now().strftime("%d-%m-%Y") + ".txt"

# TODO: Add Ouptut File Writing
with open(create_name, "a+") as output:
    line = "[" + config["project"] + "][" + config["ticket"] + "][" + args["start"] + " - " + args["end"] + "] " + " ".join(args["description"]) + " [" +args["tag"]+ "]" + "\n"
    print(line)
    output.write(line)

# TODO: Add to path