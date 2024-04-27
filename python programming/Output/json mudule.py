# Java script  json
import json
data = '{"var1:" harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

data2 = {
    "company name": "software engineer",
    "cars": ['BMW', 'audi', 'bbt', 'ferrari'],
    "fridge": ('Drunk', 540),
    "is bad": 'True'
}
jscomp = json.dumps(data2)
print(jscomp)
