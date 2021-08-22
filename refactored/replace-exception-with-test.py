def get_value_for_period(period_number):
    if period_number < 0 or period_number >= len(values):
        return -1

    return values[period_number]