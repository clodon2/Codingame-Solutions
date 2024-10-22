import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    thrust = 100
    normalized_angle = next_checkpoint_angle

    final_thrust = thrust - normalized_angle

    final_thrust = int(final_thrust)

    if final_thrust <= 0:
        final_thrust = 0
    elif final_thrust >= 100:
        final_thrust = 100
        if next_checkpoint_dist >= 400:
            final_thrust = "BOOST"

    final_thrust = " " + str(final_thrust)
        
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + final_thrust)
