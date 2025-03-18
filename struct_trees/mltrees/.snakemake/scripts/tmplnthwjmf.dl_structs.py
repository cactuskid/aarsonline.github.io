
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/work/FAC/FBM/DBC/cdessim2/default/dmoi/miniconda3/envs/foldtree/lib/python3.10/site-packages', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/cache/snakemake/snakemake/source-cache/runtime-cache/tmpwdnmoy7l/file/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95@\x07\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8c\x17c2/sequence_dataset.csv\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x10\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x16)}\x94\x8c\x05_name\x94h\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8c\x0fc2/finalset.csv\x94a}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94(\x89\x89K\nK2\x88\x89e}\x94(h\x0c}\x94(\x8c\tfiltervar\x94K\x00N\x86\x94\x8c\x04cath\x94K\x01N\x86\x94\x8c\rfiltervar_min\x94K\x02N\x86\x94\x8c\rfiltervar_avg\x94K\x03N\x86\x94\x8c\x0ecustom_structs\x94K\x04N\x86\x94\x8c\x0cclean_folder\x94K\x05N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bh6\x89h8\x89h:K\nh<K2h>\x88h@\x89ub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94\x8c\x02c2\x94a}\x94(h\x0c}\x94\x8c\x06folder\x94K\x00N\x86\x94sh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94b\x8c\x06folder\x94hOub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M\x98:M\xe27M\xe8\x03M\xba\x03\x8c\r/tmp/51037351\x94\x8c\x03cpu\x94\x8c\x0800:45:00\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\tpartition\x94K\x07N\x86\x94\x8c\x04time\x94K\x08N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bhhK\x01hjK\x01hlM\x98:hnM\xe27hpM\xe8\x03hrM\xba\x03hthc\x8c\tpartition\x94hd\x8c\x04time\x94heub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8c\x15c2/logs/dlstructs.log\x94a}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x06filter\x94\x89\x8c\x0ecustom_structs\x94\x88\x8c\x04cath\x94\x89\x8c\nfilter_min\x94K\n\x8c\nfilter_avg\x94K2\x8c\x0bastral_path\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/software/ASTER-Linux/bin/astral-pro\x94\x8c\rfoldseek_path\x94\x8c\x08foldseek\x94\x8c\x0efoldseek_cores\x94K\x01\x8c\x0biqtree_redo\x94\x89\x8c\x0ciqtree_cores\x94K\x01\x8c\x0eprob_threshold\x94\x8c\x030.9\x94\x8c\x0eqcov_threshold\x94\x8c\x0270\x94\x8c\x0escov_threshold\x94\x8c\x010\x94\x8c\x10evalue_threshold\x94\x8c\x051e-05\x94\x8c\tsubmat3di\x94\x8c$3diphy/3DI_substmat/3di_substmat.txt\x94\x8c\x0fmafft_submat3di\x94\x8c\x16mafftmat/3diHEXmat.txt\x94\x8c\x0cclean_folder\x94\x89\x8c\tfam_limit\x94M\x10'h]]\x94(\x8c\x02c2\x94\x8c\x02c1\x94\x8c\x07CRIMVLG\x94eu\x8c\x04rule\x94\x8c\x11BM_dl_ids_structs\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src\x94ub."); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/src/dl_structs.py';
######## snakemake preamble end #########
import AFDB_tools
import os
import shutil
import glob
import pandas as pd
from Bio import PDB as pdb

'''
This script is used to download the structures from the afdb
it also filters the structures based on the plddt score

'''



infolder = snakemake.input[0].split('/')[:-1]
infolder = ''.join( [i + '/' for i in infolder])
structfolder = infolder+'structs/'
rejectedfolder = infolder+'rejected/'

#remove tmp folder

try:
	shutil.rmtree(infolder+'tmp/')
except:
	pass

custom_structs = snakemake.params.custom_structs
if custom_structs == True and snakemake.params.cath == False:
	print('custom structures, skipping download of structures')
	found = glob.glob(structfolder+'*.pdb')
	finalset = { f.replace('.pdb', '' ).split('/')[-1] : AFDB_tools.get_amino_acid_sequence(f) for f in found }
	with open(snakemake.output[0] , 'w') as outfile:
		outfile.write(''.join(['>'+i+'\n'+finalset[i]+'\n' for i in finalset]))
	

elif custom_structs == True and snakemake.params.cath == True:
	print('custom cath structures, skipping download of structures')
	found = glob.glob(structfolder+'*.pdb')
	finalset = { f.replace('.pdb', '' ).split('/')[-1] : AFDB_tools.get_amino_acid_sequence(f) for f in found }
	seqdf = pd.read_csv(snakemake.input[0])
	ids = list(seqdf['query'].unique())
	missing_structs = set(ids)-set(finalset.keys())
	print('missing in cath:',missing_structs)
	missing_sequences = set(ids)-set(seqdf['query'].unique())
	print( 'missing in sequences:',missing_sequences)
	finalset = set(ids)-set(missing_sequences)
	finalset = set(finalset)-set(missing_structs)
	resdf = seqdf[seqdf['query'].isin(finalset)]
	assert len(finalset) == len(resdf['query'].unique()) , 'finalset and resdf do not have the same length'
	#assert len(glob.glob(structfolder+'*.pdb')) == len(resdf['query'].unique()) , 'struct set and resdf do not have the same length'
	resdf.to_csv(snakemake.output[0])
else:
	#oma data
	try:
		os.mkdir(structfolder)
	except:
		print(structfolder , 'already exists ')

	try:
		os.mkdir(rejectedfolder)
	except:
		print(rejectedfolder , 'already exists ')

	#with open(snakemake.input[0]) as infile:
	#	ids = [ i.strip() for i in infile if len(i.strip())>0 ]
	seqdf = pd.read_csv(snakemake.input[0])
	ids = list(seqdf['query'].unique())

	missing = [	AFDB_tools.grab_struct(i, structfolder, rejectedfolder) for i in ids ]
	found = glob.glob(structfolder+'*.pdb') + glob.glob(rejectedfolder+'*.pdb')
	found = { i.split('/')[-1].replace('.pdb',''):i for i in found}
	missing_structs = set(ids)-set(found.keys())

	filtervar = snakemake.params.filtervar
	filtervar_min = snakemake.params.filtervar_min
	filtervar_avg = snakemake.params.filtervar_avg

	#get plddt from afdb structures and remove those with avg plddt < 0.4
	if filtervar == True:
		plddt = { i:AFDB_tools.filter_plddt( found[i] , thresh= filtervar_avg , minthresh = filtervar_min ) for i in found}
	else:
		plddt = { i:True for i in found}

	for i in list(found.keys()):
		if i not in ids or plddt[i] is False:
			#move to rejected folder
			if not os.path.isfile(rejectedfolder + i + '.pdb'):
				shutil.move(found[i], rejectedfolder)
			else:
				os.remove(found[i])
			missing_structs.add(i)
			del found[i]
	
	#remove sequences that do not have a structure
	missing_sequences = set(ids)-set(seqdf['query'].unique())
	print('missing in afdb:',missing_structs)
	print( 'missing in sequences:',missing_sequences)
	finalset = set(ids)-set(missing_sequences)
	finalset = set(finalset)-set(missing_structs)
	resdf = seqdf[seqdf['query'].isin(finalset)]
	found = glob.glob(structfolder+'*.pdb') + glob.glob(rejectedfolder+'*.pdb')
	finalset = { f.replace('.pdb', '' ).split('/')[-1] : AFDB_tools.get_amino_acid_sequence(f) for f in found if f.replace('.pdb', '' ).split('/')[-1] in finalset }	
	assert len(finalset) == len(resdf['query'].unique()) , 'finalset and resdf do not have the same length'
	assert len(glob.glob(structfolder+'*.pdb')) == len(resdf['query'].unique()) , 'struct set and resdf do not have the same length'
	#with open(snakemake.output[0] , 'w') as outfile:
	#	outfile.write(''.join(['>'+i+'\n'+finalset[i]+'\n' for i in finalset]))
	resdf.to_csv(snakemake.output[0])