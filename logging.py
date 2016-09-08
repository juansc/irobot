def print_error_message_and_exit(message):
    sys.stderr.write("[ERROR] {}\n".format(message))
    sys.exit(1)

def log_message(message):
    print "[INFO] {}".format(message)