#!/bin/bash
#$ -cwd
cd /storage/home/users/pjt6/chicken_data

#conda activate trinity
cat /storage/home/users/jw279/data/chickendata/thrid/*_paired_R1.fq.gz > R1.fq.gz

cat /storage/home/users/jw279/data/chickendata/thrid/*_paired_R2.fq.gz > R2.fq.gz

/shelf/apps/pjt6/apps/STAR-master/bin/Linux_x86_64_static/STAR --genomeDir star_indicies/  \
--limitBAMsortRAM 115554136874 --runThreadN 16 --readFilesCommand zcat \
--outSAMtype BAM SortedByCoordinate --outFilterMismatchNmax 7  --outFilterMultimapNmax 5 \
--outFileNamePrefix chick --readFilesIn R1.fq.gz R2.fq.gz

samtools index chick*.bam

 Trinity --genome_guided_bam chick*.bam \
         --genome_guided_max_intron 15000 \
         --CPU 12 --max_memory 100G --full_cleanup --output chicken_Trinity --genome_guided_min_coverage 5
         
 rm -rf R1.fq.gz R2.fq.gz