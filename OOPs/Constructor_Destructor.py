class Sample:
     def __init__(self):
          print("Initialization")
     def __del__(self):
          print("Clean up")

s1 = Sample()
s1 = None 