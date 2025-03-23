#!/usr/bin/env python3

max_401k = 23500.00
standard_deduction = 15000.00
tax_brackets = [
    (0.10, 11925.00),
    (0.12, 48475.00),
    (0.22, 103350.00),
    (0.24, 197300.00),
    (0.32, 250525.00),
    (0.35, 626350.00),
    (0.37, float("inf")),
]
long_term_tax_brackets = [
    (0.00, 48350.00),
    (0.15, 533400.00),
    (0.20, float("inf")),
]
supplemental_withholding_rate = 0.22
amt_rate = 0.009
amt_threshold = 200000.00
niit_rate = 0.038
niit_threshold = 200000.00
qbi_deduction_rate = 0.20
max_capital_loss_deduction = 3000.00
