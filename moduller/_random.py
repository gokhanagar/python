import random

result = random.random()
result = random.random()
result = random.uniform(1, 10)
result = int(random.uniform(10, 100))

result = random.randint(1, 100)

greeting = 'hello there'
names = ['ali','veli', 'ayse','fatma','ahmet','efe']
result = names[random.randint(0, len(names)-1)]

result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

result = random.sample(liste, 3) # rastgele 3 rakam getirir.
result = random.sample(names, 2)





print(result)







