#step-1:get farenheit value
farenheit=float(input("Enter farenheit temperature: "))
#step-2:evaluate celsius value
celsius=(farenheit-32)*5/9
celsius=round(celsius,2)
#step-3:print the result
print(farenheit,"degrees farenheit","is equal to",celsius,"degrees celsius")