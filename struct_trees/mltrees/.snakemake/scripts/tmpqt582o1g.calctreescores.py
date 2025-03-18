
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/work/FAC/FBM/DBC/cdessim2/default/dmoi/miniconda3/envs/foldtree/lib/python3.10/site-packages', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/cache/snakemake/snakemake/source-cache/runtime-cache/tmpcomq67ll/file/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95\x1e\x07\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94(\x8c\x17c2/sequence_dataset.csv\x94\x8c&c2/sequences.aln.muscle.fst.nwk.rooted\x94e}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x11\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x17)}\x94\x8c\x05_name\x94h\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8c#c2/treescores_sequences.muscle.json\x94a}\x94(h\r}\x94h\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94}\x94(h\r}\x94h\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94(\x8c\x02c2\x94\x8c\x06muscle\x94e}\x94(h\r}\x94(\x8c\x06folder\x94K\x00N\x86\x94\x8c\x07aligner\x94K\x01N\x86\x94uh\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94b\x8c\x06folder\x94hDhJhEub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M\x98:M\xe27M\xe8\x03M\xba\x03\x8c\r/tmp/51038160\x94\x8c\x03cpu\x94\x8c\x0800:45:00\x94e}\x94(h\r}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\tpartition\x94K\x07N\x86\x94\x8c\x04time\x94K\x08N\x86\x94uh\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bh`K\x01hbK\x01hdM\x98:hfM\xe27hhM\xe8\x03hjM\xba\x03hlh[\x8c\tpartition\x94h\\\x8c\x04time\x94h]ub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8c$c2/logs/sequences_scoring.muscle.log\x94a}\x94(h\r}\x94h\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x06filter\x94\x89\x8c\x0ecustom_structs\x94\x88\x8c\x04cath\x94\x89\x8c\nfilter_min\x94K\n\x8c\nfilter_avg\x94K2\x8c\x0bastral_path\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/software/ASTER-Linux/bin/astral-pro\x94\x8c\rfoldseek_path\x94\x8c\x08foldseek\x94\x8c\x0efoldseek_cores\x94K\x01\x8c\x0biqtree_redo\x94\x89\x8c\x0ciqtree_cores\x94K\x01\x8c\x0eprob_threshold\x94\x8c\x030.9\x94\x8c\x0eqcov_threshold\x94\x8c\x0270\x94\x8c\x0escov_threshold\x94\x8c\x010\x94\x8c\x10evalue_threshold\x94\x8c\x051e-05\x94\x8c\tsubmat3di\x94\x8c$3diphy/3DI_substmat/3di_substmat.txt\x94\x8c\x0fmafft_submat3di\x94\x8c\x16mafftmat/3diHEXmat.txt\x94\x8c\x0cclean_folder\x94\x89\x8c\tfam_limit\x94M\x10'hU]\x94(\x8c\x02c2\x94\x8c\x02c1\x94\x8c\x07CRIMVLG\x94eu\x8c\x04rule\x94\x8c\x15BM_calc_tax_score_seq\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src\x94ub."); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/src/calctreescores.py';
######## snakemake preamble end #########
import json
import treescore
import pandas as pd
import toytree
import numpy as np
from scipy.stats import describe
import copy
from ete3 import PhyloTree, NCBITaxa

ncbi = NCBITaxa()

def retspecies_tree(species_set):
    #get ncbi tree of species set
    species_set = list(species_set)
    species_set = [int(s) for s in species_set]
    species_set = ncbi.get_topology(species_set, intermediate_nodes=True)
    return species_set

def calc_scores(t , uniprot_csv ):
    uniprot_df = pd.read_csv(uniprot_csv)
    tree = toytree.tree(t)
    lineages = treescore.make_lineages(uniprot_df)
    species = treescore.get_species(uniprot_df)
    tree = treescore.label_leaves( tree , lineages , species)
    #tree = treescore.labelwRED(tree.treenode)
    overlap = treescore.getTaxOverlap(tree.treenode)
    taxscore = tree.treenode.score

    #calc descriptive stats on normalized branch lens to see if trees are balanced  
    lengths = np.array([node.dist for node in tree.treenode.traverse()])
    lengths /= np.sum(lengths)
    #calc the root first taxscore

    tree4 = copy.deepcopy(tree)
    treescore.getTaxOverlap_root(tree4.treenode)
    root_score , root_score_nr = treescore.sum_rootscore(tree4.treenode)

    species_set = set()
    #label the leaves with species and number
    for l in tree.treenode.get_leaves():
        if l.sp_num:
            l.name = l.sp_num
            species_set.add(l.sp_num.split('_')[0])

    species_tree = retspecies_tree(species_set)

    #change to phylo tree
    ncbitree = PhyloTree(species_tree.write()  , sp_naming_function=None)

    ncbitree.write(outfile=uniprot_csv.replace('.csv','_ncbi_tree.nwk' ) , format=1)
    etetree = PhyloTree(tree.write() , sp_naming_function=None)

    for l in etetree.get_leaves():
        l.species   = l.name.split('_')[0]
    
    recon_tree, events = etetree.reconcile(ncbitree)
    recon_dups = recon_tree.search_nodes(evoltype="D")
    recon_losses = recon_tree.search_nodes(evoltype="L")
    recon_speciations = recon_tree.search_nodes(evoltype="S")
    print( 'algo 1' )
    print('dups:', len(recon_dups))
    print('losses:', len(recon_losses))
    print('speciations:', len(recon_speciations))

    print( 'algo 2' )
    events = etetree.get_descendant_evol_events()
    dups = etetree.search_nodes(evoltype="D")
    losses = etetree.search_nodes(evoltype="L")
    speciations = etetree.search_nodes(evoltype="S")    
    print('dups:', len(dups))
    print('losses:', len(losses))
    print('speciations:', len(speciations))

    scores = {}
    #measure the distances of leaves to root
    distances = np.array([ node.get_distance(tree.treenode) for node in tree.treenode.get_leaves() ])
    distances_norm = distances / np.mean(distances)
    scores[t] = {'score': taxscore, 'stats': describe(lengths) , 'ultrametricity':  describe(distances), 
                    'ultrametricity_norm':  describe(distances_norm) , 'root_score': root_score , 'root_score_nr': root_score_nr  , 
                    'SO_speciations': len(recon_speciations) , 'SO_dups': len(recon_dups) , 'SO_losses': len(recon_losses) ,
                    'RECON_speciations':len(speciations) ,'RECON_dups': len(dups) , 'RECON_losses': len(losses)  }
    return scores

#calc the taxscore 
uniprot_df = pd.read_csv(snakemake.input[0])
scores = {}
stats = {}

for t in snakemake.input[1:]:
    print(t)
    scores.update(calc_scores(t , snakemake.input[0]))
print(scores)
with open(snakemake.output[0], 'w') as snakeout:
    snakeout.write( json.dumps( scores ) )



