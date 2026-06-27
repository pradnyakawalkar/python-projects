def analyze_string(text):
    vowels = "aeiouAEIOU"
    vowels_count = 0

    #loop for counting vowels
    for ch in text:
        if ch in vowels:
            vowels_count += 1
    print("original string :",text)
    print("Total Character :",len(text))
    print("total vowels :",vowels_count)

    #main program
String = input("Enter a string:")
analyze_string(String)
