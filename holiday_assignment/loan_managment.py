def calculate_interest(metal, purity, amount, tenure):

    rates = {
        "gold": {18: 12, 22: 10, 24: 8},
        "silver": {925: 11, 950: 10, 999: 9},
        "platinum": {900: 9, 950: 8, 999: 7}
    }

    metal = metal.lower()

    if metal not in rates:
        raise ValueError("Invalid metal type.")

    if purity not in rates[metal]:
        raise ValueError("Unsupported purity for this metal.")

    interest_rate = rates[metal][purity]

    interest = (amount * interest_rate * tenure) / 100

    return interest


def process_loan(*args):
    try:
        result = calculate_interest(*args)

    except TypeError as e:
        print("Type Error:", e)

    except ValueError as e:
        print("Value Error:", e)

    else:
        print("Interest Amount: Rs.", result)

    finally:
        print("Loan processing completed.\n")


# Valid loan
process_loan("gold", 22, 500000, 2)

# Missing arguments
process_loan()
process_loan("gold")
process_loan("gold", 22)
process_loan("silver")

# Invalid metal
process_loan("diamond", 999, 100000, 2)

# Invalid purity
process_loan("gold", 15, 100000, 2)