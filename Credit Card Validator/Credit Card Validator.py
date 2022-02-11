# Take the credit card number
card_number = input('PLEASE ENTER YOUR CREDIT CARD NUMBER:\n >>>')
temp = card_number.split()


# Check if the card number is 16 digits long
while len(card_number)!=16:
    card_number = input('THE CREDIT CARD NUMBER SHOULD BE 16 DIGITS LONG.\
                        \nPLEASE ENTER YOUR CREDIT CARD NUMBER AGAIN:\n >>>')
    
    
# Check that credit card number does not contain any alphabets
for temp in card_number:
    if any(char.isalpha() for char in temp):
        card_number = input('THE CREDIT CARD NUMBER CAN NOT CONTAIN ALPHABETS.\
                            \nPLEASE ENTER YOUR CREDIT CARD NUMBER AGAIN:\n >>>')
    
    
# Applying Luhn's Algorithm
#1. Take every alternate digit starting from penultimate position and multipy it by 2
if len(card_number)==16:
    required_digits = [2*(int(i)) for i in card_number[-2::-2]]
    
    
#2. Calculate sum of all indivisual digits
required_digits_str = ''.join([str(elem) for elem in required_digits])
total_1 = sum([int(i) for i in required_digits_str])
    
#3. Calculate sum of every alternate digit starting from last position
remaining_digits = [int(i) for i in card_number[::-2]]
total_2 = sum(remaining_digits)


#4. Add both the totals
total = total_1+total_2


#5. If the total is divisible by 10, card is valid!!!
if total%10 == 0:
    print('YOUR CREDIT CARD IS VALID!')
else:
    print('SORRY, YOUR CREDIT CARD IS INVALID.')