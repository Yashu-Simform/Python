#   Python
-   Try to import this

##  Dtypes:
-   String:                 x = "hi"
-   Int                     x = 5
-   Float                   x = 5.5
-   List                    x = [1,2,3,3]
-   Dictonary               x = {1:3,"name": "Tomato"}
-   Set                     x = {1,2,3}
-   NoneType                x = None


### Behaviour of ++ and -- in python
-   ++ and -- is not treated as increment or decrement operators in python as it does in C++.

-   In python ++ and -- is treated as:
    ```
        a = 7
        ++a  =>  +(+a)  =>  +a
        --a  =>  -(-a)  =>  +a


        7 +++++ ++ + + a  =>    7+a         =>  14
        7 -- a            =>    7 + 7       =>  14
        7 --- a           =>    7 - (+7)    =>  7 - 7  => 0
        7 --- -- - - - a  =>    7 + 7       =>  14
    ```

### Python Functions
-   reversed(): Take any iterable and reversed it and returns the iteratorfor this reveresed object.

    ![reversed function](./Outputs/reversed_function.png)

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


### Ordered Dictonary from collections
-   It has all properties of dictonary in addition to one quality of preserving the insertion order of elements.
-   If you change the value of any key, there will be no change in its position.

```
    from collections import OrderedDict

    od1= OrderedDict([(3: "Three"), (2: "Two"), (1: "One")])

    od2 = OrderedDict()
    od2[1] = "T-One"
    od2[3] = "T-Three"
    od2[2] = "T-Two"

    print(od1 == od2)   =>  Output: False
```

-   Reverse the order of OrderedDict:
    ```
        od1 = OrderedDict(reversed(list(od1.items())))
    ```

-   popitem(last=True)   =>  remove the last (key-value) and returns it. Or specify an index to remove specific item.


### Functions
-   Functions are the block of statements which will executed when called.
-   Instead of writting a code again and again we declare function to reuse it.

-   Parameters: The values that a function expect as declared in its definetion are called parameters (params).
-   Arguments: The actual values passed to functions when called are called arguments.

-   #### Docstring
    -   We can show information about the function in Docstring.
    -   Docstring will be highlighted when hover over function name
    ```
        def sayHello():
            """
            This function will print hello when called.
            """

            print('Hello')
    ```

-   #### Type-Hint:  
    -   A data type is specified as a hint which is just for understanding purpose.
    -   It is totally ignored by the python interpreter and will not be executed.
    -   You can specify type-hint using ':' operator
    ```
        a: int = 5
        b: str = 'String is there.'

        def func(name: str, age: int) -> int:
            print(name, age, sep='\n')
            return 0

    ``` 
    -   We can use <b>mypy</b> for static type checking in python:
        ```
            #Install
            pip install mypy

            #Static type checking
            mypy myfile.py
        ```
        -   The mypy will check the type hints and give error message if any, these error messages are just showing type errors as per type-hints.
        -   Our program will run even if the mypy has showed error messages as type-hints are just like comments when interpreted by python interpreter.

-   Python supports 4 types of arguments:
    -   Default arguments:
        -   Rule: There should be no any non-default argument followed by default argument.
        ```
            def func(a, b=10):
                print(a,b)


            func(5,5)   =>  output: 5 5
            func(5)     =>  output: 5 10
        ```

    -   Keyword arguments:
        -   Arguments passed with parametric names
        -   Used when order of parameters are not known.
        ```
            def func(fname, lname):
                print("Fname: ", fname," Lname: ", lname)

            func(lname='Ranparia', fname='Yashu')   =>  Output: Yashu Ranparia
        ```

    -   Positional arguments:
        -   When values are passed without parametric names they are considered as positional arguments.
        ```
            def func(fname, lname):
                print("Fname: ", fname," Lname: ", lname)

            func('Yashu', 'Ranparia')   =>  Output: Yashu Ranparia
        ```

    -   Arbitary arguments:
        -   We can pass a variable number of arguments while calling a function.
        ```
            def func(*args):
                for arg in args:
                    print(arg,end=' ')

            func('Yashu', 'Ranparia')   =>  Output: Yashu Ranparia


            def func(**kwargs):
                print(kwargs)

            func(name="Yashu", cmp="Simform")   =>  Output: {name: "Yashu", cmp: "Simform"}
        ```

### Pass Keyword
-   Pass indicates that the line must not be executed by the interpreter


### Packing and Unpacking
-   Here * and ** is used  for packing and unpacking tuples and dictonary.
-   A * operator is used for sequence and ** is used for key-value pairs

-   Packing: When we do not know how many arguments will be passed to function, we can use packing to pack any number of arguments into a single variable.
```
    def hobbies(*args);
        for hobby in args:
            print(hobby)

    hobbies("Cricket", "CP", "Automation")    <-   These arguments are packed as tuple named args 
```  


