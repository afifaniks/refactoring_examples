def get_expense_limit(self):
    assert self.expenseLimit != NULL_EXPENSE
    
    return self.expenseLimit if self.expenseLimit != NULL_EXPENSE else \
        self.primaryProject.getMemberExpenseLimit()