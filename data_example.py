#!/usr/bin/env python3

# --------------------------------------
# Job-related income
# --------------------------------------

# Facts obtained from your latest paystub
pay_periods_per_year = 26
remaining_pay_periods = 25
annual_salary = 123456.78
last_withholding = 123.45
ytd_withholding = 123.45
ytd_gross_pay = 1234.56

# Imputed income (taxable benefits). Typically things like exercise
# benefit, disability/life insurance. Do NOT include imputed income
# in the one-time value that has already been added to your gross pay.
imputed_income_one_time = (
    + 0.00
)
imputed_income_per_period = (
    + 0.00
)

# Everything in the pre-tax section in your paystub, EXCEPT for 401k.
# Typically things like FSA, health insurance.
pre_tax_deductions_one_time = (
    + 0.00
)
pre_tax_deductions_per_period = (
    + 0.00
)

# Income from bonus. Guesstimate how much your bonus multiplier will
# be. Assumption: bonus = (multiplier * salary / payouts per year)
bonus_payouts_per_year = 2
remaining_bonus_payouts = 2
bonus_multiplier = 0.125

# Income from RSUs. Guesstimate a price for when the RSUs will vest
# (assuming you sell them immediately). Do NOT include shares that
# have already vested and are included in your gross pay.
rsu_price = 123.45
remaining_rsu_shares = (
    + 100  # Feb
    + 100  # May
    + 100  # Aug
    + 100  # Nov
)

# --------------------------------------
# Investment income
# --------------------------------------

# Long and short term capital gains (or losses)
long_term_capital_gains = (
    + 0.00  # long term capital gains
)
short_term_capital_gains = (
    + 0.00  # short term capital gains
    + 0.00  # gains on RSUs between vest -> sell
)

# Investment income that's taxed at the long term capital gains rate,
# EXCLUDING long term capital gains itself. Non-exhaustive list:
#
# - capital gain distributions
# - qualified dividends
other_long_term_investment_income = (
    + 0.00  # capital gain distributions
    + 0.00  # qualified dividends
)

# Investment income that's taxed at the ordinary income tax rate,
# EXCLUDING short term capital gains itself. Non-exhaustive list:
#
# - interest (savings, CD, tax refund, etc)
# - non-qualified dividends (ordinary dividends - qualified dividends)
other_short_term_investment_income = (
    + 0.00  # savings interest
    + 0.00  # non-qualified dividends
)

# Deductions and credits from 1099-DIV
section_199a_dividends = 0.00
foreign_tax_paid = 0.00
