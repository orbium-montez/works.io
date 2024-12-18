is_sunny = True 
temperature = 75 
is_perfect_day = is_sunny and (70 <= temperature <= 80)

if is_perfect_day:
    print("Let's go outside!")
elif is_sunny: 
    print("It's sunny but temperature isn't ideal")
else: print("Stay inside")

