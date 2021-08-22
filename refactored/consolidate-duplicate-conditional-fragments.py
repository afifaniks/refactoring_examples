def is_special_deal():
    return True

if is_special_deal():
    total = price * 0.95
else:
    total = price * 0.98
send()