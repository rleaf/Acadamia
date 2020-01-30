# Ryan Lin | Comp Sci 101 | 9/17/19


#answer = float(input('Enter how many shares Ali purchased: '))
answer = float(input('Enter how many shares Ali purchased: '))
#answer = 1000


print('The amount of commission Ali paid to his broker: ${:5,.2f}'.format(answer * 30 * .025))
print('The net amount of money Ali paid for his stock including commission: ${:5,.2f}'.format((answer * 30) + (answer * 30 * .025)))
print('The amount of commission Ali paid his broker when he sold the stock: ${:5,.2f}'.format(answer * .025 * 45))
print('The net amount that Ali received by selling the stock including the cost of commission: ${:5,.2f}'.format(45 * answer - (answer * .025 * 45)))
print('Ali profit made: ${:5,.2f}'.format(45 * answer - (answer * .025 * 45) - ((answer * 30) + (answer * 30 * .025))))
