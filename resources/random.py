import pulumi_random as random

def random_string():
    op = random.RandomString("random_string",
                             length=10,
                             special="false")
    return  op
