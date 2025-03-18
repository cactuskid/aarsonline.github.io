
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/work/FAC/FBM/DBC/cdessim2/default/dmoi/miniconda3/envs/foldtree/lib/python3.10/site-packages', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/cache/snakemake/snakemake/source-cache/runtime-cache/tmpyqkek9hl/file/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src', '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95\xf7\x06\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94(\x8c\x16CRIMVLG/alnAA_AA.fasta\x94\x8c\x18CRIMVLG/aln3di_3di.fasta\x94e}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x11\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x17)}\x94\x8c\x05_name\x94h\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94(\x8c\x17CRIMVLG/alnAA_3di.fasta\x94\x8c\x17CRIMVLG/aln3di_AA.fasta\x94e}\x94(h\r}\x94h\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94}\x94(h\r}\x94h\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94\x8c\x07CRIMVLG\x94a}\x94(h\r}\x94\x8c\x06folder\x94K\x00N\x86\x94sh\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94b\x8c\x06folder\x94hEub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M\x98:M\xe27M\xe8\x03M\xba\x03\x8c\r/tmp/51037466\x94\x8c\x03cpu\x94\x8c\x0800:45:00\x94e}\x94(h\r}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\tpartition\x94K\x07N\x86\x94\x8c\x04time\x94K\x08N\x86\x94uh\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bh^K\x01h`K\x01hbM\x98:hdM\xe27hfM\xe8\x03hhM\xba\x03hjhY\x8c\tpartition\x94hZ\x8c\x04time\x94h[ub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8c\x1bCRIMVLG/logs/cross_alns.log\x94a}\x94(h\r}\x94h\x0f]\x94(h\x11h\x12eh\x11h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x11sNt\x94bh\x12h\x15h\x17\x85\x94R\x94(h\x17)}\x94h\x1bh\x12sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x06filter\x94\x89\x8c\x0ecustom_structs\x94\x88\x8c\x04cath\x94\x89\x8c\nfilter_min\x94K\n\x8c\nfilter_avg\x94K2\x8c\x0bastral_path\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/software/ASTER-Linux/bin/astral-pro\x94\x8c\rfoldseek_path\x94\x8c\x08foldseek\x94\x8c\x0efoldseek_cores\x94K\x01\x8c\x0biqtree_redo\x94\x89\x8c\x0ciqtree_cores\x94K\x01\x8c\x0eprob_threshold\x94\x8c\x030.9\x94\x8c\x0eqcov_threshold\x94\x8c\x0270\x94\x8c\x0escov_threshold\x94\x8c\x010\x94\x8c\x10evalue_threshold\x94\x8c\x051e-05\x94\x8c\tsubmat3di\x94\x8c$3diphy/3DI_substmat/3di_substmat.txt\x94\x8c\x0fmafft_submat3di\x94\x8c\x16mafftmat/3diHEXmat.txt\x94\x8c\x0cclean_folder\x94\x89\x8c\tfam_limit\x94M\x10'hS]\x94(\x8c\x02c2\x94\x8c\x02c1\x94\x8c\x07CRIMVLG\x94eu\x8c\x04rule\x94\x8c\x10BM_ML_cross_alns\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cK/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/workflow/../src\x94ub."); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/work/FAC/FBM/DBC/cdessim2/default/dmoi/projects/snake_tree/src/crossalns.py';
######## snakemake preamble end #########

#copy the alignment logic from structal to sequence and vice versa
import Bio.SeqIO
import Bio.AlignIO

def crossaln(aln1f, aln2f, outaln):
    #copy aln1 logic to aln2
    #aln1 and al2 are both file names

    #read in the alignments
    aln1 = [ rec for rec in Bio.SeqIO.parse(aln1f, "fasta") ]
    aln2 = [ rec for rec in  Bio.SeqIO.parse(aln2f, "fasta") ]

    #get the sequences by removing the gaps
    seqs1= { rec.id: str(rec.seq) for rec in Bio.SeqIO.parse(aln1f, "fasta") }
    seqs2= { rec.id: str(rec.seq).replace("-","") for rec in Bio.SeqIO.parse(aln2f, "fasta") }

    print('seqs1',seqs1.keys())
    print('seqs2',seqs2.keys())


    #copy the gap positions from aln1 to aln2
    for rec in aln2:
        seq = seqs2[str(rec.id)]
        seq = list(seq)
        i = 0
        for c in seqs1[str(rec.id)]:
            if c == "-":
                seq.insert(i, "-")
            else:
                i += 1
        seqs2[str(rec.id)] = "".join(seq)
    #write out the new alignment
    with open(outaln, "w") as f:
        for rec in aln2:
            f.write(">%s\n%s\n" % (rec.id, seqs2[str(rec.id)]))
    return outaln

if __name__ == "__main__":

    #snakemake input and output files
    aln1 = snakemake.input[0]
    aln2 = snakemake.input[1]
    outaln = snakemake.output[0]


    crossaln(aln1, aln2, outaln)

    aln1 = snakemake.input[1]
    aln2 = snakemake.input[0]
    outaln = snakemake.output[1]

    crossaln(aln1, aln2, outaln)
