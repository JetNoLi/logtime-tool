from math import floor, ceil

def calculate_start_and_end(args):
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

    return args;