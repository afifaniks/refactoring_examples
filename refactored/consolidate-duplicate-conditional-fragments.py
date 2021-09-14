SPECIAL_OFF = 0.95
NORMAL_OFF = 0.98

def is_special_deal(price: float):
    return True

if is_special_deal(price):
    total = price * SPECIAL_OFF
else:
    total = price * NORMAL_OFF
send()