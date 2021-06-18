# R
# prepare the exons using the py sxcript from https://bioconductor.org/packages/3.10/bioc/vignettes/DEXSeq/inst/doc/DEXSeq.html

inDir = '/storage/home/users/pjt6/chicken_data/bam_files/light_ret_24_vs_lightret_6H/'

countFiles = list.files(inDir, pattern=".exons.counts$", full.names=TRUE)

basename(countFiles)

flattenedFile = list.files(inDir, pattern="gtf$", full.names=TRUE)

basename(flattenedFile)

sampleTable = data.frame(
   row.names = c('LIGHTRETRIGHT_24H_1', 'LIGHTRETRIGHT_24H_2', 'LIGHTRETRIGHT_24H_3', 'LIGHTRETRIGHT_24H_4', 'LIGHTRETRIGHT_24H_5', 
   'LIGHTRETRIGHT_6H_1', 'LIGHTRETRIGHT_6H_2', 'LIGHTRETRIGHT_6H_3', 'LIGHTRETRIGHT_6H_4', 'LIGHTRETRIGHT_6H_5'),
condition = c('LIGHTRETRIGHT_24H', 'LIGHTRETRIGHT_24H', 'LIGHTRETRIGHT_24H', 'LIGHTRETRIGHT_24H', 'LIGHTRETRIGHT_24H', 
'LIGHTRETRIGHT_6H', 'LIGHTRETRIGHT_6H', 'LIGHTRETRIGHT_6H', 'LIGHTRETRIGHT_6H', 'LIGHTRETRIGHT_6H'),
libType = c('paired-end',
 'paired-end', 'paired-end', 'paired-end', 'paired-end', 'paired-end', 'paired-end', 'paired-end', 
 'paired-end', 'paired-end'))

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

table ( dxr1$padj < 0.1 )

plotMA(dxr1, cex=0.8)

DEXSeqHTML( dxr1, FDR=0.3)

plotDEXSeq( dxr1, "FBgn0010909", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )


plotDEXSeq( dxr1, "ENSGALT00000002199", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000084418", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000102380", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000093660", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000104500", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000094699", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000006936", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000055021", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000104275", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000091144", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )
plotDEXSeq( dxr1, "ENSGALT00000058082", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )

