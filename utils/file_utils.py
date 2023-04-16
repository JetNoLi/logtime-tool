from datetime import datetime;
import calendar;
import os;
import json;

def get_config():
    config = None
    config_path = "/Users/jethendricks/Desktop/Projects/Scripts/logtime-tool/config.json"

    with open(config_path) as config_file:
        config = json.load(config_file)

    return config;

def get_file_name():
    logs_folder="/Users/jethendricks/Desktop/Projects/Scripts/logtime-tool/time-logs/"
    year = datetime.now().strftime("%Y")
    month = calendar.month_abbr[int(datetime.now().strftime("%m"))]

    logs_path = logs_folder + year + "/" + month + "/";

    if (os.path.exists(logs_path) == False):
        os.makedirs(logs_path)

    return logs_path + datetime.now().strftime("%d-%m-%Y") + ".txt";

def get_log_entry(args, config):
    return "[" + config["project"] + "][" \
        + config["ticket"] + "][" \
        + args["start"] + " - " + args["end"] + "] " \
        + " ".join(args["description"]) \
        + " <" + args["tag"]+ ">" \
        + " {" + str(args["duration"]) + "}" \
        + "\n"

def calculate_total_time_logged(log_file_name):
    total = 0

    with open(log_file_name, "r") as log_file:
        lines = log_file.readlines()
        
        for line in lines:
            start = line.find("{")
            end = line.find("}")
            total += int( line[start + 1: end])

    return total