#######################
# EXAMPLE: combinations of print and return
#######################
def is_even_with_return( i ):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

is_even_with_return(3)
print(is_even_with_return(3))

def is_even_without_return(i):
    """
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    remainder = i % 2

# is_even_without_return(3)
print(is_even_without_return(3))

# Simple is_even function definition
def is_even( i ):
    """
    Input: i, a positive int
    Returns 1 if i is even, otherwise 0
    """
    remainder = i % 2
    return 1-remainder

# Use the is_even function later on in the code
print("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")

#########################
## EXAMPLE: applying functions to repeat same task many times
#########################
def bisection_cuberoot_approx(x, epsilon):
    """
    Input: x, an integer and epsilon, floating number
    Uses bisection to approximate the cube root of x to within epsilon
    Returns: a float approximating the cube root of x
    """
    low = 0.0
    high = x
    guess = (high + low)/2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

x = 1
while x <= 10000:
    approx = bisection_cuberoot_approx(x, 0.01)
    print(approx, "is close to cube root of", x)
    x *= 10


#########################
## EXAMPLE: functions as arguments
#########################
def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a))


########################
# EXAMPLE: returning function objects
########################
def f():
  def x(a, b):
    return a+b
  return x

# the first part, f(), returns a function object
# then apply that function with parameters 3 and 4
a = f()
print(a)
val = a(3,4)
print(val)


########################
# EXAMPLE: shows accessing variables outside scope
########################
def f(y):
  x = 1
  x += 1
  print(x)

x = 5
f(x)
print(x)

def g(y):
  print(x)
  print(x+1)

x = 5
g(x)
print(x)

def h(y):
  # pass
  global x
  x += 1 #leads to an error without line `global x` inside h
  print('in h, x =', x)

x = 5
print('in global scope, before h, x =', x)
h(x)
print('in global scope, after h, x =', x)


#########################
## EXAMPLE: hader scope example from slides
#########################
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)


#########################
# EXAMPLE: complicated scope, test yourself!
########################
def f(x):
  x = x + 1
  print('in f(x): x =', x)
  return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

def g(x):
  x = x + 1
  print('in g(x): x = 4? ', x)

  def h(x):
    x = x + 1
    print("in h(x): x = 5?", x)

  h(x)
  return x # 4?

x = 3
z = g(x)
print('in main program scope: x = 3? ', x)
print('in main program scope: z = 4?', z)