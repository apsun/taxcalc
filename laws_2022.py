#!/usr/bin/env python3

max_401k = 20500.00
standard_deduction = 12950.00
tax_brackets = [
    (0.10, 10275.00),
    (0.12, 41775.00),
    (0.22, 89075.00),
    (0.24, 170050.00),
    (0.32, 215950.00),
    (0.35, 539900.00),
    (0.37, float("inf")),
]
long_term_tax_brackets = [
    (0.00, 41675.00),
    (0.15, 459750.00),
    (0.20, float("inf")),
]
supplemental_withholding_rate = 0.22
amt_rate = 0.009
amt_threshold = 200000.00
niit_rate = 0.038
niit_threshold = 200000.00
qbi_deduction_rate = 0.20
max_capital_loss_deduction = 3000.00
