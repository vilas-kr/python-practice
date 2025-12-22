def vowel_frequency(s) :
    '''
    Parameter
    ---------
    s : String
        a sentance
    
    Returns
    -------
    count : int
        Frequency of vowels in the sentance
    '''
    s = s.lower()
    count = 0
    for i in s:
        if i in 'aeiou':
            count += 1
    return count

print(vowel_frequency(input("Enter a sentance : ")))