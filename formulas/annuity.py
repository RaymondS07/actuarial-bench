def present_value_annuity(rate, term, payment):
    """Present value of an ordinary annuity, paid at the end of each period."""
    return payment * (1 - (1 + rate) ** -term) / rate


if __name__ == "__main__":
    print(present_value_annuity(0.06, 10, 500))