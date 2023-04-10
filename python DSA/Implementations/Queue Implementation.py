class Queue:
    lis=[]

    def insert(self):
        ele=input("enter an element to insert")
        self.lis.append(ele)
        print("{} is inserted in the queue".format(ele))

    def delete(self):
        if(len(self.lis)==0):
            print("Queue is empty, deletion not possible")
        else:
            print("The Element deleted is ",self.lis.pop(0))

    def display(self):
        if(len(self.lis)==0):
            print("Queue is empty, display not possible")
        else:
            print("Queue elements are ")
            for i in range(len(self.lis)):
                print(self.lis[i],end=" ")
            print()

    def isEmpty(self):
         if len(self.lis)==0:
             print("True")
         else:
            print("False")

    def front(self):
        if(len(self.lis)==0):
            print("Queue is empty, front not possible")
        else:
            print("front element is ",self.lis[0])
            
    def rear(self):
        if(len(self.lis)==0):
            print("Queue is empty, rear not possible")
        else:
            print("Rear element is ",self.lis[len(self.lis)-1])

queue=Queue()

while True:
     s="""Enter the operation you want to perform
    "1" for insert 
    "2" for delete
    "3" for display front element
    "4" for display rear element
    "5" for display 
    "6" for checking queue empty or not
    "anything" for exit"""
     print(s)
     x=int(input())
     if x==1:
      queue.insert()
     elif x==2:
      queue.delete()
     elif x==3:
      queue.front()
     elif x==4:
      queue.rear()
     elif x==5:
      queue.display()
     elif x==6:
        queue.isEmpty()
     else:
      exit()



    
        
