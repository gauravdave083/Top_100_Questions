# Error handling in Object-Oriented Programming (OOP) involves managing runtime errors in a structured way, ensuring robust and maintainable code. Here's an overview of how error handling is implemented in OOP:


# 1. Principles of Error Handling in OOP

# Encapsulation: Errors should be handled within the class where they occur.
# Abstraction: Hide the complexity of error handling from the user.
# Inheritance & Polymorphism: Create a hierarchy of error/exception classes to categorize different types of errors.


# 2. Key Concepts in Error Handling

# Exceptions: Objects that encapsulate information about an error.
# Try-Catch Blocks: Mechanism to catch and handle exceptions.
# Throw: Used to signal that an exception has occurred.
# Finally: Ensures cleanup code is executed regardless of exceptions.


class CustomError(Exception):
     """Custom exception class for specific errors."""
     def __init__(self, message):
          self.message = message

class Calculator:
     """A simple calculator class."""
     @staticmethod
     def divide(a, b):
          if b == 0:
               raise CustomError("Division by zero is not allowed!")
          return a / b

try:
     result = Calculator.divide(10, 0)
     print(f"Result: {result}")
except CustomError as e:
     print(f"Error: {e.message}")
finally:
     print("Execution completed.")