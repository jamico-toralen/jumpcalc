# jumpcalc.py
# A simple program with a simple goal: to calculate the per-system jump time for a route in EVE
# Created by Jamico Toralen

# Import basics
import math
import argparse
# Create the parser
parser = argparse.ArgumentParser(description='Takes in basic inputs and calculates your expected average per-jump travel time. By default returns the average per-jump gate-to-gate time, but you can request averages broken down by sec status or even specify a custom gate-to-gate distance to use.', epilog='Tips accepted if you find this useful, please send them to Plarium Marketing LLC in-game')
# Create required arguments
parser.add_argument('align', metavar = "-a", type = float, help = "Your vessel's align time, in seconds")
parser.add_argument('warp', metavar = "-w", type = float, help = "Your vessel's maximum warp speed, in AU/s")
parser.add_argument('vel', metavar = "-v", type = float, help = "Your vessel's base maximum velocity, with propmod off, in m/s")
# Create optional arguments
parser.add_argument("-f", "--full", help = "View a full breakdown of average warp times, by sec status", action = "store_true")
parser.add_argument("-d", "--dist", type = int, help = "A specified distance, to override in the calculations")
# Create a variable to hold the arguments from the parser
args = parser.parse_args()
# Warn the user about vessels warping faster than 6AU/s
if (args.warp > 6):
    print("WARNING: Results will be inaccurate for vessels warping faster than 6AU/s. Take these results with a grain of salt.")
# Calculate the average system warp time
warptime = args.align + (25.7312 / args.warp) + (24 / args.warp) + ((math.log((args.warp * 149597870700) / min(args.vel / 2, 100))) / (min(args.warp / 3, 2))) + 10
# Handle the -f flag
if args.full == True:
# Calculate the warp times for each sec region
    warptimehs = args.align + (25.7312 / args.warp) + (25.1 / args.warp) + ((math.log((args.warp * 149597870700) / min(args.vel / 2, 100))) / (min(args.warp / 3, 2))) + 10
    warptimels = args.align + (25.7312 / args.warp) + (24.1 / args.warp) + ((math.log((args.warp * 149597870700) / min(args.vel / 2, 100))) / (min(args.warp / 3, 2))) + 10
    warptimens = args.align + (25.7312 / args.warp) + (23.4 / args.warp) + ((math.log((args.warp * 149597870700) / min(args.vel / 2, 100))) / (min(args.warp / 3, 2))) + 10
# Print the results
    print("Overall Average : " + '{:.2f}'.format(round(warptime, 2)) + "s")
    print("Highsec Average : " + '{:.2f}'.format(round(warptimehs, 2)) + "s")
    print("Lowsec Average :  " + '{:.2f}'.format(round(warptimels, 2)) + "s")
    print("Nullsec Average : " + '{:.2f}'.format(round(warptimens, 2)) + "s")
# Handle the -d flag, if the -f flag isn't set
elif args.dist != 0:
# Warn the player about short warps and then calculate with the cruise phase removed
    if args.dist < 4:
        print("WARNING: Results will be inaccurate for distances less than 4AU due to the lack of a Cruise phase. Take these results with a grain of salt.")
        warptimedist = args.align + (25.7312 / args.warp) + ((math.log((args.warp * 149597870700) / min(args.vel / 2, 100))) / (min(args.warp / 3, 2))) + 10
# Otherwise, calculate normally
    else:
        warptimedist = args.align + (25.7312 / args.warp) + ((args.dist - 4) / args.warp) + ((math.log((args.warp * 149597870700) / min(args.vel / 2, 100))) / (min(args.warp / 3, 2))) + 10
# Print the results
    print("Jump time : " + '{:.2f}'.format(round(warptimedist, 2)) + "s")
# Handle the default case
else:
# Print the results
    print("Jump time : " + '{:.2f}'.format(round(warptime, 2)) + "s")
