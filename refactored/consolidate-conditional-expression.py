def disability_amount():
    if is_eligible():
        return 0
    return None

def is_eligible():
    if seniority < 2 \
        or months_disabled > 12 \
        or is_parttime:
        return True
    
    return False