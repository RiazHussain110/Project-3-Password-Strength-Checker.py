import string
password = input ("Enter the Password: ")
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
characters = [upper_case, lower_case, special, digits]
length = len(password)
score = 0
with open('common.txt', 'r', encoding='utf-8') as f:  # Specify the encoding
    common = f.read().splitlines()
if password in common:
    print("Your Password is Weak and might be Hacked: ")
    exit()
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1
print(f"Password length is {str(length)}, adding {str(score)} points!")
if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points! ")
if score < 4:
    print(f"The Password is Quite weak! Score {str(score)} / 7")
elif score == 4:
    print(f"The Password is ok! Score: {str(score)} / 7")
elif 4 < score < 6:
    print(f"The Password is pretty good! Score: {str(score)} / 7")
elif score >= 6:
    print(f"The Password is Strong! Score: {str(score)} / 7")
