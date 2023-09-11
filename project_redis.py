# import of the libraries
import redis
from tabulate import tabulate  # to print the statistics in a table

r = redis.Redis(host='localhost', port=6379, db=0)  # connection to the redis server


def long_to_short(email):

    ''' this function takes the email of the user and
    create a hash table with the email which will be used to store the number of insertion
    of the user. Then it takes the url from the user and join it with the email to create a key.
    If the key already exists in the database, it means that the url has already been shortened and return the short url.
    If the key doesn't exist, it creates a hash table with the email+url as key and the short url as value. and
    it also creates a hash table with the short url as key and the email+url as value. and it
     increments the number of insertion of the user by 1.'''

    id = 'count ' + 'of insertion for ' + email  # id of the hash table that will store the number of insertion of the user
    r.hsetnx(email, id, 0)  # create a hash table with the email which will be used to store the number of insertion of the user

    url = input(' please enter the url: ')

    key = email + ':' + url

    if r.exists(key):

        print('the present url already shortened and the short url is :', r.hget(key, "short").decode('utf-8'))


    else:
        value = str(hash(url))  # the short url is the hash of the url

        r.hset(key, "short", value)  # create a hash table with the email+url as key and the short url as value

        print('your shortened url is : ', r.hget(key, "short").decode('utf-8'))

        r.hset(value, "clé", key)  # create a hash table with the short url as key and the email+url as value and it will be used to get the long url
        r.hincrby(email, id, 1)  # increment the number of insertion of the user by 1


def short_to_long(email):
    ''' this function takes the email of the user and
    create a hash table with the email which will be used to store the number of request.
    Then it takes the short url from the user and check if it exists in the database.
    If the short url exists, it returns the long url and increment the number of request of the user by 1.
    If the short url doesn't exist, it returns an error message.

    '''

    shortUrl = input('please inter the shortened url that you want long url')  # take the short url from the user

    id_short = 'count of request ' + 'for shorturl ' + shortUrl  # id of the hash table that will store the number of request of the user

    if r.exists(shortUrl):

        key = r.hget(shortUrl, "clé").decode('utf-8').split(':')   # get the long url from the 
        
        print('the long email corresponding to this shortened url is : ', key[1])

        r.hsetnx(email, id_short,0)  # create a hash table with the email which will be used to store the number of request
        
        r.hincrby(email, id_short, 1)  # increment the number of request of the user by 1
    else:
        print('this sortened url has no long email in our database')


def get_stat(email):
    ''' this function takes the email of the user and
    return the number of insertion and the number of request of the user
    '''
    stats = r.hgetall(email)  # get all the hash tables of the user
    list_stat = []  # list that will be used to print the statistics in a table

    for j, k in stats.items():
        list_stat.append((j.decode('utf-8'), k.decode('utf-8')))  # add the statistics in the list
    output = tabulate(list_stat, headers=["statistics", "number"],
                      tablefmt='fancy_grid')  # print the statistics in a table
    return output


if __name__ == '__main__':

    ''' this part of the code is used to test the functions
    '''

    email = input('please enter your email: ')  # take the email of the user

    while True:
        print('1- long to short')
        print('2- short to long')
        print('3- get statistics')
        print('4- exit')
        choice = input('please enter your choice: ')
        if choice == '1':
            long_to_short(email)
        elif choice == '2':
            short_to_long(email)
        elif choice == '3':
            stat = get_stat(email)  # get the statistics of the user
            print(stat)  # print the statistics of the user
        elif choice == '4':
            break
        else:
            print('invalid choice')