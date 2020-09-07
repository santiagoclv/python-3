BaseException
 +-- SystemExit # Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, it causes the interpreter to exit.
 +-- KeyboardInterrupt # Raised when the user interrupts program execution, usually by pressing Ctrl+c.
 +-- GeneratorExit
 +-- Exception # Base class for all exceptions. This catches most exception messages.
      +-- StopIteration # Raised when the next() method of an iterator does not point to any object.
      +-- StopAsyncIteration
      +-- ArithmeticError # Base class for all errors that occur for numeric calculation. You know a math error occurred, but you don’t know the specific error.
      |    +-- FloatingPointError # Raised when a floating point calculation fails.
      |    +-- OverflowError # Raised when a calculation exceeds maximum limit for a numeric type.
      |    +-- ZeroDivisionError
      +-- AssertionError # Raised in case of failure of the Assert statement.
      +-- AttributeError # Raised in case of failure of an attribute reference or assignment.
      +-- BufferError
      +-- EOFError # Raised when there is no input from either the raw_input() or input() function and the end of file is reached.
      +-- ImportError # Raised when an import statement fails
      +-- LookupError # Base class for all lookup errors.
      |    +-- IndexError # Raised when an index is not found in a sequence.
      |    +-- KeyError # Raised when the specified key is not found in the dictionary.
      +-- MemoryError # Raised when a operation runs out of memory.
      +-- NameError # Raised when an identifier is not found in the local or global namespace.
      |    +-- UnboundLocalError # Raised when trying to access a local variable in a function or method but no value has been assigned to it.
      +-- OSError # Raises for operating system related errors.
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError # Raised when a file or directory is requested but doesn’t exist.
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError # Raised when trying to run an operation without the adequate access rights.
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError # Raised when a generated error does not fall into any category.
      |    +-- NotImplementedError # Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.
      |    +-- RecursionError # Raised when the maximum recursion depth has been exceeded.
      +-- SyntaxError # Raised when there is an error in Python syntax.
      |    +-- IndentationError # Raised when indentation is not specified properly.
      |         +-- TabError
      +-- SystemError # Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.
      +-- TypeError # Raised when an operation or function is attempted that is invalid for the specified data type.
      +-- ValueError # Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning


IOError # Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist. Also raised for operating system-related errors.
EnvironmentError # Base class for all exceptions that occur outside the Python environment.



