# Retirement & Investment Guide CLI

A lightweight, interactive command-line application written in Python to help users evaluate their monthly budget, determine discretionary income, and calculate savings targets needed to reach retirement within a specified timeframe.

---

## Features

- **Income & Expense Tracking**: Collects annual post-tax income and common monthly living expenses (rent/mortgage, vehicle, utilities, groceries, transport, phone, debt).
- **Discretionary Income Calculation**: Calculates disposable monthly income after mandatory expenses.
- **Deficit Detection**: Automatically prompts the user to re-evaluate if monthly expenses exceed income.
- **Retirement Savings Target**: Estimates how much money you need to save each month based on your target retirement horizon and existing savings/investments.
- **Input Validation**: Ensures all monetary and time values are non-negative integers.

---

## Requirements

- **Python 3.6+** (no third-party dependencies required; uses Python standard library only).

---

## Installation & Setup

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/your-username/retirement-guide.git
   cd retirement-guide
   ```

2. **Save the script:**
   Ensure the script is saved as `main.py` (or your preferred file name).

---

## Usage

Run the script from your terminal:

```bash
python main.py
```

### Example Walkthrough

```text
Welcome to retirement and investment guide
--------------------------------------------
Please enter your yearly salary after taxes:
60000
--------------------------------------------
We will now ask for your mandatory expenses
--------------------------------------------
Please enter your monthly rent or morgage payments:
1500
--------------------------------------------
Please enter your monthly car payments:
300
--------------------------------------------
Please enter your monthly utilities/bills:
150
--------------------------------------------
Please enter your monthly grocery bill
(Not including eating out):
400
--------------------------------------------
Please enter your monthly transportation costs
(i.e. Gas, car insurance, vehicle maintenence):
200
--------------------------------------------
Please enter your monthly phone bill:
80
--------------------------------------------
Please enter your monthly debt payments (if none, enter 0):
200
--------------------------------------------
After all mandatory expenses, you have $2170 per month to spend
--------------------------------------------
Please enter the sum of your savings and investments:
15000
--------------------------------------------
After how many years would you like to retire?:
25
--------------------------------------------
In order to retire in 25 years, you need to save $2350 dollars per month
This leaves you with $-180 extra dollars to spend each month
```

---

## How the Calculations Work

1. **Monthly Discretionary Income**:
   $$\text{Leftover} = \left(\frac{\text{Salary}}{12}\right) - \sum \text{Mandatory Expenses}$$

2. **Target Nest Egg**:
   $$\text{Retirement Goal} = (\text{Salary} \times 12) - \text{Current Savings}$$

3. **Required Monthly Savings**:
   $$\text{Monthly Savings} = \frac{\text{Retirement Goal}}{\text{Years to Retire} \times 12}$$

4. **Remaining Monthly Buffer**:
   $$\text{Buffer} = \text{Leftover} - \text{Monthly Savings}$$

---

## Potential Improvements & Roadmap

- [ ] Support floating-point input values (cents) instead of strictly integers.
- [ ] Incorporate compound interest / estimated investment returns ($4-8\%$ annual ROI).
- [ ] Adjust for inflation and post-retirement cost-of-living estimates.
- [ ] Add an option to export results to a JSON or CSV file.

---

## License

This project is licensed under the MIT License - feel free to modify and use it for personal or educational projects.