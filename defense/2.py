#1 после запятой 2 нуля
def match_ab(s):
    matches = re.findall(r',\s*00(\d+)', s)
    match_count = len(matches) 
    if match_count > 0:
        return f"Match found: {match_count} times"
    else:
        return "Match not found"

text = input()  
result = match_ab(text)  
print(result)
#2
import re

s = "По крайней мере, для некоторых моделей iPhone, "
"а именно моделей Pro, Apple работает над устранением «моноброви», "
"в которой находится аппаратное обеспечение, необходимое для Face ID. "
"«Монобровь» или «челка», как ее еще называют, изначально была спорным дизайнерским решением. "
"налитик Apple Минг-Чи Куо заявил в марте 2021 года, что в моделях iPhone 2022 года ее не будет, "
"а вместо нее будет дизайн в стиле дырокола, который был популярен на многих телефонах Android."
"iPhone iPhone iPhone iPhone"

count = 0

result = re.findall("iPhone",s)

for i in result:
    count += 1
    
print(count)

#3 числа закончиваются на 0
import re

def count_values(s):
    match_generator = (1 for match in re.finditer(r'\b\d*0\b', s))

    return sum(match_generator)

text = input("Enter numbers: ") 
match_count = count_values(text)
print(f"Count of values: {match_count}")