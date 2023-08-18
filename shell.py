# sys allows us to look into system memory, among other things
import sys

list_comprehension = [n for n in range(100000)]
generator_expression = (n for n in range(100000))

# Returns the size of an object in bytes
sys.getsizeof(list_comprehension)
# 824456
sys.getsizeof(generator_expression)
# 112