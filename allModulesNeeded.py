import time
import datetime
import os
import sys
import random
import json
import requests
import re
import threading
import queue
import logging
import logging.handlers
import urllib3
import urllib
import collections
import itertools
import functools
import operator
import math
import cmath
import decimal
import fractions
import statistics
import copy
import pprint
import pickle
import shelve


"""
# Learning the time module
time.time())  # get the current time in seconds
time.localtime()) # get the current time in a tuple
time.asctime())   # get the current time in a string
time.ctime()) # get the current time in a string
time.gmtime())    # get the current time in a tuple
time.mktime(time.localtime()))    # get the current time in seconds
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))   # get the current time in a string

# Learning the datetime module
datetime.datetime.now())  # get the current date and time
datetime.datetime.now().isoformat())  # get the current date and time in ISO format
datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))    # get the current date and time in a string
datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))   # get the current date and time in a string with microseconds


# Learning the os module
os.getcwd())  # get current working directory
os.listdir()) # list all files and directories in the current working directory
os.path.exists('Assignment41.py'))    # check if the file exists
os.path.isfile('Assignment41.py'))    # check if the file is a file
os.path.isdir('Assignment41.py'))    # check if the file is a directory
os.path.getsize('Assignment41.py'))   # get the size of the file
os.path.getmtime('Assignment41.py'))  # get the last modified time of the file



# Learning the sys module
sys.argv)  # get the command line arguments
sys.platform)  # get the platform
sys.version)  # get the version
sys.path)  # get the path
sys.modules)  # get the modules
sys.stdin)  # get the standard input
sys.stdout)  # get the standard output
sys.stderr)  # get the standard error


# Learning the random module
random.random())  # get a random number between 0 and 1
random.randint(1, 10))    # get a random integer between 1 and 10
random.choice(['apple', 'banana', 'cherry']))    # get a random element from a list
random.choices(['apple', 'banana', 'cherry'], k=2))   # get a list of random elements from a list k times
random.shuffle(['apple', 'banana', 'cherry']))    # shuffle a list in place randomly
random.sample(['apple', 'banana', 'cherry'], k=2))    # get a random sample from a list `k` times
random.uniform(1, 10))    # get a random float between 1 and 10
random.seed(1))   # set the seed
random.getstate())    # get the state
random.setstate(random.getstate()))    # set the state
random.getrandbits(16))   # get a random number with 16 bits
random.randrange(1, 10, 2))   # get a random number between 1 and 10 with a step of 2
random.gauss(0, 1))    # get a random number from a Gaussian distribution
random.normalvariate(0, 1))    # get a random number from a normal distribution
random.lognormvariate(0, 1))    # get a random number from a log-normal distribution
random.expovariate(1))    # get a random number from an exponential distribution
random.betavariate(1, 1))    # get a random number from a beta distribution
random.gammavariate(1, 1))    # get a random number from a gamma distribution
random.triangular(1, 10, 5))    # get a random number from a triangular distribution
random.vonmisesvariate(0, 1))    # get a random number from a von Mises distribution
random.paretovariate(1))    # get a random number from a Pareto distribution
random.weibullvariate(1, 1))    # get a random number from a Weibull distribution



# Learning the json module
json.dumps({'a': 1, 'b': 2}))  # convert a dictionary to a JSON string
json.loads('{"a": 1, "b": 2}'))    # convert a JSON string to a dictionary
json.load(open('data.json')))   # load a JSON file
json.dump({'a': 1, 'b': 2}, open('data.json', 'w')))    # dump a dictionary to a JSON file
json.JSONEncoder().encode({'a': 1, 'b': 2}))    # encode a dictionary to a JSON string
json.JSONDecoder().decode('{"a": 1, "b": 2}'))    # decode a JSON string to a dictionary


# Learning the requests module
requests.get('https://www.google.com').text)    # get the HTML content of a webpage
requests.get('https://www.google.com').json())    # get the JSON content of a webpage
requests.get('https://www.google.com').content)    # get the content of a webpage
requests.get('https://www.google.com').status_code)    # get the status code of a webpage
requests.get('https://www.google.com').headers)    # get the headers of a webpage
requests.get('https://www.google.com').url)    # get the URL of a webpage
requests.get('https://www.google.com').encoding)    # get the encoding of a webpage
requests.get('https://www.google.com').history)    # get the history of a webpage
requests.get('https://www.google.com').cookies)    # get the cookies of a webpage
requests.get('https://www.google.com').elapsed)    # get the elapsed time of a webpage
requests.get('https://www.google.com').request)    # get the request of a webpage
requests.get('https://www.google.com').text)    # get the text of a webpage



# Learning the re module
re.match('a', 'apple'))    # match a string with a pattern at the beginning
re.search('a', 'apple'))    # search a string with a pattern
re.findall('a', 'apple'))    # find all occurrences of a pattern in a string
re.sub('a', 'b', 'apple'))    # substitute a pattern in a string
re.split('a', 'apple'))    # split a string by a pattern
re.compile('a'))    # compile a pattern
re.match('a', 'apple').group())    # get the matched string
re.match('a', 'apple').start())    # get the start position of the matched string
re.match('a', 'apple').end())    # get the end position of the matched string
re.match('a', 'apple').span())    # get the start and end position of the matched string



# Learning the threading module
def worker():   # define a worker function
    'Worker') # print 'Worker'

t = threading.Thread(target=worker)   # create a thread
t.start()   # start the thread
t.join()    # wait for the thread to finish



# Learning the queue module
q = queue.Queue()   # create a queue
q.put(1)    # put an item in the queue
q.put(2)    # put an item in the queue
q.put(3)    # put an item in the queue
q.get())    # get an item from the queue



# Learning the logging module
logging.basicConfig(level=logging.DEBUG)    # set the logging level
logging.debug('This is a debug message')    # log a debug message
logging.info('This is an info message')    # log an info message
logging.warning('This is a warning message')    # log a warning message
logging.error('This is an error message')    # log an error message
logging.critical('This is a critical message')    # log a critical message
logger = logging.getLogger('my_logger')    # create a logger
logger.setLevel(logging.DEBUG)    # set the logging level
logger.debug('This is a debug message')    # log a debug message
logger.info('This is an info message')    # log an info message
logger.warning('This is a warning message')    # log a warning message
logger.error('This is an error message')    # log an error message
logger.critical('This is a critical message')    # log a critical message
handler = logging.handlers.RotatingFileHandler('my_log.log', maxBytes=1024, backupCount=3)    # create a file handler
handler.setLevel(logging.DEBUG)    # set the logging level
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))    # set the formatter
logger.addHandler(handler)    # add the handler to the logger


# Learning the urllib module
urllib.request.urlopen('https://www.google.com').read())    # get the content of a webpage
urllib.request.urlopen('https://www.google.com').geturl())    # get the URL of a webpage
urllib.request.urlopen('https://www.google.com').info())    # get the headers of a webpage
urllib.request.urlopen('https://www.google.com').getcode())    # get the status code of a webpage
urllib.request.urlopen('https://www.google.com').getheaders())    # get the headers of a webpage
urllib.request.urlopen('https://www.google.com').getheader('Content-Type'))    # get a header of a webpage
urllib.request.urlopen('https://www.google.com').getheaders())    # get the headers of a webpage



# Learning the collections module
collections.Counter('apple'))    # count the occurrences of each character in a string
collections.Counter(['apple', 'banana', 'cherry']))    # count the occurrences of each element in a list
collections.Counter({'a': 1, 'b': 2}))    # count the occurrences of each key in a dictionary
collections.Counter(a=1, b=2))    # count the occurrences of each key in a dictionary
collections.Counter('apple') + collections.Counter('banana'))    # add two counters
collections.Counter('apple') - collections.Counter('banana'))    # subtract two counters
collections.Counter('apple') & collections.Counter('banana'))    # get the intersection of two counters
collections.Counter('apple') | collections.Counter('banana'))    # get the union of two counters
collections.Counter('apple').most_common(1))    # get the most common element
collections.Counter('apple').elements())    # get the elements of the counter
collections.Counter('apple').values())    # get the values of the counter
collections.Counter('apple').keys())    # get the keys of the counter
collections.Counter('apple').items())    # get the items of the counter
collections.Counter('apple').update('banana'))    # update the counter
collections.Counter('apple').subtract('banana'))    # subtract the counter
collections.Counter('apple').copy())    # copy the counter
collections.Counter('apple').clear())    # clear the counter
collections.Counter('apple').pop('a'))    # pop an element from the counter
collections.Counter('apple').popitem())    # pop an item from the counter
collections.Counter('apple').setdefault('a', 1))    # set a default value for a key
collections.Counter('apple').fromkeys('apple', 1))    # create a counter from keys and values
collections.Counter('apple').default_factory)    # get the default factory
collections.Counter('apple').default_factory())    # get the default value
collections.Counter('apple').default_factory(1))    # set the default value

collections.ChainMap({'a': 1}, {'b': 2}))    # create a chain map
collections.ChainMap({'a': 1}, {'b': 2})['a'])    # get a value from a chain map
collections.ChainMap({'a': 1}, {'b': 2}).maps)    # get the maps of a chain map
collections.ChainMap({'a': 1}, {'b': 2}).new_child())    # create a new child of a chain map
collections.ChainMap({'a': 1}, {'b': 2}).parents)    # get the parents of a chain map
collections.ChainMap({'a': 1}, {'b': 2}).copy())    # copy a chain map
collections.ChainMap({'a': 1}, {'b': 2}).clear())    # clear a chain map
collections.ChainMap({'a': 1}, {'b': 2}).pop('a'))    # pop a value from a chain map
collections.ChainMap({'a': 1}, {'b': 2}).popitem())    # pop an item from a chain map
collections.ChainMap({'a': 1}, {'b': 2}).setdefault('a', 1))    # set a default value for a key
collections.ChainMap({'a': 1}, {'b': 2}).fromkeys('apple', 1))    # create a chain map from keys and values
collections.ChainMap({'a': 1}, {'b': 2}).default_factory)    # get the default factory
collections.ChainMap({'a': 1}, {'b': 2}).default_factory())    # get the default value
collections.ChainMap({'a': 1}, {'b': 2}).default_factory(1))    # set the default value


collections.deque('apple'))    # create a deque
collections.deque('apple').append('a'))    # append an element to a deque
collections.deque('apple').appendleft('a'))    # append an element to the left of a deque
collections.deque('apple').extend('banana'))    # extend a deque
collections.deque('apple').extendleft('banana'))    # extend a deque to the left
collections.deque('apple').pop())    # pop an element from a deque
collections.deque('apple').popleft())    # pop an element from the left of a deque
collections.deque('apple').remove('a'))    # remove an element from a deque
collections.deque('apple').reverse())    # reverse a deque
collections.deque('apple').rotate(1))    # rotate a deque
collections.deque('apple').clear())    # clear a deque
collections.deque('apple').copy())    # copy a deque
collections.deque('apple').count('a'))    # count the occurrences of an element in a deque
collections.deque('apple').index('a'))    # get the index of an element in a deque

collections.defaultdict(int))    # create a defaultdict
collections.defaultdict(int)['a'])    # get a value from a defaultdict
collections.defaultdict(int).default_factory)    # get the default factory
collections.defaultdict(int).default_factory())    # get the default value
collections.defaultdict(int).default_factory(1))    # set the default value
collections.defaultdict(int).fromkeys('apple', 1))    # create a defaultdict from keys and values
collections.defaultdict(int).copy())    # copy a defaultdict
collections.defaultdict(int).clear())    # clear a defaultdict
collections.defaultdict(int).pop('a'))    # pop a value from a defaultdict
collections.defaultdict(int).popitem())    # pop an item from a defaultdict
collections.defaultdict(int).setdefault('a', 1))    # set a default value for a key

collections.OrderedDict({'a': 1, 'b': 2}))    # create an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2})['a'])    # get a value from an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).move_to_end('a'))    # move an element to the end of an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).popitem(last=False))    # pop an item from an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).popitem(last=True))    # pop an item from an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).copy())    # copy an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).clear())    # clear an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).pop('a'))    # pop a value from an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).setdefault('a', 1))    # set a default value for a key
collections.OrderedDict({'a': 1, 'b': 2}).fromkeys('apple', 1))    # create an ordered dictionary from keys and values
collections.OrderedDict({'a': 1, 'b': 2}).move_to_end('a', last=False))    # move an element to the beginning of an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).move_to_end('a', last=True))    # move an element to the end of an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).popitem(last=False))    # pop an item from the beginning of an ordered dictionary
collections.OrderedDict({'a': 1, 'b': 2}).popitem(last=True))    # pop an item from the end of an ordered dictionary


collections.UserDict({'a': 1, 'b': 2}))    # create a user dictionary
collections.UserDict({'a': 1, 'b': 2})['a'])    # get a value from a user dictionary
collections.UserDict({'a': 1, 'b': 2}).copy())    # copy a user dictionary
collections.UserDict({'a': 1, 'b': 2}).clear())    # clear a user dictionary
collections.UserDict({'a': 1, 'b': 2}).pop('a'))    # pop a value from a user dictionary
collections.UserDict({'a': 1, 'b': 2}).setdefault('a', 1))    # set a default value for a key
collections.UserDict({'a': 1, 'b': 2}).fromkeys('apple', 1))    # create a user dictionary from keys and values
collections.UserDict({'a': 1, 'b': 2}).update({'a': 1, 'b': 2}))    # update a user dictionary
collections.UserDict({'a': 1, 'b': 2}).items())    # get the items of a user dictionary
collections.UserDict({'a': 1, 'b': 2}).keys())    # get the keys of a user dictionary
collections.UserDict({'a': 1, 'b': 2}).values())    # get the values of a user dictionary
collections.UserDict({'a': 1, 'b': 2}).popitem())    # pop an item from a user dictionary
collections.UserDict({'a': 1, 'b': 2}).move_to_end('a'))    # move an element to the end of a user dictionary
collections.UserDict({'a': 1, 'b': 2}).move_to_end('a', last=False))    # move an element to the beginning of a user dictionary
collections.UserDict({'a': 1, 'b': 2}).move_to_end('a', last=True))    # move an element to the end of a user dictionary
collections.UserDict({'a': 1, 'b': 2}).popitem(last=False))    # pop an item from the beginning of a user dictionary
collections.UserDict({'a': 1, 'b': 2}).popitem(last=True))    # pop an item from the end of a user dictionary


collections.UserList([1, 2, 3]))    # create a user list
collections.UserList([1, 2, 3])[0])    # get an element from a user list
collections.UserList([1, 2, 3]).copy())    # copy a user list
collections.UserList([1, 2, 3]).clear())    # clear a user list
collections.UserList([1, 2, 3]).pop(0))    # pop an element from a user list
collections.UserList([1, 2, 3]).append(4))    # append an element to a user list
collections.UserList([1, 2, 3]).extend([4, 5, 6]))    # extend a user list
collections.UserList([1, 2, 3]).insert(0, 4))    # insert an element into a user list
collections.UserList([1, 2, 3]).remove(1))    # remove an element from a user list
collections.UserList([1, 2, 3]).reverse())    # reverse a user list
collections.UserList([1, 2, 3]).sort())    # sort a user list


collections.UserString('apple'))    # create a user string
collections.UserString('apple')[0])    # get a character from a user string
collections.UserString('apple').copy())    # copy a user string
collections.UserString('apple').clear())    # clear a user string
collections.UserString('apple').capitalize())    # capitalize a user string
collections.UserString('apple').casefold())    # casefold a user string
collections.UserString('apple').center(10))    # center a user string
collections.UserString('apple').count('a'))    # count the occurrences of a character in a user string
collections.UserString('apple').encode())    # encode a user string
collections.UserString('apple').endswith('e'))    # check if a user string ends with a character
collections.UserString('apple').expandtabs())    # expand tabs in a user string
collections.UserString('apple').find('a'))    # find a character in a user string
collections.UserString('apple').format())    # format a user string
collections.UserString('apple').format_map({'a': 1}))    # format a user string
collections.UserString('apple').index('a'))    # get the index of a character in a user string
collections.UserString('apple').isalnum())    # check if a user string is alphanumeric
collections.UserString('apple').isalpha())    # check if a user string is alphabetic
collections.UserString('apple').isascii())    # check if a user string is ASCII
collections.UserString('apple').isdecimal())    # check if a user string is decimal
collections.UserString('apple').isdigit())    # check if a user string is a digit
collections.UserString('apple').isidentifier())    # check if a user string is an identifier
collections.UserString('apple').islower())    # check if a user string is lowercase
collections.UserString('apple').isnumeric())    # check if a user string is numeric
collections.UserString('apple').isprintable())    # check if a user string is printable
collections.UserString('apple').isspace())    # check if a user string is a space
collections.UserString('apple').istitle())    # check if a user string is a title
collections.UserString('apple').isupper())    # check if a user string is uppercase
collections.UserString('apple').join('apple'))    # join a user string
collections.UserString('apple').ljust(10))    # left justify a user string
collections.UserString('apple').lower())    # convert a user string to lowercase
collections.UserString('apple').lstrip())    # strip a user string
collections.UserString('apple').partition('a'))    # partition a user string
collections.UserString('apple').replace('a', 'b'))    # replace a character in a user string
collections.UserString('apple').rfind('a'))    # find a character in a user string from the right
collections.UserString('apple').rindex('a'))    # get the index of a character in a user string from the right
collections.UserString('apple').rjust(10))    # right justify a user string
collections.UserString('apple').rpartition('a'))    # partition a user string from the right
collections.UserString('apple').rsplit())    # split a user string from the right
collections.UserString('apple').rstrip())    # strip a user string from the right
collections.UserString('apple').split())    # split a user string
collections.UserString('apple').splitlines())    # split a user string by lines
collections.UserString('apple').startswith('a'))    # check if a user string starts with a character
collections.UserString('apple').strip())    # strip a user string
collections.UserString('apple').swapcase())    # swap case in a user string
collections.UserString('apple').title())    # convert a user string to title case
collections.UserString('apple').translate('a'))    # translate a user string
collections.UserString('apple').upper())    # convert a user string to uppercase
collections.UserString('apple').zfill(10))    # fill a user string with zeros
collections.UserString('apple').format_map({'a': 1}))    # format a user string
collections.UserString('apple').format())    # format a user string




# Learning the itertools module
itertools.count(1))    # create an infinite counter
itertools.cycle('apple'))    # create an infinite cycle
itertools.repeat('apple'))    # create an infinite repeat
itertools.chain('apple', 'banana'))    # chain two iterables
itertools.compress('apple', [1, 0, 1, 0]))    # compress an iterable
itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5]))    # drop elements from an iterable
itertools.filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5]))    # filter elements from an iterable
itertools.islice('apple', 1, 3))    # slice an iterable
itertools.starmap(operator.add, [(1, 2), (3, 4)]))    # map a function to an iterable
itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5]))    # take elements from an iterable
itertools.tee('apple'))    # create two iterators
itertools.zip_longest('apple', 'banana'))    # zip two iterables
itertools.product('apple', 'banana'))    # get the Cartesian product of two iterables
itertools.permutations('apple', 2))    # get the permutations of an iterable
itertools.combinations('apple', 2))    # get the combinations of an iterable
itertools.combinations_with_replacement('apple', 2))    # get the combinations with replacement of an iterable
itertools.groupby('apple'))    # group an iterable
itertools.accumulate('apple'))    # accumulate an iterable
itertools.chain.from_iterable('apple'))    # chain an iterable
itertools.compress('apple', [1, 0, 1, 0]))    # compress an iterable
itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5]))    # drop elements from an iterable
itertools.filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5]))    # filter elements from an iterable

# Learning the functools module
functools.partial(operator.add, 1, 2))    # create a partial function
functools.reduce(operator.add, [1, 2, 3, 4, 5]))    # reduce an iterable
functools.lru_cache(1))    # create an LRU cache
functools.total_ordering)    # create a total ordering
functools.cmp_to_key)    # convert a comparison function to a key function
functools.update_wrapper)    # update the wrapper of a function
functools.wraps)    # wrap a function
functools.singledispatch)    # create a single dispatch
functools.singledispatchmethod)    # create a single dispatch method
functools.cached_property)    # create a cached property

# Learning the operator module
operator.add(1, 2))    # add two numbers
operator.sub(1, 2))    # subtract two numbers
operator.mul(1, 2))    # multiply two numbers
operator.truediv(1, 2))    # divide two numbers
operator.floordiv(1, 2))    # floor divide two numbers
operator.mod(1, 2))    # modulo two numbers
operator.pow(1, 2))    # power two numbers
operator.lt(1, 2))    # less than two numbers
operator.le(1, 2))    # less than or equal two numbers
operator.eq(1, 2))    # equal two numbers
operator.ne(1, 2))    # not equal two numbers
operator.ge(1, 2))    # greater than or equal two numbers
operator.gt(1, 2))    # greater than two numbers
operator.and_(1, 2))    # bitwise and two numbers
operator.or_(1, 2))    # bitwise or two numbers
operator.xor(1, 2))    # bitwise xor two numbers
operator.invert(1))    # bitwise invert a number
operator.lshift(1, 2))    # left shift a number
operator.rshift(1, 2))    # right shift a number
operator.concat('a', 'b'))    # concatenate two strings
operator.contains('a', 'b'))    # check if a string contains another string
operator.countOf('apple', 'a'))    # count the occurrences of a character in a string
operator.indexOf('apple', 'a'))    # get the index of a character in a string
operator.attrgetter('a'))    # get an attribute of an object
operator.itemgetter(1))    # get an item of an object

# Learning the math module
math.ceil(1.5))    # round up a number
math.floor(1.5))    # round down a number
math.trunc(1.5))    # truncate a number
math.copysign(1, -1))    # copy the sign of a number
math.fabs(-1))    # get the absolute value of a number
math.factorial(5))    # get the factorial of a number
math.fmod(1, 2))    # get the modulus of a number
math.frexp(1))    # get the mantissa and exponent of a number
math.fsum([1, 2, 3, 4, 5]))    # sum a list of numbers    
math.isfinite(1))    # check if a number is finite
math.isinf(1))    # check if a number is infinite
math.isnan(1))    # check if a number is NaN
math.modf(1))    # get the fractional and integer parts of a number
math.ldexp(1, 2))    # multiply a number by 2 raised to the power of another number
math.exp(1))    # get the exponential of a number
math.expm1(1))    # get the exponential of a number minus 1
math.log(1))    # get the natural logarithm of a number
math.log1p(1))    # get the natural logarithm of a number plus 1
math.log2(1))    # get the base-2 logarithm of a number
math.log10(1))    # get the base-10 logarithm of a number
math.pow(1, 2))    # raise a number to a power
math.sqrt(1))    # get the square root of a number
math.acos(1))    # get the arccosine of a number
math.asin(1))    # get the arcsine of a number
math.atan(1))    # get the arctangent of a number
math.atan2(1, 2))    # get the arctangent of a number
math.cos(1))    # get the cosine of a number
math.sin(1))    # get the sine of a number
math.tan(1))    # get the tangent of a number
math.degrees(1))    # convert a number from radians to degrees
math.radians(1))    # convert a number from degrees to radians
math.hypot(1, 2))    # get the hypotenuse of a right-angled triangle
math.acosh(1))    # get the inverse hyperbolic cosine of a number
math.asinh(1))    # get the inverse hyperbolic sine of a number
math.atanh(1))    # get the inverse hyperbolic tangent of a number
math.cosh(1))    # get the hyperbolic cosine of a number
math.sinh(1))    # get the hyperbolic sine of a number

# Learning the statistics module
statistics.mean([1, 2, 3, 4, 5]))    # get the mean of a list of numbers
statistics.harmonic_mean([1, 2, 3, 4, 5]))    # get the harmonic mean of a list of numbers
statistics.median([1, 2, 3, 4, 5]))    # get the median of a list of numbers
statistics.median_low([1, 2, 3, 4, 5]))    # get the low median of a list of numbers
statistics.median_high([1, 2, 3, 4, 5]))    # get the high median of a list of numbers
statistics.median_grouped([1, 2, 3, 4, 5]))    # get the grouped median of a list of numbers
statistics.mode([1, 2, 3, 4, 5]))    # get the mode of a list of numbers
statistics.pstdev([1, 2, 3, 4, 5]))    # get the population standard deviation of a list of numbers
statistics.pvariance([1, 2, 3, 4, 5]))    # get the population variance of a list of numbers
statistics.stdev([1, 2, 3, 4, 5]))    # get the sample standard deviation of a list of numbers
statistics.variance([1, 2, 3, 4, 5]))    # get the sample variance of a list of numbers
statistics.quantiles([1, 2, 3, 4, 5]))    # get the quantiles of a list of numbers
statistics.median_absolute_deviation([1, 2, 3, 4, 5]))    # get the median absolute deviation of a list of numbers
statistics.stdev([1, 2, 3, 4, 5]))    # get the standard deviation of a list of numbers
statistics.variance([1, 2, 3, 4, 5]))    # get the variance of a list of numbers
statistics.pstdev([1, 2, 3, 4, 5]))    # get the population standard deviation of a list of numbers
statistics.pvariance([1, 2, 3, 4, 5]))    # get the population variance of a list of numbers
statistics.quantiles([1, 2, 3, 4, 5]))    # get the quantiles of a list of numbers
statistics.median_absolute_deviation([1, 2, 3, 4, 5]))    # get the median absolute deviation of a list of numbers
statistics.median_grouped([1, 2, 3, 4, 5]))    # get the grouped median of a list of numbers
statistics.median_high([1, 2, 3, 4, 5]))    # get the high median of a list of numbers
statistics.median_low([1, 2, 3, 4, 5]))    # get the low median of a list of numbers
statistics.mode([1, 2, 3, 4, 5]))    # get the mode of a list of numbers
statistics.mean([1, 2, 3, 4, 5]))    # get the mean of a list of numbers
statistics.harmonic_mean([1, 2, 3, 4, 5]))    # get the harmonic mean of a list of numbers
statistics.stdev([1, 2, 3, 4, 5]))    # get the sample standard deviation of a list of numbers
statistics.variance([1, 2, 3, 4, 5]))    # get the sample variance of a list of numbers
statistics.pstdev([1, 2, 3, 4, 5]))    # get the population standard deviation of a list of numbers
statistics.pvariance([1, 2, 3, 4, 5]))    # get the population variance of a list of numbers
statistics.quantiles([1, 2, 3, 4, 5]))    # get the quantiles of a list of numbers
statistics.median_absolute_deviation([1, 2, 3, 4, 5]))    # get the median absolute deviation of a list of numbers
statistics.median_grouped([1, 2, 3, 4, 5]))    # get the grouped median of a list of numbers
statistics.median_high([1, 2, 3, 4, 5]))    # get the high median of a list of numbers

# Learning the copy module
copy.copy('apple'))    # create a shallow copy of a string
copy.deepcopy('apple'))    # create a deep copy of a string
copy.copy('apple'))    # create a shallow copy of a string

# Learning the pprint module
pprint.p'apple'))    # pretty print a string
pprint.pformat('apple'))    # format a string
pprint.isreadable('apple'))    # check if a string is readable
pprint.isrecursive('apple'))    # check if a string is recursive
pprint.saferepr('apple'))    # get a safe representation of a string

# Learning the pickle module
pickle.dumps('apple'))    # serialize a string
pickle.loads('apple'))    # deserialize a string
pickle.dump('apple', 'apple.txt'))    # serialize a string to a file
pickle.load('apple.txt'))    # deserialize a string from a file

"""
# Learning the shelve module
shelve.open('apple.txt'))    # open a shelf
shelve.open('apple.txt').close())    # close a shelf
shelve.open('apple.txt').keys())    # get the keys of a shelf
shelve.open('apple.txt').values())    # get the values of a shelf
shelve.open('apple.txt').items())    # get the items of a shelf
shelve.open('apple.txt').get('a'))    # get a value from a shelf
shelve.open('apple.txt').setdefault('a', 1))    # set a default value for a key
shelve.open('apple.txt').update({'a': 1}))    # update a shelf
shelve.open('apple.txt').pop('a'))    # pop a value from a shelf
shelve.open('apple.txt').popitem())    # pop an item from a shelf
shelve.open('apple.txt').clear())    # clear a shelf
shelve.open('apple.txt').copy())    # copy a shelf
shelve.open('apple.txt').sync())    # sync a shelf
shelve.open('apple.txt').writeback())    # write back a shelf




