import datetime, os, random
from letter_patterns import letter_patterns

#!!!!!!!!! WARNING !!!!!!!!
#!!!!!!!!! the first day of your chosen year must be Wednesday at the latest !!!!!!!!
year = 2017


start_date = datetime.date(year, 1, 1)

def calculate_commit_dates(text):
    text = text.upper()
    commit_dates = []
    
    for i, char in enumerate(text):
        if char in letter_patterns:
            pattern = letter_patterns[char]
            for row in range(5):
                for col in range(5):
                    if pattern[row][col] == "#":
                        week_offset = i * 6 + col  # We leave 1 column space between letters
                        day_offset = row
                        commit_date = start_date + datetime.timedelta(weeks=week_offset, days=day_offset)
                        commit_dates.append(commit_date)
    
    return sorted(commit_dates)


# YOUR TEXT HERE
text = "NS.CPP"
# YOUR TEXT HERE

dates = calculate_commit_dates(text)

f = open("dates.txt", "w")
for date in dates:
    print(date)
    
    f.write(str(date)+'\n')
f.close()


j = open('dates.txt','r')
for date in j:
    a=0
    d = str(a) + 'days ago'
    with open('test.txt' , 'a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit -m 1 --date=" '+date+'"')
    a+=1
os.system('git push -u origin main -f')
