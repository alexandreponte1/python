import random
import json
import os

count  = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip]

for identifier in range(count): 
    amount = random.uniform(1.0, 1000)
    content = 