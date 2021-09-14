from typing import Union

def is_eligible(
    seniority: int, 
    months_disabled: int, 
    is_parttime: bool):

    if seniority < 2 \
        or months_disabled > 12 \
        or is_parttime:
        return True
    
    return False


def disability_amount(
    seniority: int, 
    months_disabled: int, 
    is_parttime: bool) -> Union[int, bool]:
    
    if is_eligible():
        return 0
        
    return None