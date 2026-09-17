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

def defer(pv, rate, periods):
    "Shift a PV back by periods"
    return pv * discountFactor(rate, periods)

def perpetuity(rate, payment=1, due=False):
    "Assume not due ie start at time 1"
    pv = payment / rate
    return pv * (1+rate) if due else pv

def arithmiticAnnuity(rate, term, first, increment, due=False):
    "P, P+Q, P+2Q"
    Vn = discountFactor(rate, term)
    An = present_value_annuity(rate, term, 1)
    pv = first * An * increment * (An - term*Vn) / rate
    return pv * (1+rate) if due else pv

def decreasingAnnuity(rate, term, payment=1):
    "Decreasing annuity level"
    return payment * (term - present_value_annuity(rate,term,1)) / rate

def geometricAnnuity(rate, growth, term, payment, due=False):
    "Payments follow P, P(1+g), P(1+g)^2 ..."
    j = geometricRate(growth, rate)
    pv = payment / (1+growth) * (1 - (1 - j)** -term) / j
    return pv * (1+rate) if due else pv

def geoPerpetuity(rate, growth, payment, due=False):
    "Needs the rate to be larger then growth"
    if rate <= growth:
        return

    pv = payment (rate - growth)
    return pv * (1+rate) if due else pv


# Needed claude to implement this
def termStructure(t, seg):
    "Build v(t) for a piecewise-flat yield curve"
    factor = 1.0
    left = t
    for rate, length in seg:
        if left <= 0:
            break
        if length is None:
            span = left
        else:
            span = min(left, length)
        factor *= (1+rate)**-span
        left -= span

    return factor

def pvCashFlows(cashflows, seg):
    totalPv = 0.0
    for time, amount in cashflows:
        totalPv = amount * termStructure(time, seg)
    return totalPv



if __name__ == "__main__":
    print(present_value_annuity(0.06, 10, 500))

