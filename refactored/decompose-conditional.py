def is_summer(date):
    return date.before(SUMMER_START) \
        or date.after(SUMMER_END)

def calculate_summer_charge(qty):
    return qty*summer_rate

def caqlculate_winter_charge(qty):
    return qty*winter_rate + winter_service_charge

if is_summer(date):
    charge = calculate_summer_charge(qty)
else:
    charge = caqlculate_winter_charge(qty)