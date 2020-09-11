import json

my_list = []
firms_with_results, average_profit = {}, {}
cnt, common_profit = 0, 0

with open("text_7.txt", "r", encoding="utf-8") as text_file:
    string_list = text_file.readlines()

for string in string_list:
    profit = int(string.split()[2]) - int(string.split()[3])
    firms_with_results[string.split()[0]] = profit
    if profit > 0:
        cnt += 1
        common_profit += profit
    average_profit["average_profit"] = float(common_profit / cnt)

my_list.append(firms_with_results)
my_list.append(average_profit)
print(my_list)

with open("text_7.json", "w", encoding="utf-8") as json_file:
    json.dump(my_list, json_file, ensure_ascii=False, indent=4)
