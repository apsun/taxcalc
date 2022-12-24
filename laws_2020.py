#!/usr/bin/env python3

max_401k = 19500.00
standard_deduction = 12400.00
tax_brackets = [
    (0.10, 9875.00),
    (0.12, 40125.00),
    (0.22, 85525.00),
    (0.24, 163300.00),
    (0.32, 207350.00),
    (0.35, 518400.00),
    (0.37, float("inf")),
]
long_term_tax_brackets = [
    (0.00, 40000.00),
    (0.15, 441450.00),
    (0.20, float("inf")),
]
supplemental_withholding_rate = 0.22
amt_rate = 0.009
amt_threshold = 200000.00
niit_rate = 0.038
niit_threshold = 200000.00
qbi_deduction_rate = 0.20
max_capital_loss_deduction = 3000.00
