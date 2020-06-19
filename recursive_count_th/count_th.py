'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

"""
Pseudocode

General idea:
 - move across the string 1 letter at a time.  
 - base case is we reach the end of the string (word[1] = None)
 - if not at base case, check for "th" then increment by 1



def th_counter(word, count)

Check for base case (word[1] = None)

Check first letter in word. ( letter = word[0] )

    check if next letter is "h".

        if it is, increment counter by 1. Then call the function with inputs of (word[1:], counter)

            note that we could increment by 2. but we'd have to also check if word[2:] exists.

else
    call function on next letter (word[1:], counter)

"""

def count_th(word, count=0):
    
    # base case: reached the end of the word
    if len(word) <= 1:
        return count

    letter = word[0]

    # check for t and h
    if letter == "t" and word[1] == "h":
        
        return count_th(word[1:], count+1)
    
    else:
        return count_th(word[1:], count)

    
if __name__ == '__main__':
    word = "ath 123 th_t_hqhqtth"
    #word = 'th th'
    print(count_th(word))

    print("test")
    print(len(""))
    print("test")