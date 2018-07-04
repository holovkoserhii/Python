# Завдання 2.
# Ваша програма має видати безперервну послідовність латинських літер в нижньому регістрі довжиною 1 000 000 символів.
# Послідовність має відповідати вимогам:
# Кожна літера з'являється не частіше 40 000 раз в послідовності;
# Кожна можлива послідовність з двох букв зявляється не частіше 2 000;
# Кожна можлива послідовність з трьох букв з'являється не частіше 100;

import random

def sequence():
    seq = []
    length = 1000000
    double_collection = {}
    double_limit = 2000
    triple_collection = {}
    triple_limit = 100
    
    count = 0
    while count < length:
        generated_letter = chr(random.randrange(1, 27) + 96)
        if count >= 1:
            if double_collection.get("".join(seq[-1:]) + generated_letter) == None:
                double_collection["".join(seq[-1:]) + generated_letter] = 1
            else:
                if double_collection["".join(seq[-1:]) + generated_letter] == double_limit:
                    continue
                else:
                    double_collection["".join(seq[-1:]) + generated_letter] += 1
                
        if count >= 2:
            if triple_collection.get("".join(seq[-2:]) + generated_letter) == None:
                triple_collection["".join(seq[-2:]) + generated_letter] = 1
            else:
                if triple_collection["".join(seq[-2:]) + generated_letter] == triple_limit:
                    continue
                else:
                    triple_collection["".join(seq[-2:]) + generated_letter] += 1
        seq.append(generated_letter)
        count += 1
    print(double_collection)
    print(triple_collection)
    return seq
sequence()