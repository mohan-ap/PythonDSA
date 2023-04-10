class Stack:
    lis=[]

    def push(self):
        ele=input("Enter an element to push ")
        self.lis.append(ele)
        print("{} pushed on to the stack".format(ele))

    def pop(self):
        if len(self.lis)==0:
            print("stack is empty, pop not possible")
        else:
            print("pop element is ",self.lis.pop())

    def peek(self):
        if len(self.lis)==0:
             print("stack is empty, peek not possible")
        else:
            print("peek element is")
            print(self.lis[len(self.lis)-1])

    def isEmpty(self):
        if len(self.lis)==0:
            print("True")
        else:
            print("False")
    def display(self):
         if len(self.lis)==0:
             print("stack is empty, display not possible")
         else:
            print("Stack elements are")
            for i in range(len(self.lis)):
                print(self.lis[i], end=" ")
            print()

stack=Stack()

while True:
     s="""Enter the operation you want to perform
    "1" for push 
    "2" for pop
    "3" for peek
    "4" for display 
    "5" for checking queue empty or not
    "anything" for exit"""
     print(s)
     x=int(input())
     if x==1:
      stack.push()
     elif x==2:
      stack.pop()
     elif x==3:
      stack.peek()
     elif x==4:
      stack.display()
     elif x==5:
        stack.isEmpty()
     else:
      exit()




    


        
