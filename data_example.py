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

# Taxable interest (e.g. savings account, CD, tax refund)
taxable_interest = (
    + 0.00
)

# Long and short term capital gains (or losses), either from selling
# stonks or from capital gain distributions.
long_term_capital_gains = (
    + 0.00  # stonks
    + 0.00  # capital gain distributions
)
short_term_capital_gains = (
    + 0.00  # stonks
    + 0.00  # gains on RSUs between vest -> sell
)

# Total ordinary dividends from 1099-DIV. INCLUDE qualified
# dividends and section 199A dividends in this value.
total_ordinary_dividends = (
    + 0.00
)

# Qualified dividends from 1099-DIV.
qualified_dividends = (
    + 0.00
)

# Section 199A dividends from 1099-DIV.
section_199a_dividends = (
    + 0.00
)

# Foreign tax paid from 1099-DIV.
foreign_tax_paid = (
    + 0.00
)
