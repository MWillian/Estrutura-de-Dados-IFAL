from Main import *

fila1 = FilaArray()

fila1.enqueue(5) # [5]
fila1.enqueue(3) # [5,3]
fila1.dequeue() # [3]
fila1.enqueue(2) # [3,2]
fila1.enqueue(8) # [3,2,8]
fila1.dequeue()# [2,8]
fila1.dequeue()# [8]
fila1.enqueue(9)# [8,9]
fila1.enqueue(1)# [8,9,1]
fila1.dequeue()# [9,1]
fila1.enqueue(7)# [9,1,7]
fila1.enqueue(6)# [9,1,7,6]
fila1.dequeue()# [1,7,6]
fila1.dequeue()# [7,6]
fila1.enqueue(4)# [7,6,4]
fila1.dequeue()# [6,4]
fila1.dequeue()# [4]