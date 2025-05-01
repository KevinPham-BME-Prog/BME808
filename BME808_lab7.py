def isBasePair(a, b):
    if (a == "A" and b == "U") or (a == "U" and b == "A") or (a == "y_cor" and b =="G") or (a == "G" and b =="y_cor"):
       return 1 
    else: 
        return 0

def getMaxK(ref_matrix, i, j):
    curent_max = -1
    for boundary in range(i+1,j):
        t = ref_matrix[i][boundary] + ref_matrix[boundary+1][j]
        if t > curent_max:
            curent_max = t
    return curent_max
    
def findBasePairs(ref_matrix, seq_input, x_cor, y_cor):
    if x_cor >= y_cor:
        return
    elif ref_matrix[x_cor][y_cor] == ref_matrix[x_cor+1][y_cor]:
        findBasePairs(ref_matrix, seq_input, x_cor+1, y_cor)
    elif ref_matrix[x_cor][y_cor] == ref_matrix[x_cor][y_cor-1]:
        findBasePairs(ref_matrix, seq_input, x_cor, y_cor-1)
    elif ref_matrix[x_cor][y_cor] ==ref_matrix[x_cor+1][y_cor-1] + isBasePair(seq_input[x_cor], seq_input[y_cor]):
        if isBasePair(seq_input[x_cor], seq_input[y_cor]) == 1:
            print(seq_input[x_cor], ' (', x_cor,') base pairs with', seq_input[y_cor], '(', y_cor, ')')
        findBasePairs(ref_matrix, seq_input, x_cor+1, y_cor-1)
    else: 
        for boundary in range(x_cor+1, y_cor):
            t = ref_matrix[x_cor][boundary] + ref_matrix[boundary+1][y_cor]
            if t == ref_matrix[x_cor][y_cor]:
                findBasePairs(ref_matrix, seq_input, x_cor, boundary)
                findBasePairs(ref_matrix, seq_input, boundary+1, y_cor)


def read_fasta_file(filename):
    seq_input = open(filename)
    line1 = seq_input.readline()
    seq_input = seq_input.read().replace("\n",'')
    print(f"\nLine 1 = {line1}")

    return seq_input

while(True):    
    seq_input = " "
    while (seq_input == " "):
        choice = int(input("\nEnter 1 for CCCUUGG, 2 for seq1.txt, 3 for seq2.txt, and 4 for seq3.txt: "))
        if choice == 1: 
            seq_input = "CCCUUGG"
            print("\nLine 1 = A simple RNA sequence\n")
        elif choice == 2: seq_input = read_fasta_file("seq1.txt")
        elif choice == 3: seq_input = read_fasta_file("seq2.txt")
        elif choice == 4: seq_input = read_fasta_file("seq3.txt")
        
        
    N = len(seq_input)
    print (f"sequence = {seq_input}\nlength = {N}")
    print (f"-------------------------------\n-------------------------------\n{seq_input}")
    
    ref_matrix = [[0 for i in range(N)]for j in range(N)]
    
    for index, value in enumerate(ref_matrix):
         print(f"{value}") 
    
    for diagonal in range(1,N):
        for row in range(0, N-diagonal):
            col = row + diagonal
            w = isBasePair(seq_input[row], seq_input[col])
            v1 = ref_matrix[row+1][col-1] + w
            v2 = ref_matrix[row+1][col]
            v3 = ref_matrix[row][col-1]
            v4 = getMaxK(ref_matrix, row, col)
            ref_matrix[row][col] = max(v1, v2, v3, v4)
    
    print (f"-------------------------------\n-------------------------------\n{seq_input}")
    for index, value in enumerate(ref_matrix):
         print(f"{value}") 
    print("-------------------------------\n")
    
    findBasePairs(ref_matrix, seq_input, 0, N-1)
    
    quit_choice = input("\nEnter 0 to quit. Hit enter to continue: ")
    if quit_choice == "0": 
        break