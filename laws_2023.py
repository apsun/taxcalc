#!/usr/bin/env python3

max_401k = 22500.00
standard_deduction = 13850.00
tax_brackets = [
    (0.10, 11000.00),
    (0.12, 44725.00),
    (0.22, 95375.00),
    (0.24, 182100.00),
    (0.32, 231250.00),
    (0.35, 578125.00),
    (0.37, float("inf")),
]
long_term_tax_brackets = [
    (0.00, 44625.00),
    (0.15, 492300.00),
    (0.20, float("inf")),
]
supplemental_withholding_rate = 0.22
amt_rate = 0.009
amt_threshold = 200000.00
niit_rate = 0.038
niit_threshold = 200000.00
qbi_deduction_rate = 0.20
max_capital_loss_deduction = 3000.00
