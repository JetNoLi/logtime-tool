def validate_input(args):
    print(args)

    is_valid = True

    missing_values = {}

    if args.description == None:
        Exception("No Description to Log")
        return

    if args.duration == None:
        is_valid = False
        missing_values["duration"] = True
    
    if args.tag == None:
        is_valid = False
        missing_values["tag"] = True

    if args.start == None and args.end == None:
        is_valid = False
        missing_values["start"] = True

    # If we only recieved end time
    return is_valid, args.__dict__, missing_values