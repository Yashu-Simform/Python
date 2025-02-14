def decorator_function(original_function):
    def wrapper_function(*args):
        print('Before!')
        ans = original_function(*args)
        print('Sum is: ', ans)
        print('After!')
        pass

    return wrapper_function


@decorator_function
def add(*args):
    print('Adding values!')
    ans = 0
    for x in args:
        ans = ans + x
        pass

    return ans


add(2,3,4,5)


#Decorators with params

def myroute(route):
    def route_decorator(routeFun):
        def wrapper_function():
            print('Route is being checked!')
            print('Route: ', route, ' is valid!')
            routeFun()
            print('Connection established to a host abc.abc.abc.abc!')
            pass
        return wrapper_function
    return route_decorator


@myroute('/Users/uncleroy/userdetails')
def get_user_details():
    print('Making a http call!')

get_user_details()



#decorators using class
class route_up(object):
    def __init__(self, original_fun):
        self.original_fun = original_fun
        pass

    def __call__(self, r):
        def wrapper_fun(r):
            print('Waiting for ack!')
            self.original_fun(r)
            print('Ack received!')

        return wrapper_fun(r)

@route_up
def check_route(r):
    print('Route ', r, 'is checked!')

check_route('/user/ironman/routes/')