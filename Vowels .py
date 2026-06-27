def analyze_string(text):
    vowels = "aeiou AEIOU"
    vowels_count = 0

    #loop for counting vowels
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    print("original string :",text)
    print("Total Character :",len(text))
    print("total vowels :",vowel_count)

    #main program
    String = input("Enter a string:")
    analyze_string(String)
