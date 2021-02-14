# R
# prepare the exons using the py sxcript from https://bioconductor.org/packages/3.10/bioc/vignettes/DEXSeq/inst/doc/DEXSeq.html

inDir = '/storage/home/users/pjt6/chicken_data/bam_files/'

countFiles = list.files(inDir, pattern=".exons.counts$", full.names=TRUE)

basename(countFiles)

flattenedFile = list.files(inDir, pattern="gtf$", full.names=TRUE)

basename(flattenedFile)

# all vs all - too much for what we want. Took 2 weeks to run!!
sampleTable = data.frame(
   row.names = c("DARKRETLEFT_1", "DARKRETLEFT_2", "DARKRETLEFT_3", "DARKRETLEFT_4", "DARKRETLEFT_5", 
   "DARKRETRIGHT_1", "DARKRETRIGHT_2", "DARKRETRIGHT_3", "DARKRETRIGHT_4", "DARKRETRIGHT_5", "DARKTELLEFT_1", 
   "DARKTELLEFT_2", "DARKTELLEFT_3", "DARKTELLEFT_4", "DARKTELLEFT_5", "DARKTELRIGHT_1", "DARKTELRIGHT_2",
   "DARKTELRIGHT_3", "DARKTELRIGHT_4", "DARKTELRIGHT_5", "LIGHTRETLEFT_24H_1", "LIGHTRETLEFT_24H_2", "LIGHTRETLEFT_24H_3", 
   "LIGHTRETLEFT_24H_4", "LIGHTRETLEFT_24H_5", "LIGHTRETLEFT_6H_1", "LIGHTRETLEFT_6H_2", "LIGHTRETLEFT_6H_3", "LIGHTRETLEFT_6H_4", 
   "LIGHTRETLEFT_6H_5", "LIGHTRETRIGHT_24H_1", "LIGHTRETRIGHT_24H_2", "LIGHTRETRIGHT_24H_3", "LIGHTRETRIGHT_24H_4", "LIGHTRETRIGHT_24H_5", 
   "LIGHTRETRIGHT_6H_1", "LIGHTRETRIGHT_6H_2", "LIGHTRETRIGHT_6H_3", "LIGHTRETRIGHT_6H_4", "LIGHTRETRIGHT_6H_5", 
   "LIGHTTELLEFT_24H_1", "LIGHTTELLEFT_24H_2", "LIGHTTELLEFT_24H_3", "LIGHTTELLEFT_24H_4", "LIGHTTELLEFT_24H_5", "LIGHTTELLEFT_6H_1", 
   "LIGHTTELLEFT_6H_2", "LIGHTTELLEFT_6H_3", "LIGHTTELLEFT_6H_4", "LIGHTTELLEFT_6H_5", "LIGHTTELRIGHT_24H_1", "LIGHTTELRIGHT_24H_2",
   "LIGHTTELRIGHT_24H_3", "LIGHTTELRIGHT_24H_4", "LIGHTTELRIGHT_24H_5", "LIGHTTELRIGHT_6H_1", "LIGHTTELRIGHT_6H_2", "LIGHTTELRIGHT_6H_3", 
   "LIGHTTELRIGHT_6H_4", "LIGHTTELRIGHT_6H_5"),
   condition = c("DARKRETLEFT",  "DARKRETLEFT",  "DARKRETLEFT",  "DARKRETLEFT",  "DARKRETLEFT",  "DARKRETRIGHT",  "DARKRETRIGHT",  
   "DARKRETRIGHT",  "DARKRETRIGHT",  "DARKRETRIGHT",  "DARKTELLEFT",  "DARKTELLEFT",  "DARKTELLEFT",  "DARKTELLEFT",  "DARKTELLEFT",  
   "DARKTELRIGHT",  "DARKTELRIGHT",  "DARKTELRIGHT",  "DARKTELRIGHT",  "DARKTELRIGHT",  "LIGHTRETLEFT_24H",  "LIGHTRETLEFT_24H",  
   "LIGHTRETLEFT_24H",  "LIGHTRETLEFT_24H",  "LIGHTRETLEFT_24H",  "LIGHTRETLEFT_6H",  "LIGHTRETLEFT_6H",  "LIGHTRETLEFT_6H",  "LIGHTRETLEFT_6H",  
   "LIGHTRETLEFT_6H",  "LIGHTRETRIGHT_24H",  "LIGHTRETRIGHT_24H",  "LIGHTRETRIGHT_24H",  "LIGHTRETRIGHT_24H",  "LIGHTRETRIGHT_24H", 
   "LIGHTRETRIGHT_6H",  "LIGHTRETRIGHT_6H",  "LIGHTRETRIGHT_6H",  "LIGHTRETRIGHT_6H",  "LIGHTRETRIGHT_6H",  "LIGHTTELLEFT_24H", 
   "LIGHTTELLEFT_24H",  "LIGHTTELLEFT_24H",  "LIGHTTELLEFT_24H",  "LIGHTTELLEFT_24H",  "LIGHTTELLEFT_6H",  "LIGHTTELLEFT_6H",  
   "LIGHTTELLEFT_6H",  "LIGHTTELLEFT_6H",  "LIGHTTELLEFT_6H",  "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_24H", 
   "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_6H",  "LIGHTTELRIGHT_6H",  "LIGHTTELRIGHT_6H",  "LIGHTTELRIGHT_6H", 
   "LIGHTTELRIGHT_6H"),
   libType = c("paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end",
   "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", 
   "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end",
   "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", 
   "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", 
   "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end"))


