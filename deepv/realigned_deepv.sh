cd /storage/home/users/pjt6/docker/deepvariant/

        LC_ALL = "en_US.UTF-8"
        LC_CTYPE = "en_US.UTF-8"
        LANG = "en_US.UTF-8"

BIN_VERSION="0.10.0"
    # Run DeepVariant.
/opt/deepvariant/bin/run_deepvariant       --model_type=WES       --ref=ucsc.hg19.fasta       --reads=/storage/home/users/pjt6/docker/deepvariant/realigned.bam       --output_vcf=/storage/home/users/pjt6/docker/deepvariant//storage/home/users/pjt6/docker/deepvariant/realigned.vcf       --output_gvcf=/storage/home/users/pjt6/docker/deepvariant//storage/home/users/pjt6/docker/deepvariant/realigned.g.vcf.gz       --num_shards=10
 