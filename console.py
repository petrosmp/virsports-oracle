from test import get_scores_per_month


print("Enter the month you wish to get the scores for (0 for current month, available up to 6 months ago):")
month = input()
try:
    month = int(month)
except ValueError:
    print("What you entered is not a integer")
    exit()

get_scores_per_month(month)
