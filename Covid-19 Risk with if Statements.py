age=(input('Are you a cigarette addict older than 75 years old? (Yes/No): ')).strip().capitalize()=='Yes' and True
chronic=(input('Do you have a severe chronic disease? (Yes/No): ')).strip().capitalize()=='Yes' and True
immune=(input('Is your immune system too weak? (Yes/No): ')).strip().capitalize()=='Yes' and True
if age or chronic or immune:
    print('You are in risky group!')
else:
    print('You are not in risky group.')