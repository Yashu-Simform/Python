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


### Dictonary
-   Can be declared as:
    -   x = {}      ->      type(x)     ->      type='dict'
    -   x = dict()  
    -   x = dict(k1:"v1", k2:"v2", k3:"v3")     ->  Declaring and initializing the dictonary with specified values.
-   Stores a key value pair

-   Dictonary methods:
    -   x.keys()    ->  Returns a list of keys : ['k1', 'k2', 'k3']
    -   x.values()  ->  Returns a list of values: ['v1', 'v2', 'v3']
    -   x.items()   ->  Returns a list of tuple : [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]

-   Traversing through the dictonary:
    -   ```
            for key in x.keys():
                print("Key is: ", key, " ", " Value is: ", x[key])

            for (key, val) in x.items():
                print("Key is: ", key, " ", " Value is: ", val)
        ```