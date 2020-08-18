# pybbiology

```
Freely available tools for Analsis of DNA
The Biopython Project is an international association of developers
of freely available Python tools for computational molecular biology.
```

## List of functions and usage
-  seq_percent(dna_sequence,*char)
-  has_stop_codon(dna,frame=0)

## 1. compute DNA sequence 
```
def seq_percent(dna_sequence,*char):
        sum=0
        listed=[]
        dna_length=len(dna_sequence)
        for arg in char:
            if listed.count(arg)==0:
                sum= sum + dna_sequence.count(arg)
                listed.append(arg)
        return (sum)*100.0/dna_length
```
## 2. This function checks if given DNA has in frame stop codons.

```
def has_stop_codon(dna,frame=0):
    stop_codon_found=False
    stop_codons=['tga','tag','taa']
    for i in range(frame,len(dna),3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found
```