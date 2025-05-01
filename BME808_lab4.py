f = open("AF516335.txt")
f.readline()
seq = f.read().replace("\n", '')


def findpattern(pattern, search_Text, start_Loc, stop_loc, increment, thresh):
    patternlen = len(pattern)

    for i in range(start_Loc, stop_loc, increment):
        count = 0
        j = i

        for k in range(patternlen):
            if search_Text[j] == pattern[k]:
                count += 1
            j += 1
        if count >= thresh:
            return i
    return -1

limit = 99

stop_Codon = ["TAG", "TGA", "TAA"]
shine_seq = "AGGAGG"

while True:
    count = 0
    q = int(input("\nEnter [i] for Q[i] or 0 to exit: "))
    if q == 0:
        break
    elif q not in [1, 2, 3]:
        print("Incorrect input: \nEnter options: 1, 2, 3, 0.")
        continue

    i = 0

    while i < len(seq):
        stop_loc = 0
        start = findpattern("ATG", seq, i, len(seq) -3, 1 , 3)
        if start == -1:
            break

        for w in range(start + 3, len(seq) -3 ,3):
            if seq[w:w+3] in stop_Codon:
                stop_loc = w
                break

            else:
                stop_loc = -1
        orf = stop_loc - start

        if q == 1:
            start_Codon = findpattern("ATG", seq, 0 , len(seq) -3,1,3)
            print("\nQ1: ")
            print("\tStart Codon Length:", start_Codon)
            break
        elif q == 2:
            if orf >= limit:
                count += 1
                print("\tORF#", count, "\tATG = ", start, "\tSTOP = ", stop_loc)
                i = stop_loc
            else:
                i = start + 3
        elif q == 3:
            shine_loc = findpattern(shine_seq, seq, start - 13, start - 3, 1,5)
            if shine_loc != -1:
                if orf >= limit:
                    count += +1
                    print("\tORF#", count ,"\tSHINE = ", shine_loc ,"\tATG = ", start ,"\tSTOP = ", stop_loc)
                i = stop_loc + 3
            else:
                i = start +3