# RIGHT LIGHT vs DAR TEL
sampleTable = data.frame(
   row.names = c("DARKTELRIGHT_1",  "DARKTELRIGHT_2",  "DARKTELRIGHT_3",  "DARKTELRIGHT_4", 
   "DARKTELRIGHT_5",  "LIGHTTELRIGHT_24H_1",  "LIGHTTELRIGHT_24H_2",  "LIGHTTELRIGHT_24H_3", 
   "LIGHTTELRIGHT_24H_4",  "LIGHTTELRIGHT_24H_5",  "LIGHTTELRIGHT_6H_1",  "LIGHTTELRIGHT_6H_2", 
   "LIGHTTELRIGHT_6H_3",  "LIGHTTELRIGHT_6H_4",  "LIGHTTELRIGHT_6H_5"),
condition = c("DARKTELRIGHT",  "DARKTELRIGHT",  "DARKTELRIGHT",  "DARKTELRIGHT",  "DARKTELRIGHT",  
    "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_24H",  "LIGHTTELRIGHT_24H", 
    "LIGHTTELRIGHT_6H",  "LIGHTTELRIGHT_6H",  "LIGHTTELRIGHT_6H",  "LIGHTTELRIGHT_6H",  "LIGHTTELRIGHT_6H"),
libType = c("paired-end",  "paired-end",  "paired-end",  "paired-end",  "paired-end",  "paired-end",  
    "paired-end",  "paired-end",  "paired-end",  "paired-end",  "paired-end",  "paired-end",  "paired-end", 
    "paired-end",  "paired-end"))
				

sampleTable


#dxd =read.HTSeqCounts(countFiles,sampleData=sampleTable,design= ~ sample + exon + condition:exon,flattenedfile=flattenedFile) 


library("DEXSeq")

dxd = DEXSeqDataSetFromHTSeq(countFiles, sampleData=sampleTable, design= ~ sample + exon + condition:exon,flattenedfile=flattenedFile )

colData(dxd)

head( counts(dxd), 5 )

head( featureCounts(dxd), 5) 

 head ( rowRanges(dxd), 3 )
 
 sampleAnnotation( dxd )
 
# uses DEseq2 method
dxd = estimateSizeFactors( dxd )

# dispersion estimation
dxd = estimateDispersions( dxd)

#As a shrinkage diagnostic, the DEXSeqDataSet inherits the method plotDispEsts() that plots the per-exon dispersion estimates versus the mean normalised count, the resulting fitted valuesand the a posteriori (shrinked) dispersion estimates
plotDispEsts( dxd )

# test for DE (exon) expression) 
dxd = testForDEU( dxd )

dxr1 = DEXSeqResults( dxd )

write.table(dxr1, file = "chicken_RNAseq_Dexseq_results.out", append = FALSE, quote = TRUE, sep = "\t",
            eol = "\n", na = "NA", dec = ".", row.names = TRUE,
            col.names = TRUE, qmethod = c("escape", "double"),
            fileEncoding = "")

dxr1


#From this object, we can ask how many genes are signicant with a false discovery rate of 5%:
#table ( dxr1$padj < 0.05 )

#From this object, we can ask how many genes are signicant with a false discovery rate of 1%:
table ( dxr1$padj < 0.01 )

# ask how many genes are aected (FDR 0.001)
#table ( tapply( dxr1$padj < 0.001, dxr1$groupID, any ) )

table ( tapply( dxr1$padj < 0.001, dxr1, any ) )



plotMA(dxr1, cex=0.8)

#DEXSeqHTML( dxr1, FDR=0.001)
DEXSeqHTML( dxr1, FDR=0.1)
