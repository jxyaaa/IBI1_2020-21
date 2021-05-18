def reverse(seq):
#input data
    list_seq=list(seq)
#create a list
    DNA=''
    for i in range(len(list_seq)-1,-1,-1):
        T={'C':'G','G':'C','A':'T','T':'A','c':'G','g':'C','a':'T','t':'A'}
        code=list_seq[i]
        DNA=DNA+T[code]
    return print(DNA)

reverse("AGCGGtCTCaGACT")
#an example