input_file = open("spades_scaffolds.fasta", "r")
output_file = open("output.bed", "w")
dna_sequence = input_file.read()
start_codon = "ATG"
stop_codon = ["TAA", "TAG", "TGA"]
gene_starts = []
gene_ends = []
gene_found = False

for i in range(len(dna_sequence)):
    codon = dna_sequence[i:i+3]
    if codon == start_codon:
        gene_starts.append(i)
        gene_found = True
    elif codon in stop_codon and gene_found:
        gene_ends.append(i + 2) 
        gene_found = False

for i in range(len(gene_starts)):
    if i < len(gene_ends):
        bed_line = f"chr1\t{gene_starts[i]}\t{gene_ends[i]}\tGene{i+1}\t.\t+\n"
        output_file.write(bed_line)
    else:
        print(f"Не удалось найти соответствующий конец для старт-кодона {gene_starts[i]}")
        
input_file.close()
output_file.close()

print("Результаты в output.bed")
