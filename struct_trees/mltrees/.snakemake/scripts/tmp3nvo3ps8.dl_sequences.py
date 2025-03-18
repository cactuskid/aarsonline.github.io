
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/work/FAC/FBM/DBC/cdessim2/default/dmoi/miniconda3/envs/foldtree/lib/python3.10/site-packages', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/cache/snakemake/snakemake/source-cache/runtime-cache/tmp7oaebzug/file/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95\x0c\x07\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8c\x12c2/identifiers.txt\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x03ids\x94K\x00N\x86\x94s\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x12\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x18)}\x94\x8c\x05_name\x94h\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh\x0eh\nub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8c\x17c2/sequence_dataset.csv\x94a}\x94(h\x0c}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94(\x89\x88\x89e}\x94(h\x0c}\x94(\x8c\x04cath\x94K\x00N\x86\x94\x8c\x0ecustom_structs\x94K\x01N\x86\x94\x8c\x0cclean_folder\x94K\x02N\x86\x94uh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh8\x89h:\x88h<\x89ub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94\x8c\x02c2\x94a}\x94(h\x0c}\x94\x8c\x06folder\x94K\x00N\x86\x94sh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94b\x8c\x06folder\x94hKub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M\x98:M\xe27M\xe8\x03M\xba\x03\x8c\r/tmp/51037347\x94\x8c\x03cpu\x94\x8c\x0800:45:00\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\tpartition\x94K\x07N\x86\x94\x8c\x04time\x94K\x08N\x86\x94uh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bhdK\x01hfK\x01hhM\x98:hjM\xe27hlM\xe8\x03hnM\xba\x03hph_\x8c\tpartition\x94h`\x8c\x04time\x94haub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8c\x17c2/logs/dlsequences.log\x94a}\x94(h\x0c}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x06filter\x94\x89\x8c\x0ecustom_structs\x94\x88\x8c\x04cath\x94\x89\x8c\nfilter_min\x94K\n\x8c\nfilter_avg\x94K2\x8c\x0bastral_path\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/software/ASTER-Linux/bin/astral-pro\x94\x8c\rfoldseek_path\x94\x8c\x08foldseek\x94\x8c\x0efoldseek_cores\x94K\x01\x8c\x0biqtree_redo\x94\x89\x8c\x0ciqtree_cores\x94K\x01\x8c\x0eprob_threshold\x94\x8c\x030.9\x94\x8c\x0eqcov_threshold\x94\x8c\x0270\x94\x8c\x0escov_threshold\x94\x8c\x010\x94\x8c\x10evalue_threshold\x94\x8c\x051e-05\x94\x8c\tsubmat3di\x94\x8c$3diphy/3DI_substmat/3di_substmat.txt\x94\x8c\x0fmafft_submat3di\x94\x8c\x16mafftmat/3diHEXmat.txt\x94\x8c\x0cclean_folder\x94\x89\x8c\tfam_limit\x94M\x10'hY]\x94(\x8c\x02c2\x94\x8c\x02c1\x94\x8c\x07CRIMVLG\x94eu\x8c\x04rule\x94\x8c\x13BM_dl_ids_sequences\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src\x94ub."); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/src/dl_sequences.py';
######## snakemake preamble end #########
import AFDB_tools
import os
import shutil	

custom_structs = snakemake.params.custom_structs
print('custom_structs: ', custom_structs)

clean = snakemake.params.clean_folder
print( 'clean: ', clean	)

basedir = snakemake.input[0].split('/')[:-1]
basedir = ''.join( [i + '/' for i in basedir])

if  clean == True:
	#move all structs from rejected to structs
	pass
	"""
	if os.path.exists(basedir + 'structs/') == False:
		os.mkdir(basedir + 'structs/')
	if os.path.exists(basedir + 'rejected/') == False:
		os.mkdir(basedir + 'rejected/')
	else:
		ids = os.listdir(basedir + 'rejected/')
		for i in ids:
			shutil.move(basedir + 'rejected/'+i, basedir + 'structs/' +i)
	#delete all files except identifiers.txt in basedir
	for file in os.listdir(basedir):
		if file != 'identifiers.txt' and os.path.isfile(basedir + file):
			os.remove(basedir + file)
	"""

if custom_structs == True and snakemake.params.cath == False:
	print('custom structures, skipping download of sequences')
	#writes a dummy file with the structs included
	with open(snakemake.output[0] , 'w') as outfile:
		outfile.write('')

else:
	with open(snakemake.input[0]) as infile:
		ids = [ i.strip() for i in infile if len(i.strip())>0 ]
	resdf = AFDB_tools.grab_entries(ids, verbose = True)
	resdf.to_csv(snakemake.output[0])
