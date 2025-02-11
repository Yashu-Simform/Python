#   Python

##  Dtypes:
-   String:                 x = "hi"
-   Int                     x = 5
-   Float                   x = 5.5
-   List                    x = [1,2,3,3]
-   Dictonary               x = {1:3,"name": "Tomato"}
-   Set                     x = {1,2,3}
-   NoneType                x = None


### False Values:
-   False
-   None
-   Zero of any numeric type
-   Any empty collection '', [], (), {}


### List
-   Can be declared as:
    -   x = []
    -   x = list(any iterable)
    -   Using dictonary to create list:  
        ```
            # Can use any iterables to create list   
            b = {1: 4, 2: 6}
            a = list(b)         # When we pass the dictonary object by default it will consider b.keys() 
            print(a)    ->      [1, 2]
            a = list(b.items())
            a = list(b.values())
        ```
-   When a list object is created a base memory address is assigned to it. Which can grow and shrink in contiguous memory blocks starting from the base address.
-    If you pop or remove the element all elements will shift towards right side to fill the empty block and last block is released.
-   Properties:
    -   Can contain heterogeneous data
    -   Lists are mutable in Python
    -   Dynamic size as vectors in CPP
    -   Stores references in contiguous memory locations of the data inserted.
        ```
        #0      #1      #2
        #12     #23     #34


        #12         #23                                 #34
        "Yashu"     ["Maths", "Computer Science"]       1
        ```

-   List Methods:
    -   append(element):    Append element to last of the list
    -   extend(iterable):   Extends the original list by appending the elements of the given iterable.
    -   insert(index, element): Append the given element at specified index.

    -   remove(single-object):  Removes the first occurence of the specified object from the list
    -   pop(index = (default)-1):   Removes the element from specified index of a list and returns it, the default index is -1.
    -   index(element, start(optional), end (optional)):    It returns the lowest index of the given element, we can specify the start index and end index for searching. It will throw value error if element is not in the list
    -   reverse():  reverses the original list
    -   sort(): Sort the entire original list 
    -   clear():    Removes all the elements from the list
    -   count(element):    It counts the number of occurence of given element with time complexity of O(n)


### Dictonary
-   Can be declared as:
    -   x = {}      ->      type(x)     ->      type='dict'
    -   x = dict()  
    -   x = dict(k1:"v1", k2:"v2", k3:"v3")     ->  Declaring and initializing the dictonary with specified values.

-   Properties:
    -   Stores a key value pair
    -   It internally uses hashing and apply quadratic probation when collisio occurs that is search for the empty slot to store key.
    -   Storage, Update and Retrival: Time complexity - O(1)

-   Dictonary methods:
    -   x.keys()    ->  Returns a list of keys : ['k1', 'k2', 'k3']
    -   x.values()  ->  Returns a list of values: ['v1', 'v2', 'v3']
    -   x.items()   ->  Returns a list of tuple : [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]
    -   x.pop(key, default-msg)  ->  Returns value corresponding to given key if not present returns default-msg. 
    -   clear():    ->      Empties the entire dictonary, takes O(n) time 
    -   copy():     ->      Returns the copies of the dictonary
    -   popitem()   ->      Returns (key, value)

-   Traversing through the dictonary:
    -   ```
            for key in x.keys():
                print("Key is: ", key, " ", " Value is: ", x[key])

            for (key, val) in x.items():
                print("Key is: ", key, " ", " Value is: ", val)
        ```


### Pass Keyword
-   Pass indicates that the line must not be executed by the interpreter


### Garbage collection
-   Python has a support for inbuilt garbage collection using reference counter and cyclic garbage collector
-   reference counter: Maintains the records for number of refernces for a particular variable, if it is 0 then it release out the memory space for that variable
-   del operator in python:
    -   del {specify-object}
    ```
    a = "Yashu"
    del a

    It remove all the references to a and free up the memory.
    ```