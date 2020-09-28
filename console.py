from test import get_scores_per_month
import sys

try:
    if sys.argv[1] == "-V" or sys.argv[1] == "-v" or sys.argv[1] == "--verbose":
        print("Enter the month you wish to get the scores for (0 for current month, available up to 6 months ago):")
        month = input()
        try:
            month = int(month)
        except ValueError:
            print("What you entered is not a integer")
            exit()
        get_scores_per_month(month, 1)
    elif sys.argv[1] == "--help" or sys.argv[1] == "-H" or sys.argv[1] == "-h":
        print("Parameters:")
        print("--verbose (-v or -V): script runs in verbose mode")
        print("--help: displays this help message")
        exit()      
except IndexError:
    print("Enter the month you wish to get the scores for (0 for current month, available up to 6 months ago):")
    month = input()
    try:
        month = int(month)
    except ValueError:
        print("What you entered is not a integer")
        exit()
    get_scores_per_month(month, 0)