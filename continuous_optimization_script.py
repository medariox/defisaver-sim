
from modules.readConfig import readConfig
from modules.optimize import optimizeRatioContinuous

underlying_return, time_period, volatility, borrow_rate = readConfig("Continuous limit optimization parameters")

optimal_ratio, optimal_return = optimizeRatioContinuous(underlying_return, time_period, volatility, borrow_rate)

print("Optimal leverage ratio = ", optimal_ratio)
print("Optimal return = ", optimal_return)
print("Relative performance to underlying = ", optimal_return/underlying_return)
if optimal_return/underlying_return > 1:
    print("BETTER THAN HOLDING \n")
else:
    print("WORSE THAN HOLDING \n")
