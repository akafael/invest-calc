"""
Python Compound Interest Calculator

This program calculates compound interest based on the principal amount, interest rate,
and time period provided by the user.

Author: Andre Almeida
Date: 3/13/2024

"""

import csv


def calculate_total_amount(principal, monthly_payment, yearly_rate, years):
    """
    Function to calculate total amount based on compound interest.

    Args:
        principal (float): The principal amount.
        monthlyPayment (float): The monthly contribution.
        yearly_rate (float): The annual interest rate (in percentage).
        years (float): The time period (in years).

    Returns:
        float array: The total amount.
    """
    # Calculate compound interest
    total_amount = [principal]
    for i in range(1, years*12+1):
        total_amount.append(total_amount[i-1] + total_amount[i-1] * yearly_rate / 12 / 100 + monthly_payment)

    return total_amount

def calculate_interest(principal, monthly_payment, yearly_rate, years):
    """
    Function to calculate total amount based on compound interest.

    Args:
        principal (float): The principal amount.
        monthlyPayment (float): The monthly contribution.
        yearly_rate (float): The annual interest rate (in percentage).
        years (int): The time period (in years).

    Returns:
        float array: The compound interest.
    """
    # Calculate compound interest
    total_amount = calculate_total_amount(principal, monthly_payment, yearly_rate, years)

    interest = [0]
    for i in range(1, years*12+1):
        interest.append(total_amount[i]-(principal+monthly_payment*i))

    return interest

def build_csv_file(principal, monthly_payment, rate, time):
    """
    Write data to a CSV file.

    Args:
        principal (float): The principal amount.
        monthlyPayment (float): The monthly contribution.
        rate (float): The annual interest rate (in percentage).
        time (int): The time period (in years).
    """

    filename = "compound_interest.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        total_amount = calculate_total_amount(principal, monthly_payment, rate, time)
        interest = calculate_interest(principal, monthly_payment, rate, time)

        writer.writerow(['Month', 'Investment', 'Accumulated Investment', 'Accumulated Interest', 'Balance'])
        writer.writerow([0, principal, principal, 0, principal])
        for i in range(1, time*12+1):
            writer.writerow([i, monthly_payment, round(total_amount[i]-interest[i],2), round(interest[i],2), round(total_amount[i],2)])

    print(f"Data has been written to '{filename}' successfully.")


def main():
    # Input principal amount, interest rate, and time period
    principal = float(input("Enter the principal amount: "))
    monthly_payment = float(input("Enter montly payment amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = int(input("Enter the time period (in years): "))

    # Calculate compound interest
    total_amount = calculate_total_amount(principal, monthly_payment, rate, time)
    interest = calculate_interest(principal, monthly_payment, rate, time)

    # Display the result
    for i in range(time+1):
        print(f"\nTotal amount after {i} years: {round(total_amount[i*12],2)}")
        print(f"Interest amount after {i} years: {round(interest[i*12], 2)}")

    # Build detailed CSV file
    build_csv_file(principal, monthly_payment, rate, time)

if __name__ == "__main__":
    main()
