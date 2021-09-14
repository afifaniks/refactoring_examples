def is_summer(date):
    return date.before(SUMMER_START) \
        or date.after(SUMMER_END)

def calculate_summer_charge(qty, summer_rate):
    return qty*summer_rate

def caqlculate_winter_charge(qty, winter_rate, winter_service_charge):
    return qty*winter_rate + winter_service_charge

if is_summer(date):
    charge = calculate_summer_charge(qty, 1)
else:
    charge = caqlculate_winter_charge(qty, 1.5,  2)