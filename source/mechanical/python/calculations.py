import math

# See this page for others:
# https://docs.google.com/spreadsheets/d/1MO_MTQGfHK8qPuBR74QlUKQ68MMGChDq6vC7X30unAk/edit#gid=0


def calculate_torque(kv, current):
    rev = math.pi * 2
    rad_to_rpm = 1.0 / rev * 60
    return rad_to_rpm / kv * current


if __name__ == "__main__":
    print(f"Turnigy SK8 6374-192KV = {calculate_torque(kv=192, current=100):.2f}Nm")

    # This one can be found here:
    # https://hobbyking.com/en_us/turnigy-sk8-6374-149kv-sensored-brushless-motor-14p.html
    print(f"Turnigy SK8 6374-149KV = {calculate_torque(kv=149, current=80):.2f}Nm")

