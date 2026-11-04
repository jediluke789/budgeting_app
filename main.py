def main():
    print("Welcome to retirement and investment guide")
    print_sep()
    salary = ask_for("Please enter your yearly salary after taxes")
    print_sep()
    print("We will now ask for your mandatory expenses")
    print_sep()
    rent = ask_for("Please enter your monthly rent or morgage payments")
    print_sep()
    car = ask_for("Please enter your monthly car payments")
    print_sep()
    utilities = ask_for("Please enter your monthly utilities/bills")
    print_sep()
    groceries = ask_for("Please enter your monthly grocery bill\n(Not including eating out)")
    print_sep()
    transportation = ask_for("Please enter your monthly transportation costs\n(i.e. Gas, car insurance, vehicle maintenence)")
    print_sep()
    phone = ask_for("Please enter your monthly phone bill")
    print_sep()
    debt = ask_for("Please enter your monthly debt payments (if none, enter 0)")
    print_sep()
    leftover = (salary / 12) - rent - car - utilities - groceries - transportation - phone - debt
    leftover = int(leftover)
    if leftover < 0:
        print("Mandatory expenses are higher than income. Please try again")
        main()
        return
    print(f"After all mandatory expenses, you have ${leftover} per month to spend")
    print_sep()
    savings = ask_for("Please enter the sum of your savings and investments")
    print_sep()
    while True:
        try:
            time = ask_for("After how many years would you like to retire?")
            print_sep()
            # How much you need to save
            retirement = (salary * 12) - savings
            # How much you need to save per month
            monthly = (retirement / time) / 12
            print(f"In order to retire in {time} years, you need to save ${int(monthly)} dollars per month")
            print(f"This leaves you with ${int(leftover - monthly)} extra dollars to spend each month")
            break
        except ValueError:
            print("Please try again")



def ask_for(question: str) -> int:
    while True:
        try:
            amount = int(input(f"{question}:\n"))
            if amount < 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid Input. Please try again")

def print_sep() -> None:
    print("--------------------------------------------")


if __name__ == "__main__":
    main()