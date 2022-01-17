#!/usr/bin/env python3

max_401k = 19000.00
standard_deduction = 12200.00
tax_brackets = [
    (0.10, 9700.00),
    (0.12, 39475.00),
    (0.22, 84200.00),
    (0.24, 160725.00),
    (0.32, 204100.00),
    (0.35, 510300.00),
    (0.37, float("inf")),
]
long_term_tax_brackets = [
    (0.00, 39375.00),
    (0.15, 434550.00),
    (0.20, float("inf")),
]
supplemental_withholding_rate = 0.22
amt_rate = 0.009
amt_threshold = 200000.00
niit_rate = 0.038
niit_threshold = 200000.00
qbi_deduction_rate = 0.20
