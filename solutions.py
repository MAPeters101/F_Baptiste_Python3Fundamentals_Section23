'''
Question 1
Generate the sample space of rolling two 6-sided dice, numbered '9', '10', 'J', 'Q', 'K', 'A'.

(The sample space is the set of all possible outcomes).

Your result should be a list containing tuples for the outcome of each die, e.g.

[('9', '9'),
 ('9', '10'),
 ('9', 'J'),
 ('9', 'Q'),
 ('9', 'K'),
 ('9', 'A'),
 ('10', '9'),
 ('10', '10'),
 ('10', 'J'),
 ('10', 'Q'),
 ('10', 'K'),
 ('10', 'A'),
 etc
Make this a function that returns the sample space, called make_sample_space.

Solution
The important thing to remember here is that we have "replacement" - i.e. the same number can come up on each die since those are two separate die.

First let's create a tuple that contains all our possible face values for the dice:

face_values = ['9', '10', 'J', 'Q', 'K', 'A']
Our sample space is all the possible combinations of face values from two sets of face values - essentially the "Cartesian product" of the `face_values` (in set terminology).
We could do it this way:

sample_space = []
for v1 in face_values:
    for v2 in face_values:
        sample_space.append((v1, v2))

sample_space
[('9', '9'),
 ('9', '10'),
 ('9', 'J'),
 ('9', 'Q'),
 ('9', 'K'),
 ('9', 'A'),
 ('10', '9'),
 ('10', '10'),
 ('10', 'J'),
 ('10', 'Q'),
 ('10', 'K'),
 ('10', 'A'),
 ('J', '9'),
 ('J', '10'),
 ('J', 'J'),
 ('J', 'Q'),
 ('J', 'K'),
 ('J', 'A'),
 ('Q', '9'),
 ('Q', '10'),
 ('Q', 'J'),
 ('Q', 'Q'),
 ('Q', 'K'),
 ('Q', 'A'),
 ('K', '9'),
 ('K', '10'),
 ('K', 'J'),
 ('K', 'Q'),
 ('K', 'K'),
 ('K', 'A'),
 ('A', '9'),
 ('A', '10'),
 ('A', 'J'),
 ('A', 'Q'),
 ('A', 'K'),
 ('A', 'A')]
But, we can simplify this using comprehensions:

sample_space = [(v1, v2) for v1 in face_values for v2 in face_values]
So let's make this into a function:

def make_sample_space():
    face_values = ['9', '10', 'J', 'Q', 'K', 'A']
    return [(v1, v2) for v1 in face_values for v2 in face_values]
Question 2
Using the sample space you just created above, simulate throwing the two die n times by making random choices from the sample space.

Again, make this into a function that returns the random choices as a list of tuples, with n as a parameter of this function.

Call the function simulate_throws_from_sample_space.

Solution
For this we need to make n independent choices with replacement.

We could just repeatedly choose from the sample space repeatedly:

import random
sample_space = make_sample_space()
[random.choice(sample_space) for _ in range(10)]
[('10', 'K'),
 ('K', '10'),
 ('10', 'A'),
 ('J', 'Q'),
 ('A', 'A'),
 ('J', 'K'),
 ('J', 'K'),
 ('A', 'Q'),
 ('Q', 'Q'),
 ('Q', 'A')]
But it would be simpler to use the fact that choices can return multiple chocies, and it does so with replacement.

random.choices(sample_space, k=10)
[('Q', 'A'),
 ('Q', 'K'),
 ('Q', 'J'),
 ('J', 'J'),
 ('10', '10'),
 ('J', 'A'),
 ('9', '9'),
 ('9', 'A'),
 ('K', 'K'),
 ('J', 'K')]
Let's write this up as a function:

def simulate_throws_from_sample_space(n):
    return random.choices(make_sample_space(), k=n)
simulate_throws_from_sample_space(10)
[('9', 'Q'),
 ('J', '9'),
 ('J', 'Q'),
 ('J', 'K'),
 ('9', 'Q'),
 ('J', '9'),
 ('K', '9'),
 ('J', '10'),
 ('K', 'K'),
 ('Q', 'A')]
Question 3
Your goal here is to implement a function simulate_throws, similar to the one you wrote in Question 2, but without generating a sample space at all - just using the face_values.

Write a function that implements this, and name it simulate_throws.

Solution
The key here is that we can make multiple choices (with replacement) from the same set of values using the choices fucntion that we just used in Question 2.

So each throw can be simulated using:

random.choices(face_values, k=2)
['Q', 'K']
This comes back as a list, which is fine - but we could make it into a tuple if we preferred to keep it consistent with what we had before:

tuple(random.choices(face_values, k=2))
('A', 'A')
We can then asemble a list of these tuples using a simple comprehension:

[tuple(random.choices(face_values, k=2)) for _ in range(10)]
[('J', 'K'),
 ('J', 'J'),
 ('K', '9'),
 ('9', 'J'),
 ('Q', 'A'),
 ('K', 'J'),
 ('K', 'K'),
 ('K', '10'),
 ('K', 'Q'),
 ('10', 'A')]
Let's package that up into a function:

def simulate_throws(n):
    return [tuple(random.choices(face_values, k=2)) for _ in range(n)]
simulate_throws(10)
[('K', '9'),
 ('9', '9'),
 ('J', 'J'),
 ('A', 'K'),
 ('A', 'Q'),
 ('A', 'J'),
 ('10', 'J'),
 ('J', 'K'),
 ('K', 'A'),
 ('9', 'A')]
Question 4
Using both methods of generating throws, build a dictionary that contains the face values as keys, and the number of times they were selected in the simulated throws.

For example, assuming you made 100 throws using one of these methods, your dictionary might look like this:

{
    '9': 39,
    '10': 27,
    'J': 28,
    'Q': 34,
    'K': 36,
    'A': 36
}
Note that your values in the dictionary should add up to 200 is you made one 100 throws.

Write a function that is given the function to use to generate the throws, the number of throws to simulate, and returns this dictionary.

Solution
Let's create a sequence of throws:

sample = simulate_throws(100)
sample
[('9', 'K'),
 ('Q', 'J'),
 ('K', 'K'),
 ('9', 'A'),
 ('K', 'Q'),
 ('J', 'Q'),
 ('K', 'K'),
 ('Q', 'J'),
 ('9', '9'),
 ('9', 'K'),
 ('J', 'K'),
 ('J', 'Q'),
 ('A', 'K'),
 ('A', '10'),
 ('J', '10'),
 ('Q', '9'),
 ('J', '9'),
 ('Q', 'K'),
 ('9', 'Q'),
 ('J', 'K'),
 ('Q', 'K'),
 ('K', 'Q'),
 ('Q', '9'),
 ('A', '9'),
 ('10', '10'),
 ('10', 'Q'),
 ('9', '9'),
 ('J', 'J'),
 ('A', 'K'),
 ('J', 'K'),
 ('A', 'J'),
 ('9', 'A'),
 ('Q', 'A'),
 ('A', 'A'),
 ('J', 'Q'),
 ('J', 'K'),
 ('J', 'Q'),
 ('9', 'K'),
 ('K', 'J'),
 ('Q', 'J'),
 ('9', 'J'),
 ('9', 'K'),
 ('9', 'K'),
 ('Q', '9'),
 ('9', 'Q'),
 ('K', '9'),
 ('K', 'Q'),
 ('J', '10'),
 ('J', '10'),
 ('10', 'Q'),
 ('Q', 'Q'),
 ('J', 'Q'),
 ('Q', '9'),
 ('9', 'K'),
 ('K', 'J'),
 ('K', 'Q'),
 ('10', '9'),
 ('K', '9'),
 ('9', 'A'),
 ('K', '9'),
 ('J', 'A'),
 ('A', 'Q'),
 ('10', '9'),
 ('Q', '9'),
 ('A', '10'),
 ('J', 'K'),
 ('9', 'A'),
 ('9', '9'),
 ('K', 'A'),
 ('10', 'A'),
 ('Q', '10'),
 ('9', '9'),
 ('Q', '9'),
 ('9', 'K'),
 ('10', '10'),
 ('A', '9'),
 ('J', 'A'),
 ('J', '10'),
 ('Q', 'J'),
 ('K', 'A'),
 ('Q', 'A'),
 ('10', '9'),
 ('10', '9'),
 ('Q', 'Q'),
 ('Q', 'J'),
 ('A', 'J'),
 ('K', '10'),
 ('Q', 'J'),
 ('J', '10'),
 ('Q', 'J'),
 ('10', 'A'),
 ('A', 'Q'),
 ('A', 'A'),
 ('10', 'J'),
 ('A', 'J'),
 ('K', '10'),
 ('K', 'J'),
 ('A', 'A'),
 ('9', 'Q'),
 ('10', '10')]
We could try and basically iterate through every row and every item in the row and build up a counter this way:

frequencies = {}
for row in sample:
    for value in row:
        frequencies[value] = frequencies.get(value, 0) + 1
frequencies
{'9': 39, 'K': 34, 'Q': 38, 'J': 35, 'A': 29, '10': 25}
We could however, use the Counter in the collections module instead - recall how it works:

from collections import Counter
dict(Counter(['A', 'J', 'Q', 'A', 'J']))
{'A': 2, 'J': 2, 'Q': 1}
The problem here is that we have a list of tuples - what we atually need is to flatten this list out and just get a list of the individual values.

We can do this easily enough using a comprehension:

values = [e for throw in sample for e in throw]
values
['9',
 'K',
 'Q',
 'J',
 'K',
 'K',
 '9',
 'A',
 'K',
 'Q',
 'J',
 'Q',
 'K',
 'K',
 'Q',
 'J',
 '9',
 '9',
 '9',
 'K',
 'J',
 'K',
 'J',
 'Q',
 'A',
 'K',
 'A',
 '10',
 'J',
 '10',
 'Q',
 '9',
 'J',
 '9',
 'Q',
 'K',
 '9',
 'Q',
 'J',
 'K',
 'Q',
 'K',
 'K',
 'Q',
 'Q',
 '9',
 'A',
 '9',
 '10',
 '10',
 '10',
 'Q',
 '9',
 '9',
 'J',
 'J',
 'A',
 'K',
 'J',
 'K',
 'A',
 'J',
 '9',
 'A',
 'Q',
 'A',
 'A',
 'A',
 'J',
 'Q',
 'J',
 'K',
 'J',
 'Q',
 '9',
 'K',
 'K',
 'J',
 'Q',
 'J',
 '9',
 'J',
 '9',
 'K',
 '9',
 'K',
 'Q',
 '9',
 '9',
 'Q',
 'K',
 '9',
 'K',
 'Q',
 'J',
 '10',
 'J',
 '10',
 '10',
 'Q',
 'Q',
 'Q',
 'J',
 'Q',
 'Q',
 '9',
 '9',
 'K',
 'K',
 'J',
 'K',
 'Q',
 '10',
 '9',
 'K',
 '9',
 '9',
 'A',
 'K',
 '9',
 'J',
 'A',
 'A',
 'Q',
 '10',
 '9',
 'Q',
 '9',
 'A',
 '10',
 'J',
 'K',
 '9',
 'A',
 '9',
 '9',
 'K',
 'A',
 '10',
 'A',
 'Q',
 '10',
 '9',
 '9',
 'Q',
 '9',
 '9',
 'K',
 '10',
 '10',
 'A',
 '9',
 'J',
 'A',
 'J',
 '10',
 'Q',
 'J',
 'K',
 'A',
 'Q',
 'A',
 '10',
 '9',
 '10',
 '9',
 'Q',
 'Q',
 'Q',
 'J',
 'A',
 'J',
 'K',
 '10',
 'Q',
 'J',
 'J',
 '10',
 'Q',
 'J',
 '10',
 'A',
 'A',
 'Q',
 'A',
 'A',
 '10',
 'J',
 'A',
 'J',
 'K',
 '10',
 'K',
 'J',
 'A',
 'A',
 '9',
 'Q',
 '10',
 '10']
And we could pass that to now to a Counter:

dict(Counter(values))
{'9': 39, 'K': 34, 'Q': 38, 'J': 35, 'A': 29, '10': 25}
Let's make a function to encapsulate all this.

def frequency_analysis(func, n):
    sample = func(n)
    values = [e for throw in sample for e in throw]
    return dict(Counter(values))
And now we can use this function with any of our throw generators:

frequency_analysis(simulate_throws_from_sample_space, 100)
{'9': 29, '10': 40, 'A': 31, 'Q': 27, 'J': 40, 'K': 33}
frequency_analysis(simulate_throws, 100)
{'10': 40, 'A': 41, 'Q': 38, 'K': 28, 'J': 29, '9': 24}
Question 5
Write a function that given two arguments a and b returns a random float between a (inclusive) and b (exclusive).

Solution
The standard random float generator returns values in [0, 1).

In our case, we'll need to translate this to start at a:

10 + random.random()
10.497899578597625
And we'll need to make sure our random float is "scaled" to the length of our desired interval (b-a):

If we have an interval such as [10, 20), we want our random number (before adding 10) to it, to be in the range [0, 10). We can do so by multiplying it by 10 - and in general by b-a.

10 + (random.random() * (20 - 10))
15.831057883217674
Let's write this as a function:

def random_float(a=0, b=1):
    return a + random.random() * (b-a)
Ad we can then use it this way:

for _ in range(10):
    print(random_float(12, 14))
12.502599769256468
13.702552234036052
13.195295934440441
12.953629020932048
12.972948766998417
12.431119432030926
13.024268766741276
13.139809905684197
13.899017803710269
13.7863204601448

'''