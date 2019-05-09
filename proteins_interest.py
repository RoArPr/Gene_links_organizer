import prot_info
import shutil
import webbrowser

sod1 = prot_info.Prot('SOD1',
                 'Superoxide dismutase 1',
                'The protein encoded by this gene belongs to the PI3/PI4-kinase family. This protein is an important cell cycle checkpoint kinase that phosphorylates; thus, it functions as a regulator of a wide variety of downstream proteins, including tumor suppressor proteins p53 and BRCA1, checkpoint kinase CHK2, checkpoint proteins RAD17 and RAD9, and DNA repair protein NBS1. This protein and the closely related kinase ATR are thought to be master controllers of cell cycle checkpoint signaling pathways that are required for cell response to DNA damage and for genome stability. Mutations in this gene are associated with ataxia telangiectasia, an autosomal recessive disorder.',                      
                 'http://www.ncbi.nlm.nih.gov/books/NBK22225/',
                 'http://www.ncbi.nlm.nih.gov/gene/6647',
                 'http://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142168;r=21:31659622-31668931',
                 'http://www.ensembl.org/Homo_sapiens/Location/Chromosome?db=core;g=ENSG00000142168;r=21:31659622-31668931',
                 'http://www.uniprot.org/uniprot/P00441',
                 'http://www.ncbi.nlm.nih.gov/Structure/mmdb/mmdbsrv.cgi?uid=123822',
                 'http://www.ncbi.nlm.nih.gov/structure?term=SOD1',
                 'http://omim.org/entry/147450',
                 'http://www.ncbi.nlm.nih.gov/gquery/?term=SOD1')


brca1 = prot_info.Prot('BRCA1',
                      'breast cancer type 1 susceptibility protein',
                       'This gene encodes a nuclear phosphoprotein that plays a role in maintaining genomic stability, and it also acts as a tumor suppressor. The encoded protein combines with other tumor suppressors, DNA damage sensors, and signal transducers to form a large multi-subunit protein complex known as the BRCA1-associated genome surveillance complex (BASC). This gene product associates with RNA polymerase II, and through the C-terminal domain, also interacts with histone deacetylase complexes. This protein thus plays a role in transcription, DNA repair of double-stranded breaks, and recombination. Mutations in this gene are responsible for approximately 40% of inherited breast cancers and more than 80% of inherited breast and ovarian cancers. Alternative splicing plays a role in modulating the subcellular localization and physiological function of this gene. Many alternatively spliced transcript variants, some of which are disease-associated mutations, have been described for this gene, but the full-length natures of only some of these variants has been described.',
                       'http://www.ncbi.nlm.nih.gov/books/NBK22168/',
                      'http://www.ncbi.nlm.nih.gov/gene/672',
                      'http://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000012048;r=17:43044295-43125483',
                      'http://www.ensembl.org/Homo_sapiens/Location/Chromosome?db=core;g=ENSG00000012048;r=17:43044295-43125483',
                      'http://www.uniprot.org/uniprot/B7ZA85',
                      'http://www.ncbi.nlm.nih.gov/Structure/mmdb/mmdbsrv.cgi?uid=64699',
                      'http://www.ncbi.nlm.nih.gov/structure/?term=brca1',
                      'http://omim.org/entry/113705?search=brca1&highlight=brca1',
                      'http://www.ncbi.nlm.nih.gov/gquery/?term=brca1')

smad4 = prot_info.Prot('DPC4',
                       'SMAD family member 4',
                       'This gene encodes a member of the Smad family of signal transduction proteins. Smad proteins are phosphorylated and activated by transmembrane serine-threonine receptor kinases in response to TGF-beta signaling. The product of this gene forms homomeric complexes and heteromeric complexes with other activated Smad proteins, which then accumulate in the nucleus and regulate the transcription of target genes. This protein binds to DNA and recognizes an 8-bp palindromic sequence (GTCTAGAC) called the Smad-binding element (SBE). The Smad proteins are subject to complex regulation by post-translational modifications. Mutations or deletions in this gene have been shown to result in pancreatic cancer, juvenile polyposis syndrome, and hereditary hemorrhagic telangiectasia syndrome.',
                       'http://www.ncbi.nlm.nih.gov/books/NBK22206/',
                       'http://www.ncbi.nlm.nih.gov/gene/4089',
                      'http://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000141646;r=18:51028394-51085045',
                      'http://www.ensembl.org/Homo_sapiens/Location/Chromosome?db=core;g=ENSG00000141646;r=18:51028394-51085045',
                      'http://www.uniprot.org/uniprot/Q13485',
                      'http://www.ncbi.nlm.nih.gov/Structure/mmdb/mmdbsrv.cgi?uid=11496',
                      'http://www.ncbi.nlm.nih.gov/structure/?term=smad4',
                      'http://omim.org/entry/600993?search=smad4&highlight=smad4',
                      'http://www.ncbi.nlm.nih.gov/gquery/?term=smad4')

