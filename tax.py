#!/usr/bin/env python3
#
# A basic federal tax withholding calculator. NO WARRANTY PROVIDED.
# Use this as a supplement for your tax software, not a replacement.
# It makes a lot of assumptions that may not apply to your situation.
# These include, but are not limited to:
#
# - single, no dependents, no disabilities
# - max out traditional 401k
# - take the standard deduction
# - no alternative minimum tax
# - all income is from wages, bonuses, RSUs, benefits, stonks, interest
# - no self-employment, real estate, or other weird income sources

from laws_2025 import *
from data_2025 import *

def do_tax(base, x, brackets):
    total = 0.00
    for rate, ceil in brackets:
        if base <= ceil:
            total += rate * x
            break
        curr = max(0.00, ceil - base + x)
        total += rate * curr
        x -= curr
    return total

def do_income_tax(ordinary_tax_rate_income):
    return do_tax(ordinary_tax_rate_income, ordinary_tax_rate_income, tax_brackets)

def do_capital_gains_tax(taxable_income, long_term_rate_investment_income):
    return do_tax(taxable_income, long_term_rate_investment_income, long_term_tax_brackets)

def do_additional_medicare_tax(medicare_wages):
    return max(0.00, medicare_wages - amt_threshold) * amt_rate

def do_net_investment_income_tax(agi, investment_income):
    return max(0.00, min(agi - niit_threshold, investment_income)) * niit_rate

def do_capital_loss_carryover(capped_capital_gains, short_term_capital_gains, long_term_capital_gains):
    capped_loss = -capped_capital_gains
    short_term_loss = max(0.00, -short_term_capital_gains)
    long_term_gains = max(0.00, long_term_capital_gains)
    short_term_carryover = max(0.00, short_term_loss - capped_loss - long_term_gains)

    long_term_loss = max(0.00, -long_term_capital_gains)
    short_term_gains = max(0.00, short_term_capital_gains)
    remaining_capped_loss = max(0.00, capped_loss - short_term_loss)
    long_term_carryover = max(0.00, long_term_loss - remaining_capped_loss - short_term_gains)

    return (short_term_carryover, long_term_carryover)

# W-2 income
remaining_salary = remaining_pay_periods / pay_periods_per_year * annual_salary
remaining_imputed_income = imputed_income_per_period * remaining_pay_periods + imputed_income_one_time
remaining_bonus = annual_salary / bonus_payouts_per_year * bonus_multiplier * remaining_bonus_payouts
remaining_rsu_value = rsu_price * remaining_rsu_shares
remaining_supplemental = remaining_bonus + remaining_rsu_value
non_investment_income = (
    + ytd_gross_pay
    + remaining_salary
    + remaining_imputed_income
    + remaining_supplemental
)

# Investment income
total_capital_gains = long_term_capital_gains + short_term_capital_gains
capped_capital_gains = max(total_capital_gains, -max_capital_loss_deduction)
long_term_rate_capital_gains = max(0.00, min(long_term_capital_gains, total_capital_gains))
short_term_capital_loss_carryover, long_term_capital_loss_carryover = do_capital_loss_carryover(
    capped_capital_gains,
    short_term_capital_gains,
    long_term_capital_gains,
)
long_term_rate_investment_income = (
    + long_term_rate_capital_gains
    + qualified_dividends
)
investment_income = (
    + capped_capital_gains
    + taxable_interest
    + total_ordinary_dividends
)

# Taxable income
income_without_deductions = non_investment_income + investment_income
pre_tax_deductions_without_401k = pre_tax_deductions_per_period * pay_periods_per_year + pre_tax_deductions_one_time
pre_tax_deductions = pre_tax_deductions_without_401k + max_401k
medicare_wages = non_investment_income - pre_tax_deductions_without_401k
total_income = agi = magi = income_without_deductions - pre_tax_deductions
qbi_deduction = section_199a_dividends * qbi_deduction_rate
taxable_income = max(0.00, agi - standard_deduction - qbi_deduction)
ordinary_tax_rate_income = max(0.00, taxable_income - long_term_rate_investment_income)

# Total tax
income_tax = do_income_tax(ordinary_tax_rate_income)
capital_gains_tax = do_capital_gains_tax(taxable_income, long_term_rate_investment_income)
additional_medicare_tax = do_additional_medicare_tax(medicare_wages)
net_investment_income_tax = do_net_investment_income_tax(agi, investment_income)
tax_credit = (
    + foreign_tax_paid
)
tax = (
    + income_tax
    + capital_gains_tax
)
other_tax = (
    + net_investment_income_tax
    + additional_medicare_tax
)
total_tax = (
    + tax
    + other_tax
    - tax_credit
)

# Withholding
withholding_salary = ytd_withholding + last_withholding * remaining_pay_periods
withholding_supplemental = remaining_supplemental * supplemental_withholding_rate
withholding_without_amt = withholding_salary + withholding_supplemental
extra_withholding = (total_tax - additional_medicare_tax) - withholding_without_amt
extra_withholding_per_pay_period = None
if remaining_pay_periods > 0:
    extra_withholding_per_pay_period = extra_withholding / remaining_pay_periods

for k, v in globals().copy().items():
    if "__" not in k and isinstance(v, (float, int)):
        if isinstance(v, float) and not k.endswith("_rate"):
            v = f"{v:.02f}"
        print(f"{k} = {v}")
