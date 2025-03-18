
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/work/FAC/FBM/DBC/cdessim2/default/dmoi/miniconda3/envs/foldtree/lib/python3.10/site-packages', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/cache/snakemake/snakemake/source-cache/runtime-cache/tmpe_k_r92i/file/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95\x80\x07\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94(\x8c\x15CRIMVLG/allvall_1.csv\x94\x8c\rCRIMVLG/outdb\x94\x8c\x10CRIMVLG/outdb_ss\x94e}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x12\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x18)}\x94\x8c\x05_name\x94h\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94(\x8c\x15CRIMVLG/sequences.fst\x94\x8c\x14CRIMVLG/seq3di.fasta\x94e}\x94(h\x0e}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94(\x8c\x05outdb\x94\x8cR/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/mafftmat/3diHEXmat.txt\x94e}\x94(h\x0e}\x94(\x8c\x06dbname\x94K\x00N\x86\x94\x8c\x06submat\x94K\x01N\x86\x94uh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh;h7h=h8ub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94\x8c\x07CRIMVLG\x94a}\x94(h\x0e}\x94\x8c\x06folder\x94K\x00N\x86\x94sh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94b\x8c\x06folder\x94hLub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M\x98:M\xe27M\xe8\x03M\xba\x03\x8c\r/tmp/51037368\x94\x8c\x03cpu\x94\x8c\x0800:45:00\x94e}\x94(h\x0e}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\tpartition\x94K\x07N\x86\x94\x8c\x04time\x94K\x08N\x86\x94uh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bheK\x01hgK\x01hiM\x98:hkM\xe27hmM\xe8\x03hoM\xba\x03hqh`\x8c\tpartition\x94ha\x8c\x04time\x94hbub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8c\x1cCRIMVLG/logs/scrape_alns.log\x94a}\x94(h\x0e}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x06filter\x94\x89\x8c\x0ecustom_structs\x94\x88\x8c\x04cath\x94\x89\x8c\nfilter_min\x94K\n\x8c\nfilter_avg\x94K2\x8c\x0bastral_path\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/software/ASTER-Linux/bin/astral-pro\x94\x8c\rfoldseek_path\x94\x8c\x08foldseek\x94\x8c\x0efoldseek_cores\x94K\x01\x8c\x0biqtree_redo\x94\x89\x8c\x0ciqtree_cores\x94K\x01\x8c\x0eprob_threshold\x94\x8c\x030.9\x94\x8c\x0eqcov_threshold\x94\x8c\x0270\x94\x8c\x0escov_threshold\x94\x8c\x010\x94\x8c\x10evalue_threshold\x94\x8c\x051e-05\x94\x8c\tsubmat3di\x94\x8c$3diphy/3DI_substmat/3di_substmat.txt\x94\x8c\x0fmafft_submat3di\x94\x8c\x16mafftmat/3diHEXmat.txt\x94\x8c\x0cclean_folder\x94\x89\x8c\tfam_limit\x94M\x10'hZ]\x94(\x8c\x02c2\x94\x8c\x02c1\x94\x8c\x07CRIMVLG\x94eu\x8c\x04rule\x94\x8c\x11BM_ML_scrape_alns\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src\x94ub."); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/src/add_structalns.py';
######## snakemake preamble end #########

import toytree
import structalns
import os
import pandas as pd
import glob


print(snakemake.input)
print(snakemake.output)

alndf = pd.read_table(snakemake.input[0], header = None)

infolder = snakemake.input[0].split('/')[:-1]
infolder = ''.join( [i + '/' for i in infolder])

mapper3di, mapperAA = structalns.read_dbfiles3di( snakemake.input[1] , snakemake.input[2])

#add the 3di alignment to the dataframe
columns = 'query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,lddt,qaln,taln,cigar,alntmscore'.split(',')
alndf.columns = columns

print('submat', snakemake.params.submat)


alndf['query'] = alndf['query'].map(lambda x :x.replace('.pdb', ''))
alndf['target'] = alndf['target'].map(lambda x :x.replace('.pdb', ''))

alndf['3diq']= alndf['query'].map(mapper3di)
alndf['3dit']= alndf['target'].map(mapper3di)
alndf['AAq']= alndf['query'].map(mapperAA)
alndf['AAt']= alndf['target'].map(mapperAA)

#output a fasta with the 3di sequences
res = alndf.apply(structalns.calc_fident_crossaln , axis = 1)
alndf = pd.concat([alndf,res] , axis = 1)

with open(snakemake.output[0] , 'w') as out:
    for seq in alndf['query'].unique():
        out.write('>'+seq.replace('.pdb', '' )+'\n')
        out.write(mapperAA[seq.replace('.pdb', '')]+'\n')

with open(snakemake.output[1] , 'w') as out:
    for seq in alndf['query'].unique():
        out.write('>'+seq.replace('.pdb', '' )+'\n')
        out.write(mapper3di[seq.replace('.pdb', '')]+'\n')
