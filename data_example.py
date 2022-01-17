#!/usr/bin/env python3

# --------------------------------------------------
# job-related income parameters
# --------------------------------------------------

# facts obtained from your latest paystub
pay_periods_per_year = 26
remaining_pay_periods = 25
annual_salary = 123456.78
last_withholding = 123.45
ytd_withholding = 123.45
ytd_gross_pay = 1234.56

# imputed income (taxable benefits). typically things like exercise
# benefit, disability/life insurance. do NOT include imputed income
# in the one-time value that has already been added to your gross pay.
imputed_income_one_time = (
    + 0.00
)
imputed_income_per_period = (
    + 0.00
)

# everything in the pre-tax section in your paystub, EXCEPT for 401k.
# typically things like FSA, health insurance.
pre_tax_deductions_one_time = (
    + 0.00
)
pre_tax_deductions_per_period = (
    + 0.00
)

# guesstimate how much your bonus multiplier will be.
# assumption: bonus = (multiplier * salary / payouts per year)
bonus_payouts_per_year = 2
remaining_bonus_payouts = 2
bonus_multiplier = 0.125

# income from bonus and RSUs. guesstimate a price for when the RSUs
# will vest (assuming you sell them immediately). do NOT include
# shares that have already vested and are included in your gross pay.
rsu_price = 123.45
remaining_rsu_shares = (
    + 100  # feb
    + 100  # may
    + 100  # aug
    + 100  # nov
)

# --------------------------------------------------
# investment income parameters
# --------------------------------------------------

# long and short term capital gains (or losses)
long_term_capital_gains = (
    + 0.00  # long term capital gains
)
short_term_capital_gains = (
    + 0.00  # short term capital gains
    + 0.00  # gains on RSUs between vest -> sell
)

# investment income that's taxed at the long term capital gains rate,
# EXCLUDING long term capital gains itself. includes:
#
# - capital gain distributions
# - qualified dividends
other_long_term_investment_income = (
    + 0.00  # capital gain distributions
    + 0.00  # qualified dividends
)

# investment income that's taxed at the ordinary income tax rate,
# EXCLUDING short term capital gains itself. includes:
#
# - interest (savings, CD, tax refund, etc)
# - non-qualified dividends (ordinary dividends - qualified dividends)
other_short_term_investment_income = (
    + 0.00  # savings interest
    + 0.00  # non-qualified dividends
)

# deductions and credits from 1099-div
section_199a_dividends = 0.00
foreign_tax_paid = 0.00
