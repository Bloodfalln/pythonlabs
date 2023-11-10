
start = 30
end = 60


count_multiples_of_three = 0


for number in range(start, end + 1):
    
    if number % 3 == 0:
      
        print(number)
      
        count_multiples_of_three += 1


print("Кількість цілих чисел, кратних трьом в діапазоні від", start, "до", end, "дорівнює", count_multiples_of_three)