import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
count = 0
if args.payment is None:
    count += 1
if args.principal is None:
    count += 1
if args.periods is None:
    count += 1

if count == 1 and args.interest is not None:
    if args.type == "annuity":

        if args.periods is None:
            principal = float(args.principal)
            payment = float(args.payment)
            interest = float(args.interest) / 1200
            n = math.ceil(math.log((payment / (payment - interest * principal)), 1 + interest))
            overpayment = payment * n - principal

            if n < 12:
                if n == 1:
                    print("It will take", n, "month to repay this loan!")
                else:
                    print("It will take", n, "months to repay this loan!")
            elif n % 12 == 0:
                if n == 12:
                    print("It will take", int(n / 12), "year to repay this loan!")
                else:
                    print("It will take", int(n / 12), "years to repay this loan!")
            else:
                if n == 13:
                    print("It will take", int(n // 12), "year and",
                          n % 12, "month to repay this loan!")
                elif n < 24:
                    print("It will take", int(n // 12), "year and",
                          n % 12, "months to repay this loan!")
                elif n % 12 == 1:
                    print("It will take", int(n // 12), "years and",
                          n % 12, "month to repay this loan!")
                else:
                    print("It will take", int(n // 12), "years and",
                          n % 12, "months to repay this loan!")
            print(f"Overpayment = {int(overpayment)}")

        elif args.payment is None:
            principal = float(args.principal)
            n = int(args.periods)
            interest = float(args.interest) / 1200
            payment = math.ceil(principal * interest * (1 + interest) ** n /
                                ((1 + interest) ** n - 1))
            last_payment = principal - payment * (n - 1)
            overpayment = payment * n - principal
            print(f"Your monthly payment = {payment}!")
            print(f"Overpayment = {int(overpayment)}")

        elif args.principal is None:
            payment = float(args.payment)
            n = float(args.periods)
            interest = float(args.interest) / 1200
            principal = payment / ((interest * (1 + interest) ** n) / ((1 + interest) ** n - 1))
            overpayment = payment * n - math.floor(principal)
            print(f"Your loan principal = {math.floor(principal)}!")
            print(f"Overpayment = {int(overpayment)}")

    elif args.type == "diff" and args.payment is None:
        principal = float(args.principal)
        n = int(args.periods)
        interest = float(args.interest) / 1200
        payments = list(range(n + 1))
        payments[0] = 0

        for i in range(1, n + 1):
            payments[i] = math.ceil((principal / n)
                                    + interest * (principal - (principal * (i - 1)) / n))
            print(f"Month, {i}: payment is {payments[i]}")
        overpayment = sum(payments) - principal
        print(f"Overpayment = {int(overpayment)}")

    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
