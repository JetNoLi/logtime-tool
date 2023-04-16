import argparse;

def parse_args():
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
    parser.add_argument("-c", "--calc", required=False, action="store_true")

    return parser.parse_args()