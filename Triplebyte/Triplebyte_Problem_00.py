from random import random
import bisect


class ProbabilisticGenerator:
    def __init__(self, numbers, probabilities):
        assert sum(probabilities) == 1

        self.numbers = numbers
        self.cum_probs = list()
        current_cum_prob = 0
        for prob in probabilities:
            current_cum_prob += prob
            self.cum_probs.append(current_cum_prob)

    def generate_number(self):
        rand = random()
        index = bisect.bisect_left(self.cum_probs, rand)
        return self.numbers[index]


# Driver code
numbers = [1, 2, 3, 4]
probabilities = [0.1, 0.5, 0.2, 0.2]
pg = ProbabilisticGenerator(numbers, probabilities)

num_exp = 10000
outcomes = dict()
for num in numbers:
    outcomes[num] = 0

for _ in range(num_exp):
    gen_num = pg.generate_number()
    outcomes[gen_num] += 1

for num, probabilities in zip(numbers, probabilities):
    outcomes[num] = round(outcomes[num] / num_exp, 1)
    assert outcomes[num] == probabilities
