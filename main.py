import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_time", help="start time")
    args = parser.parse_args()
    print("start_time = {}".format(args.start_time))

