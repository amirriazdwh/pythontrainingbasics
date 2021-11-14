iterable_value = 'FacingIssuesOnIT'
iterable_obj = iter(iterable_value)

while True:
   try:
   # Iterate by calling next
      item = next(iterable_obj)
      print(item)
   except StopIteration as err:
      print('Stop Iteration occured', err)
      break


   class PrintNumber:
      def __init__(self, max):
         self.max = max

      # an iter always return self
      def __iter__(self):
         self.num = 0
         return self

      # a next always return self.value
      def __next__(self):
         if (self.num >= self.max):
            raise StopIteration
         self.num += 1
         return self.num


printNum = PrintNumber(3)
iterable_obj1 = iter(printNum)

while True:
   try:
   # Iterate by calling next
      item = next(iterable_obj1)
      print(item)
   except StopIteration as err:
      print('Stop Iteration occured', err)
      break
   except RuntimeError as err:
      print("The value returned from the StopIteration statement is:", err)


