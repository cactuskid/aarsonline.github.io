
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/work/FAC/FBM/DBC/cdessim2/default/dmoi/miniconda3/envs/foldtree/lib/python3.10/site-packages', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/cache/snakemake/snakemake/source-cache/runtime-cache/tmpypoer3n4/file/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95\x08\x08\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8c\x10c2/allvall_0.csv\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x10\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x16)}\x94\x8c\x05_name\x94h\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94(\x8c\x1dc2/fident_0_raw_fastmemat.txt\x94\x8c!c2/alntmscore_0_raw_fastmemat.txt\x94\x8c\x1bc2/lddt_0_raw_fastmemat.txt\x94\x8c\x1dc2/fident_0_exp_fastmemat.txt\x94\x8c!c2/alntmscore_0_exp_fastmemat.txt\x94\x8c\x1bc2/lddt_0_exp_fastmemat.txt\x94e}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94\x8coquery,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,lddt,qaln,taln,cigar,alntmscore\x94a}\x94(h\x0c}\x94\x8c\x03fmt\x94K\x00N\x86\x94sh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bh<h9ub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94(\x8c\x02c2\x94\x8c\x010\x94e}\x94(h\x0c}\x94(\x8c\x06folder\x94K\x00N\x86\x94\x8c\x07alntype\x94K\x01N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94b\x8c\x06folder\x94hK\x8c\x07alntype\x94hLub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M NM\x82JM\xe8\x03M\xba\x03\x8c\r/tmp/51037372\x94\x8c\x03cpu\x94\x8c\x0800:45:00\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\tpartition\x94K\x07N\x86\x94\x8c\x04time\x94K\x08N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bhhK\x01hjK\x01hlM NhnM\x82JhpM\xe8\x03hrM\xba\x03hthc\x8c\tpartition\x94hd\x8c\x04time\x94heub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8c\x1ec2/logs/0_foldseek2distmat.log\x94a}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x06filter\x94\x89\x8c\x0ecustom_structs\x94\x88\x8c\x04cath\x94\x89\x8c\nfilter_min\x94K\n\x8c\nfilter_avg\x94K2\x8c\x0bastral_path\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/software/ASTER-Linux/bin/astral-pro\x94\x8c\rfoldseek_path\x94\x8c\x08foldseek\x94\x8c\x0efoldseek_cores\x94K\x01\x8c\x0biqtree_redo\x94\x89\x8c\x0ciqtree_cores\x94K\x01\x8c\x0eprob_threshold\x94\x8c\x030.9\x94\x8c\x0eqcov_threshold\x94\x8c\x0270\x94\x8c\x0escov_threshold\x94hL\x8c\x10evalue_threshold\x94\x8c\x051e-05\x94\x8c\tsubmat3di\x94\x8c$3diphy/3DI_substmat/3di_substmat.txt\x94\x8c\x0fmafft_submat3di\x94\x8c\x16mafftmat/3diHEXmat.txt\x94\x8c\x0cclean_folder\x94\x89\x8c\tfam_limit\x94M\x10'h\\]\x94(\x8c\x02c2\x94\x8c\x02c1\x94\x8c\x07CRIMVLG\x94eu\x8c\x04rule\x94\x8c\x13BM_foldseek2distmat\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src\x94ub."); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/src/foldseekres2distmat.py';
######## snakemake preamble end #########
import foldseek2tree
import numpy as np
import pandas as pd

res = pd.read_table(snakemake.input[0], header = None)


print(res.head())

#get the folder of the input file
infolder = snakemake.input[0].split('/')[:-1]
infolder = ''.join( [i + '/' for i in infolder])+'/'
res[0] = res[0].map(lambda x :x.replace('.pdb', ''))
res[1] = res[1].map(lambda x :x.replace('.pdb', ''))


if snakemake.params.fmt is None:
    res.columns = 'query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,lddt,lddtfull,alntmscore'.split(',')
else:
    res.columns = snakemake.params.fmt.split(',')

ids = list( set(list(res['query'].unique()) + list(res['target'].unique())))
pos = { protid : i for i,protid in enumerate(ids)}
kernels = ['fident', 'alntmscore', 'lddt']

#set kernel columns to float
for k in kernels:
    res[k] = res[k].astype(float)

#change nan to 0
res = res.fillna(0)


matrices = { k:np.zeros((len(pos), len(pos))) for k in kernels }
print(res)


#calc kernel for tm, aln score, lddt
for idx,row in res.iterrows():
    for k in matrices:
        matrices[k][pos[row['query']] , pos[row['target']]] += row[k]
        matrices[k][pos[row['target']] , pos[row['query']]] += row[k]

for i,k in enumerate(matrices):
    matrices[k] /= 2
    matrices[k] = 1-matrices[k]
    print(matrices[k], np.amax(matrices[k]), np.amin(matrices[k]) )
    np.save( infolder + k + '_distmat.npy' , matrices[k])
    distmat_txt = foldseek2tree.distmat_to_txt( ids , matrices[k] , snakemake.output[i] )

for i,k in enumerate(matrices):
    if k == 'fident':
        #bfactor=19/20
        bfactor=.93

    else:
        bfactor=1
    tajima =  foldseek2tree.Tajima_dist(matrices[k] + 10 **-5 , bfactor=bfactor )
    np.fill_diagonal(tajima, 0)
    distmat_txt = foldseek2tree.distmat_to_txt( ids , tajima , snakemake.output[len(matrices)+i] )
