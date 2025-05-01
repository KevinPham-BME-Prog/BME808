#%%
#convert the pseudocode to python code
#include a printout of the percent identity and the percent gaps
def buildDirectionalString(matrix, N, M, gap):
    dstring = ""
    currentrow = N
    currentcol = M
    while (currentrow != 0 or currentcol != 0):
        if (currentrow == 0):
            dstring += 'H'
            currentcol -= 1
        elif (currentcol == 0):
            dstring += 'V'
            currentrow -= 1
        elif(matrix[currentrow][currentcol-1] + gap == matrix[currentrow][currentcol]):
            dstring += 'H'
            currentcol -=1
        elif (matrix[currentrow][currentcol] + gap == matrix[currentrow][currentcol]):
            dstring += 'V'
            currentrow -= 1
        else:
            dstring += 'D'
            currentrow -= 1
            currentcol -= 1
    return dstring

def needleman(s1, s2, gap = -1, mismatch = 0, match = 1):
    N = len(s1)
    M = len(s2)
    matrix = [[0 for i in range(1+M)] for j in range(1+N)]
    for i in range(1,M+1):
        matrix[0][i] = matrix[0][i-1] + gap

    for j in range(1,N+1):
        matrix[j][0] = matrix[j-1][0] + gap
    for i in range(1,M+1):
        for j in range(1, N+1):
            if (s1[j-1] == s2[i-1]):
                score1 = matrix[j-1][i-1] + match #diagnonal
            else:
                score1 = matrix[j-1][i-1] + mismatch #diagonal
            score2 = matrix[j-1][i] + gap
            score3 = matrix[j][i-1] + gap
            matrix[j][i] = max(score1, score2, score3)
    dstring = buildDirectionalString(matrix, N, M, gap)
    seq1pos = N -1 #position of last character in seq 1
    seq2pos = M -1 #position of lasr character in seq 2
    dirpos = 0
    alignment1 = ""
    alignment2 = ""
    matline = ""
    mismatches = 0
    matches = 0
    while (dirpos < len(dstring)):
        if (dstring[dirpos] == "D"):
            alignment1 += s1[seq1pos]
            alignment2 += s2[seq2pos]
            matline += "|"
            matches += 1
            seq1pos -= 1
            seq2pos -= 1
        elif (dstring[dirpos] == "V"):
            alignment1 += s1[seq1pos]
            alignment2 += "-"
            matline += "X"
            seq1pos -= 1
            mismatches += 1
        else:
            alignment2 += s2[seq2pos]
            alignment1 += "-"
            matline += "X"
            seq2pos -= 1
            mismatches += 1
        dirpos += 1

    print(alignment1[::-1])
    print(matline[::-1])
    print(alignment2[::-1])

    percentid = matches/(max(N, M))*100
    print("Percent ID: ", percentid)
    print("Percent Error:", 100 - percentid)



#%%
#try program on two sequnces
s1 = "ACTTCAATCGGT" #y-axis
s2 = "ACTGGTCAATCGGT" #x-axis

needleman(s1, s2) #shorter on left and longer on right



#%%
#use the two sequnces found in the NCBI

H1 = open("H1.fasta", "r")
H1.readline()
H1 = H1.read()
H1 = H1.replace('\n', "")
M1 = open("M1.fasta", "r")
M1.readline()
M1 = M1.read()
M1 = M1.replace('\n', "")
M2 = M1[1900:2045]
H2 = H1[21:166]







#%%
#use needle program on M2 and H1
needleman(M2, H1) #shorter on left and longer on right

#%%
#use needle program on M2 and H2

needleman(M2, H2) #shorter on left and longer on right


#%%
def waterman(s1, s2, gap = -1, mismatch = 0, match = 1):
    N = len(s1)
    M = len(s2)
    matrix = [[0 for i in range(1+M)] for j in range(1+N)]
    for i in range(1,M+1):
        for j in range(1, N+1):
            if (s1[j-1] == s2[i-1]):
                score1 = matrix[j-1][i-1] + match #diagnonal
            else:
                score1 = matrix[j-1][i-1] + mismatch #diagonal
            if score1 < 0:
                    score1 = 0
            score2 = matrix[j-1][i] + gap
            if score2 < 0:
                    score2 = 0
            score3 = matrix[j][i-1] + gap
            if score3 < 0:
                    score3 = 0
            matrix[j][i] = max(score1, score2, score3)
    dstring = buildDirectionalString(matrix, N, M, gap)
    seq1pos = N -1 #position of last character in seq 1
    seq2pos = M -1 #position of lasr character in seq 2
    dirpos = 0
    alignment1 = ""
    alignment2 = ""
    matline = ""
    mismatches = 0
    matches = 0
    while (dirpos < len(dstring)):
        if (dstring[dirpos] == "D"):
            alignment1 += s1[seq1pos]
            alignment2 += s2[seq2pos]
            matline += "|"
            matches += 1
            seq1pos -= 1
            seq2pos -= 1
        elif (dstring[dirpos] == "V"):
            alignment1 += s1[seq1pos]
            alignment2 += "-"
            matline += "X"
            seq1pos -= 1
            mismatches += 1
        else:
            alignment2 += s2[seq2pos]
            alignment1 += "-"
            matline += "X"
            seq2pos -= 1
            mismatches += 1
        dirpos += 1

    print(alignment1[::-1])
    print(matline[::-1])
    print(alignment2[::-1])
    percentid = matches/(max(N, M))*100
    print("Percent ID: ", percentid)
    print("Percent Error:", 100 - percentid)
s1 = "CGTGAATTCAT"
s2 = "GACTTAC"
waterman(s2, s1) #shorter on left and longer on right
#modify to make smith water man algorithm
# %%
