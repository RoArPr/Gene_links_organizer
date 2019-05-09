import webbrowser

class Prot():
    def __init__(self, symbol, full_name, text_file, gene_disease, ncbi_gene, ensembl, chromosome, uniprot, structure, all_structures, omim, ncbi_all):
        self.symbol = symbol
        self.full_name = full_name
        self.text_file= text_file
        self.gene_disease = gene_disease
        self.ncbi_gene = ncbi_gene
        self.ensembl = ensembl
        self.chromosome = chromosome
        self.uniprot = uniprot
        self.structure = structure
        self.all_structures = all_structures
        self.omim = omim
        self.ncbi_all = ncbi_all
        
    def __str__(self):
        return'[%s : %s]' %(self.symbol, self.full_name)

   
    def show_gene_disease(self):
        webbrowser.open(self.gene_disease)        
        
    def show_ncbi_gene(self):
        webbrowser.open(self.ncbi_gene)

    def show_ensembl(self):
        webbrowser.open(self.ensembl)

    def show_chromosome(self):
        webbrowser.open(self.chromosome)

    def show_uniprot(self):
        webbrowser.open(self.uniprot)

    def show_structure(self):
        webbrowser.open(self.structure)
    
    def show_structure_all(self):
        webbrowser.open(self.all_structures)

    def show_omim(self):
        webbrowser.open(self.omim)

    def show_ncbi_all(self):
        webbrowser.open(self.ncbi_all)

    
    
