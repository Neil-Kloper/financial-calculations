print("BasicRetireCalc()")
print("RetireCalc()")
print("Amortization()")
print("gross_income()")




##update variable names with appropriate terms
## i = Return on investment
## n = cycles (typically years) until goal or end


def BasicRetireCalc():
##Basic calculator to determine ones asset count by retirement.
##based on fixed rate of return and fixed annual contribution
    n = input("How many years from now do you plan to retire: ")
    n = float(n)
    contribution = input("how much do you plan to contribute per year towards retirement?")
    contribution = float(contribution)
    i = input("what is your anticipated ROI for your investments? ")
    i = float(i)
    i = i + 1
    x = 0
    assets = 0
    while x < n:
        assets = assets * i
        assets = assets + contribution
        x = x + 1
    print(x)
    print(round(assets, 2))

def RetireCalc():

    print("welcome to Neil's Advanced Retirement Calculator (version 0.12), for all questions asking for a percentage value please input a decimal eg .01 \n")
    n = input("How many years from now do you plan to retire: ")
    n = float(n)
    print("\nFor the next question, pretend that inflation doesn't exist, we'll calculate that portion for you")
    retire_income = input("How much per month would you like to be able to spend: ")
    retire_income = float(retire_income)
    inflation_rate = .042
    i = input("What is your anticipated return on investment for your retirement savings? ")
    i = float(i)
    if i < inflation_rate:
            print("your return on investment is below your projected rate of inflation, you may want to consider an alternative retirement savings plan\n\n")
            exit
    present_value = input("What do you currently have saved for retirement? ")
    present_value = float(present_value)
    x = 0
    inflated = 1
    print("\n\n\n\n")
    while x < n:
        present_value = present_value * (i + 1)
        inflated = inflated * (inflation_rate + 1) 
        x = x + 1
##    print(inflated)
##    print(x)
    retire_income = (retire_income * 12) * inflated
    withdrawl_rate = (i - inflation_rate) * present_value
    q = 1/(i - inflation_rate)
    future_value = retire_income * q
    print("Your income would need to be ",round(retire_income, 2), " per year\n","in order to generate that income you will need to save", round(future_value, 2), "before retirement")
    print("based on your current rate of return your present savings would be worth: ", round(present_value, 2))
    future_value = future_value - present_value
    payment = (i * future_value)/(pow((i + 1), x) - 1)
    print("in order so meet your retirement savings goal you will need to save ", round(payment, 2), "per year")

    print("payment = ", payment)
    print("Present Value = ", present_value) ##by this point in the formula this value is equal to what that value would have grwon to by retirement 
    print("Return on Investment = ", i)
    print("Future Value = ", future_value)
    print("Number of years to retirement = ", n)
    print("x = ", x) ##incrementation variable
    print("newline")

def Amortization():##work in progress
    ##for calculating the cost of a debt over a period of time
    ##add a new output for 
    P = 100000 ##principal value
    r = .04 ##interest rate
    t = 15 ##number of periods (time)
    n = 12 ##payments per period
    monthly_payment = (P * (r/n))/(1 - (1 + (r/n))**((-1) * n * t))
    print(monthly_payment)

def gross_income():
    ##calculates annual income based on hours worked per week and pay per hour.
    ##assumes california overtime rules and is not applicable to all other states
    ##This tool is intended for a job seeker who is trying to compare pay rates between a salaried and hourly position
    hpw = input("How many hours per week are you projected to work: ") #hours per week
    pph = input("how much will you make per hour: ") #value of each hour worked
    hpw = int(hpw)
    pph = int(pph)

    if hpw > 40:
        w = hpw - 40 #temporary holder for overtime hours
        x = w * (pph * 1.5) #temporary holder for value of OT hours
        gai = ((hpw*pph) + x) * 52
    else:
        gai = hpw*pph*52
    print("the gross anual income for the given job would be: ", gai)
