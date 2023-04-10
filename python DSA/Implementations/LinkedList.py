class Node():
      def __init__(self,data):
          self.data=data
          self.link=None

class LinkedList():
    head=None
   
    def insertRear(self):
        x=input("enter a data to insert")
        newNode=Node(x)
        if self.head==None:
             self.head=newNode
        else:
             temp=self.head
             while temp.link !=None:
                  temp=temp.link
             temp.link=newNode
    
    def insertFront(self):
         x=input("enter a data to insert")
         newnode=Node(x)
         if self.head==None:
              self.head=newnode
         else:
              newnode.link=self.head
              self.head=newnode

    def deleteRear(self):
         if self.head==None:
              print("Linked List empty, Deletion not possible")
         elif self.head.link==None:
              print("Deleted data is",self.head.data)
              self.head=None
         else:
              temp=self.head
              while temp.link.link != None:
                   temp=temp.link
              print("Deleted data is",temp.link.data)
              temp.link=None

    def deletefront(self):
         if self.head==None:
              print("Linked List empty, Deletion not possible")
         elif self.head.link==None:
              print("Deleted data is",self.head.data)
              self.head=None
         else:
            print("Deleted element is ",self.head.data)
            self.head=self.head.link
          
    def display(self):
         if self.head==None:
              print("Linked list is empty, display not possible")
         elif self.head.link==None:
              print(self.head.data)
         else:
              temp=self.head
              while temp !=None:
                   print(temp.data,end=" ")
                   temp=temp.link
              print()

ll=LinkedList()

while True:
     s="""Enter the operation you want to perform
     "1" for insert front
     "2" for insert rear
     "3" for delete front
     "4" for delete rear
     "5" for display 
     "anything" for exit"""
     print(s)
     x=int(input())
     if x==1:
      ll.insertFront()
     elif x==2:
      ll.insertRear()
     elif x==3:
      ll.deletefront()
     elif x==4:
      ll.deleteRear()
     elif x==5:
      ll.display()
     else:
      exit()





           
           

            

   