list_proteins = [sod1, brca1, smad4]

def info():     
    print ('List of proteins in the webpage:\n')
    for name in list_proteins:
        print (name)
info()

def show_all_links_gene_disease():
    for name in list_proteins:
        name.show_gene_disease()
                
#show_all_links_gene_disease()

def show_all_links_ncbi_gene():
    for name in list_proteins:
        name.show_ncbi_gene()

#show_all_links_ncbi_gene()
       
template = '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Protein_links</title>
<link rel="stylesheet" type="text/css" href="prot_links1.css">
</head>
<body>
<div class="container">
    <div class= "head">
        <h1>tag_symbol</h1>
    </div>
    <div class="nav">
         <ul class="nav">
             <li><a href="tag_gene_disease" target="_blank">gene&disease</a></li>
            <li><a href="tag_ncbi_gene" target="_blank">NCBI_gene</a></li>
            <li><a href="tag_ensembl" target="_blank">ensembl</a></li>
            <li><a href="tag_chromosome" target="_blank">chromosome</a></li>
            <li><a href="tag_uniprot" target="_blank">uniprot</a></li>
            <li><a href="tag_structure" target="_blank">3D structure</a></li>
            <li><a href="tag_all_structures" target="_blank">3D all_structures</a></li>
            <li><a href="tag_omim" target="_blank">OMIM</a></li>
            <li><a href="tag_ncbi_global" target="_blank">NCBI_global </a></li>
         </ul>
     <p id ="goto"><a href="index.html">go to index</a></p>       
    </div>
    <div class="content">
        <p><h3>Name:<span id ="name"> tag_full_name</span></h3></p>
        <p><h3>Description</h3>tag_text_file </p>     
    </div>
</div>
      <!-- end .container -->
</body>
</html>
'''

index_begin = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Index prot_links</title>
<link rel="stylesheet" type="text/css" href="prot_links1.css">
</head>
<body>
<div class="container">
    <div class= "head">
        <h1>Index of proteins</h1>
    </div>
    <div class="content">
        <ol>'''
  
index_end ='''
        </ol>   
    </div>
</div>
      <!-- end .container -->
       <p>Author: Rosa Arribas</p>
</body>
</html>

'''

def web_page_prot(template):
    # for each protein:
    for name in list_proteins:
        #1 - make a copy of the empty html_template and rename with the symbol name
        template_name = "template_prot.html"
        new_name = name.symbol
        new_name = new_name.lower()
        new_name = new_name + ".html"
        shutil.copy(template_name, new_name)
        #2- customize html template (type string) by replacing the tags with the object variables   
        new_template = template   
        new_template = new_template.replace("tag_symbol", name.symbol)
        new_template = new_template.replace("tag_full_name", name.full_name)
        new_template = new_template.replace("tag_text_file", name.text_file)
        new_template = new_template.replace("tag_gene_disease", name.gene_disease)
        new_template = new_template.replace("tag_ncbi_gene", name.ncbi_gene)
        new_template = new_template.replace("tag_ensembl", name.ensembl)
        new_template = new_template.replace("tag_chromosome", name.chromosome)
        new_template = new_template.replace("tag_uniprot", name.uniprot)
        new_template = new_template.replace("tag_structure", name.structure)
        new_template = new_template.replace("tag_all_structures", name.all_structures)
        new_template = new_template.replace("tag_omim", name.omim)
        new_template = new_template.replace("tag_ncbi_global", name.ncbi_all)
        #3- write the customized html in the file
        output_file = open(new_name, 'w')
        output_file.write(new_template)
        output_file.close()
        
def web_index ():
    #1 - make the index with the names of every object in a content_index
    content_index = ''
    for name in list_proteins:
        new_name = name.symbol
        new_name = new_name.lower()
        new_name = new_name + ".html"
        tag_text = '<li> <a href="' + new_name + '"'+ '>' + name.symbol + '</a></li>'
        content_index = content_index + tag_text
    # open the empty file index.html and write the entire html index and finally open in the webbrowser
    output_file = open('index.html','w')
    output_file.write(index_begin + content_index + index_end)
    output_file.close()
    webbrowser.open('index.html')

      
web_page_prot(template) 
web_index()


                     
                     
                   
                      
                
                       
                       


