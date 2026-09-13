def present_value_annuity(rate, term, payment):
    """Present value of an ordinary annuity, paid at the end of each period."""
    return payment * (1 - (1 + rate) ** -term) / rate

def discountFactor(rate, term = 1):
    "Discount factor of a given cashflow"
    return (1+rate)**-term

# Note an annutiy due is a payment at beginning of each period hence follows
# the given formula
def annuityDue(rate, term, payment):
    return present_value_annuity(rate, term, payment)*(1+rate)

def increasingAnnuity(rate, term, payment):
    "Increasing annuity formula where payments increase constantly (non-level)"
    return payment * ((annuityDue(rate, term, 1) - term*discountFactor(rate, term)) / rate)

def geometricRate(rateIncrease, effectiveRate):
    "Adjusted rate for geometric growth"
    return (1+effectiveRate)/(1+rateIncrease) - 1



if __name__ == "__main__":
    print(present_value_annuity(0.06, 10, 500))

