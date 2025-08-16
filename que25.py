"""
Accept 5 expense from user and find average of expense
"""
expenses = map(int, input("Enter 5 expenses").split())
total = sum(expenses)
avg = total / 5
print("Average expenses:",avg)