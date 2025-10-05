# Lab Assignment number 2
print("Lab Assignment number 2")
print()
print("Problem 1: CatDog or DogCat")
x = "dog"
y = "cat"
print(x + y)
print("the " + x + " chases the " + y)
print(x * 4)                                                #realized on this one a number is highlighted in turquoise when it's being used in a function
print()                                                     #I would like to know if there is another way to do this.  I thought I had seen a different way but couldn't find it later
print("Problem 2: Valid Variables")
_player = "Var1"
print(_player)
print('168hrs = "Var2"')                                     #variable can't start with a number
print('Returns: "SyntaxError: invalid decimal literal"')
MEDIA_54 = "Var3"
print(MEDIA_54)
print('currencyIn$ = "Var4"')                                #the $ symbol is unusable naming convention
print('Returns: "SyntaxError: invalid syntax"')
print()
print("Problem 3: Most Appropriate")
print("A: Integer if we are just referring to a number as in 12")                   #Didn't fully know if you wanted date or int but I figured int since it was a single number
print("B: Float because its a decimal number")
print("C: Float because minimum wage requires a decimal for change")
print("D: String because a name is just a word")
print()
print("Problem 4: Differences between int and float")
print("Int short for integer is a whole number positive or negative")
print("Float is a decimal number positive or negative")
print("Int is more precise, while float allows for fractional values")                #fractional values have a maximum amount while int is only limited by memory. Wasn't sure if this was valid because I found conflicting information about this.
print("Int requires less memory, usually 2 bytes, while float requires 4 bytes")      #I also found that int was faster at one point in time but now with FPU float can be just as fast
print()
print("Problem 5: x=8 y=2")
x = 8
y = 2
print(f"A: x+y*3={x+y*3}")
print(f"B: (x+y)*3={x+y*3}")
print(f"C: x**y={x**y}")
print(f"D: x%y={x%y}")
print(f"E: x/12.0={x/12.0}")
print(f"F: x//6={x//6}")
print()
print("Problem 6: x = 4.66")
x = 4.66
print(f"A: round(x)={round(x)}")
print(f"B: int(x)={int(x)}")
print()
print("Problem 7: Rounding to nearest int")
print("By using the round() function python will round to the nearest whole number")
print("By using other functions like math.floor or math.ceil you can control which direction you want it to round")
print()
print("Problem 8: x = 55 use an assignment statement to increment x by 1")
x = 55
x += 1
print(f"x={x}")