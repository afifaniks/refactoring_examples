def get_pay_amount(self):
    if self.is_dead:
        return get_dead_amount()
    if self.is_separated:
        return get_separated_amount()
    if self.is_retired:
        return get_retired_amount()
        
    return normal_amount()