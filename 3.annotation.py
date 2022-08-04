#https://github.com/Edinburgh-Genome-Foundry/SnapGeneReader
#https://www.snapgene.com/resources/coronavirus-resources/?resource=SARS-CoV-2_(COVID-19)_Genome

from snapgene_reader import snapgene_file_to_dict, snapgene_file_to_seqrecord
import pandas as pd

dictionary = snapgene_file_to_dict('annotation.dna')
CDS = [k for k in dictionary["features"] if k['type'] == "CDS"]
mat_peptide = [k for k in dictionary["features"] if k['type'] == "mat_peptide"]
genes = [k for k in dictionary["features"] if k['type'] == "gene"]

pos_dict = {}

for peptide in mat_peptide[:-1]:#petaei to teleftaio poy einai tou ORF1 mikro kommati
  pos_dict[peptide['qualifiers']['product']] = [peptide['start'],peptide['end']]

for gene in genes[1:]:
  pos_dict[gene['qualifiers']['gene']] = [gene['start'],gene['end']]

final_table = pd.DataFrame()

table = pd.read_csv("total_variant_norm.csv",index_col=0)
for label in pos_dict:
  pos = pos_dict[label]
  new_row = table.loc[pos[0]:pos[1]].mean()
  df = pd.DataFrame([new_row.rename(label)])
  final_table = pd.concat([final_table,df], axis = 0)
  
final_table.to_csv("annotation.csv")
'''['source', "5'UTR", 'gene', 'CSD', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'mat_peptide', 'CDS', 'mat_peptide', 'stem_loop', 'stem_loop', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'gene', 'CDS', 'stem_loop', 'stem_loop', "3'UTR", 'stem_loop']'''