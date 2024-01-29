#Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.
"""for index in range(len(meyveler)):

    print("{}. indexte bulunan meyve: {}".format(index,meyveler[index]))"""


meyveler = ["elma", "armut", "muz", "çilek", "ayva", "kiraz", "karpuz"]

for i,j in enumerate(meyveler):
    print(f"{i}. indexte bulunan meyve:{j}")
