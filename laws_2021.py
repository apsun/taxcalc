#!/usr/bin/env python3

max_401k = 19500.00
standard_deduction = 12550.00
tax_brackets = [
    (0.10, 9950.00),
    (0.12, 40525.00),
    (0.22, 86375.00),
    (0.24, 164925.00),
    (0.32, 209425.00),
    (0.35, 523600.00),
    (0.37, float("inf")),
]
long_term_tax_brackets = [
    (0.00, 40400.00),
    (0.15, 445850.00),
    (0.20, float("inf")),
]
supplemental_withholding_rate = 0.22
amt_rate = 0.009
amt_threshold = 200000.00
niit_rate = 0.038
niit_threshold = 200000.00
qbi_deduction_rate = 0.20
max_capital_loss_deduction = 3000.00
