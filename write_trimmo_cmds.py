import os
out = open("trimmo.sh","w")
out.write("#$ -cwd\n")

for filename in os.listdir(".") :
    if not filename.endswith(".gz") : continue
    if filename.endswith("1.fastq.gz"):
        prefix = filename.split("_1.fastq.gz")[0]
        cmd = "java -jar /shelf/training/Trimmomatic-0.38/trimmomatic-0.38.jar PE -summary %s_trim_summary.txt -threads 16 -phred33 %s_1.fastq.gz %s_2.fastq.gz %s_paired_R1.fq.gz crap1.fq.gz %s_paired_R2.fq.gz crap2.fq.gz ILLUMINACLIP:/shelf/training/Trimmomatic-0.38/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:45\n" % (prefix, prefix, prefix, prefix, prefix) 
        out.write(cmd)
out.close()
