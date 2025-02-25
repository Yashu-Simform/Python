# Solid Principles

-   S: Single Responsibility Principle
-   O: Open/Close Principle
-   L: Liskov's Substitution Principle
-   I: Interface Segregation Principle
-   D: 

### S: Single Responsibility Principle
-   Any class or module should have a single responsibility. It should have a single reason to change.

### O: Open / Close Principle
-   Any class should be open to extend and closed to modification. We should be able to add new things to class without affecting the existing ones.

### L: Liskov's Substitution Principle
-   Let's say if a class 'Developer' is a subclass of class 'Employee' then throughout the program objects of class 'Developer' should be able to replace the objects of class 'Employee'

-   Pro Tip:
    -   Do not make preconditions more strict in subclass than in superclass.
    -   Do not make postconditions more weaker in subclass than in superclass.
    -   E.g. If a super class checks that a dictonary must have key "session_id", then we should not make it more strict in subclass by putting further condition like dictonary must have "class_id"
    -   If a superclass checks whether response returned must have "result" key, then we should not omit this in sub class.

### I: Interface Segregation Principle
-   We should make an interface or abstract class having as small as possible, only methods which needs to be implemented all together should be put together in to a single interface.
-   Divide an interface into multiple interfaces if there exists some methods which is not required to get implemented in any of the subclass which is going to use inherit this (interface or abstract class).


### D: Dependency Inversion
-   High Level modules should not depend on low-level modules, it should only depend on abstraction or interface.
-   Abstraction should not depend on details(or high-level / low-level modules)
-   ```
        # Abstraction
        class Work:
            def do_work(self):
                pass

        # High-level module
        class Programmer:
            def __init__(self, work: Work):
                self.work = work

            def work_on_project(self):
                self.work.do_work()

        # Low-level module
        class Coding(Work):
            def do_work(self):
                print("Coding...")

        # Use dependency inversion
        coding_task = Coding()
        programmer = Programmer(coding_task)
        programmer.work_on_project() # Output: Coding...

    ```