-   Unpacking: When a function expects a number of arguments (say 5) and I have already a list or a tuple of these arguments I can pass the unpacked list or tuple.
```
    def details(fname, lname, city, state, college):
        print('Anything')

    
    # I am getting user input as list
    user_detail = ["Yashu", "Ranparia", "Admedabad", "Gujarat", "CHARUSAT"]

    details(*user_details)  <-  Unpacking of a list
```

-   Unpacking a dictonary:
    ```
        def details(fname, lname, city, state, college):
            print(fname, lname, city, state, college, sep=' ')

        # I have user input as dictonary
        user_input = {"fname": "Yashu", "lname": "Ranparia", "city": "Ahmedabad", "State": "Gujarat", "college": "CHRUSAT"}

        details(*user_details)  =>  Output: fname lname city State college

        details(**user_details) =>  Output: Yashu Ranparia Ahmedabad Gujarat CHARUSAT
    ```

    -   ** will pass the values of the dictonary.
    -   A * will only pass the keys of dictonary.

-   *args expects comma seperated objects
-   **kwargs used specifically for named arguments, where it packs the named arguments in form of key:value pair i.e. dictonary.

-   **kwargs usage: <! Passed Arguments must be named !>
    ```
        def details(**kwargs):
            for key,value in kwargs.items():
                print(key, ' ', value)


        details(name="Yashu", cmp="Simform", hobbies=["Cricket", "CP", "Automation"])
    ```

### Print function 
```
    print("Hello", "Yashu", sep=" ", end=". ", file = sys.stdout (default), flush = False (default))
    print("How are you?")
    Output: Hello Yashu. How are you?
```
-   Objects: Strings or other objects passed as arguments to display as output.
-   sep:    The specified string will used to seperate the given objects.
-   end:    The print statement will end with the specified string in end.
-   file:   Print statement outputs by default in sys.stdout that is system console. But if we specify the file object in writing mode it will output it in to specified file.
-   flush:  By default false, if True it immediately flushes the buffer.

-   Buffering & Flushing:
    -   Print() will push the output string to buffer.
    -   The buffer will flush when:
        -   Buffer is full
        -   Newline ('\n') is encountered
        -   program ends
        -   flush = true

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


### Standard Libraries
-   Libraries provided by the python itself as builtin support.

    #### math
    -   Provides all mathematical functions

    #### webbrowser
    -   Provides functions to interact with browsers.
    -   Can go on a specific URl, open new window of browser, etc.



### OOP in Python
-   Class:  A relatable object which has its own characteristics (attributes) and behaviour (Methods).

-   In programming a class declaration is just a blueprint for an object instance.

-   Attributes: Variables associated with the class are known as attributes.
-   Methods: Functions associated with the class are known as methods.

-   Class Variable and Instance Variable
    -   Class Variables:    Variables declared outside the methods of the class and shared among all the instances of the class.
    -   Instance Variable:  Variables declared within methods or using self param are Instance Variables. Each instance has its own copy of these variables.

    ```
        class Employee:
            emp_num = 0     #Class Variable | Shared among all instances

            def __init__(self, fname):
                self.fname = fname      #Instance Variable
                self.salary = salary    #Instance Variable
                self.initLeaves()

            def initLeaves(self):
                self.leaves = 0     #Instance Variable
    ```

    -   Class variables can be accessed as:
    ```
        Employee.emp_num = 5    #willl change the value for all instances
    ```

-   Example: 
```

class Employee:     #Declaration of Class named Employee
    
    #Class Variables/Attribute
    emp_num = 0

    #constructor or init method
    def __init__(self, fname, lname, salary, joining_date):
        
        # Attributes
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.joining_date = joining_date
        pass


    # Methods
    def get_full_name(self):
        return self.fname + ' ' + self.lname
    
```

-   #### Instance-Methods | Class-Methods | Static-Methods
    -   <b>Instance methods</b>: The normal methods of the class where an instance reference is passed when any instance try to access it.  

    -   <b>Class-Methods</b>: The methods declared using @classmethod decorator and it takes class as param instead of instance reference. You can call it using any insatnce but still a class is passed as param not an instance reference.
        -   ![alt text](Outputs/classmethod.png)
        -   Classmethod as an alternate constructor:
            -   Classmethods can be used as alternate constructor when you want to initiallize an object with some different format of argumetns than original constructor.
            -   ![alt text](Outputs/classmethod_as_alt_constructor.png)
                ![alt text](Outputs/usage_class_method_alt_const.png)


    -   <b>Static Methods</b>: The methods which do not require and use instance reference or class reference, and