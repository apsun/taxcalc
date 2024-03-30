#!/usr/bin/env python3

max_401k = 23000.00
standard_deduction = 14600.00
tax_brackets = [
    (0.10, 11600.00),
    (0.12, 47150.00),
    (0.22, 100525.00),
    (0.24, 191950.00),
    (0.32, 243725.00),
    (0.35, 609350.00),
    (0.37, float("inf")),
]
long_term_tax_brackets = [
    (0.00, 47025.00),
    (0.15, 518900.00),
    (0.20, float("inf")),
]
supplemental_withholding_rate = 0.22
amt_rate = 0.009
amt_threshold = 200000.00
niit_rate = 0.038
niit_threshold = 200000.00
qbi_deduction_rate = 0.20
max_capital_loss_deduction = 3000.00
