def printForca(tent):
    if tent == 6:
        print("""|----|
|    
|   
|   """)
    if tent == 5:
        print(""" |----|
 |    o
 |
 |""")
    if tent == 4:
        print("""|----|
|    o
|   /
|""")
    if tent == 3:
        print("""|----|
|    o
|   /|
|""")
    if tent == 2:
        print("""|----|
|    o
|   /|\\
|""")
    if tent == 1:
        print("""|----|
|    o
|   /|\\
|   / """)
    if tent == 0:
        print("""|----|
|    o
|   /|\\
|   / \\""")

