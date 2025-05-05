def vowels_count (str):
    vowels = "aeiouAEIOU"
    count = 0

    for x in str:
     if x in vowels:
        count +=1 
    
    return count

str = input("Enter your string: ")
print(vowels_count(str))
