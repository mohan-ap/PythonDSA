class Node():
    def __init__(self,data):
        self.data=data
        self.nextLink=None
        self.preLink=None

class DoublyLinkedList():
    head=None

    def insertFront(self):
        x=input("enter an element ")
        newNode=Node(x)
        if self.head==None:
            self.head=newNode
        else:
            newNode.nextLink=self.head
            self.head.preLink=newNode
            self.head=newNode

    def insertRear(self):
        x=input("enter an element ")
        newNode=Node(x)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.nextLink!=None:
                temp=temp.nextLink
            temp.nextLink=newNode
            newNode.preLink=temp

    def deleteFront(self):
        if self.head==None:
            print("Linked List empty, Deletion not possible")
        elif self.head.nextLink==None:
            print("Deleted data is",self.head.data)
            self.head=None
        else:
            print("Element deleted is",self.head.data)
            self.head=self.head.nextLink
            self.head.preLink=None

    def deleteRear(self):
        if self.head==None:
            print("Linked List empty, Deletion not possible")
        elif self.head.nextLink==None:
            print("Element Deleted is",self.head.data)
            self.head=None
        else:
            temp=self.head
            while temp.nextLink.nextLink != None:
                temp=temp.nextLink
            print("Element Deleted is",temp.nextLink.data)
            temp.nextLink=None

    def displayForward(self):
        if self.head==None:
            print("Linked List empty, Display not possible")
        elif self.head.nextLink==None:
            print(self.head.data)
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.nextLink
            print()
    def displayReverse(self):
        if self.head==None:
            print("Linked List empty, Display not possible")
        elif self.head.nextLink==None:
            print(self.head.data)
        else:
            temp =self.head
            while temp.nextLink!=None:
                temp=temp.nextLink
            while temp !=None:
                print(temp.data,end=" ")
                temp=temp.preLink
            print()


dd=DoublyLinkedList()
while True:
     s="""Enter the operation you want to perform
     "1" for insert front
     "2" for insert rear
     "3" for delete front
     "4" for delete rear
     "5" for display Forward
     "6" for display Reverse
     "anything" for exit"""
     print(s)
     x=int(input())
     if x==1:
      dd.insertFront()
     elif x==2:
      dd.insertRear()
     elif x==3:
      dd.deleteFront()
     elif x==4:
      dd.deleteRear()
     elif x==5:
      dd.displayForward()
     elif x==6:
      dd.displayReverse()
     else:
       exit()





           
           

            

   










