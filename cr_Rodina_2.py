import argparse
parser = argparse.ArgumentParser()
parser.add_argument("temparature_C", type=float,
                    help="Temperature in Cel")
args = parser.parse_args()
answer = temperature_C**2
