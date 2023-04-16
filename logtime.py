#! /usr/local/bin/python
import sys

from utils.validation_utils import validate_input;
from utils.cli_utils import parse_args;
from utils.time_utils import calculate_start_and_end;
from utils.file_utils import get_file_name, get_config, get_log_entry, calculate_total_time_logged;

# Get args using argparse
args = parse_args()

# create output folder
create_name = get_file_name()

# Check is user just wants to see time logged
if args.calc != None:
    print("Current time logged today is", calculate_total_time_logged(create_name))
    sys.exit()

is_valid, args, missing_values = validate_input(args)

if is_valid != True:
    for key in missing_values:
        response = input("What is the " +  key +  "? ")
        args[key] = response

args = calculate_start_and_end(args)

print(args)

# Read Config for ticket info and project name
config = get_config()


with open(create_name, "a+") as output:
    line = get_log_entry(args, config)
    print(line)
    output.write(line)

getTotalTimeLogged = calculate_total_time_logged(create_name);