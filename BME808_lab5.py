f = open("LATcomplement.txt")
f.readline()
seq = f.read().replace("\n", '')
fileoutput = open("LATresult.txt", 'w')

seq = seq[::-1]
seq = seq.replace( 'A', 'U').replace( 'C', 'x').replace( 'T', 'A').replace( 'G', 'C').replace( 'x', 'G')
fileoutput.write(seq)
fileoutput.close()

print(f'\nThe first ten letters are: {seq[0:10]}')
print(f'\nThe last ten letters are: {seq[-10:]}')

length = len(seq)
len_A = (seq.count('A')/length)*100
len_U = (seq.count('U')/length)*100
len_G = (seq.count('G')/length)*100
len_C = (seq.count('C')/length)*100

print(f"Percent A = {'%#.1f' % len_A}%")
print(f"Percent U = {'%#.1f' % len_U}%")
print(f"Percent G = {'%#.1f' % len_G}%")
print(f"Percent C = {'%#.1f' % len_C}%")