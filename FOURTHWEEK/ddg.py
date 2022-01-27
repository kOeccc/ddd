x = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}
y = {"google", "microsoft", "apple"}


def xy(a, b):
    xy_set = set(a).union(b)
    return xy_set


c = xy(x, y)
print(c)