from collections import defaultdict


third_meta = """WTCHG_328669_209 Sample:07A_DARK_TEL_LEFT Count:6921213
WTCHG_328669_210 Sample:07B_DARK_TEL_RIGHT Count:4019341
WTCHG_328669_221 Sample:22A_6HLIGHT_TEL_LEFT Count:4004936
WTCHG_328669_222 Sample:22B_6HLIGHT_TEL_RIGHT Count:12728700
WTCHG_328669_223 Sample:22C_6HLIGHT_RET_LEFT Count:14060200
WTCHG_328669_224 Sample:22D_6HLIGHT_RET_RIGHT Count:15842389
WTCHG_328669_241 Sample:42A_24HLIGHT_TEL_LEFT Count:17379215
WTCHG_328669_242 Sample:42B_24HLIGHT_TEL_RIGHT Count:19239117
WTCHG_328669_243 Sample:42C_24HLIGHT_RET_LEFT Count:11350328
WTCHG_328669_244 Sample:42D_24HLIGHT_RET_RIGHT Count:10017003
WTCHG_328669_245 Sample:44A_24HLIGHT_TEL_LEFT Count:11485751
WTCHG_328669_246 Sample:44B_24HLIGHT_TEL_RIGHT Count:4245942
WTCHG_328669_247 Sample:44C_24HLIGHT_RET_LEFT Count:6415919
WTCHG_328669_248 Sample:44D_24HLIGHT_RET_RIGHT Count:13312943
WTCHG_328669_249 Sample:49A_24HLIGHT_TEL_LEFT Count:7824585
WTCHG_328669_250 Sample:49B_24HLIGHT_TEL_RIGHT Count:14705126
WTCHG_328669_273 Sample:02A_DARK_TEL_LEFT Count:18767526
WTCHG_328669_274 Sample:02B_DARK_TEL_RIGHT Count:3353362
WTCHG_328669_275 Sample:02C_DARK_RET_LEFT Count:11265358
WTCHG_328669_276 Sample:02D_DARK_RET_RIGHT Count:14875611
WTCHG_328669_277 Sample:03A_DARK_TEL_LEFT Count:3338442
WTCHG_328669_278 Sample:03B_DARK_TEL_RIGHT Count:12290015
WTCHG_328669_279 Sample:03C_DARK_RET_LEFT Count:3753295
WTCHG_328669_280 Sample:03D_DARK_RET_RIGHT Count:16741498
WTCHG_328669_289 Sample:24A_6HLIGHT_TEL_LEFT Count:6731848
WTCHG_328669_290 Sample:24B_6HLIGHT_TEL_RIGHT Count:14389416
WTCHG_328669_291 Sample:24C_6HLIGHT_RET_LEFT Count:4171235
WTCHG_328669_292 Sample:24D_6HLIGHT_RET_RIGHT Count:15825416
WTCHG_328669_293 Sample:25A_6HLIGHT_TEL_LEFT Count:12529431
WTCHG_328669_294 Sample:25B_6HLIGHT_TEL_RIGHT Count:11315392
WTCHG_328670_211 Sample:07C_DARK_RET_LEFT Count:4353541
WTCHG_328670_212 Sample:07D_DARK_RET_RIGHT Count:4325944
WTCHG_328670_213 Sample:10A_DARK_TEL_LEFT Count:10318631
WTCHG_328670_214 Sample:10B_DARK_TEL_RIGHT Count:4950807
WTCHG_328670_215 Sample:10C_DARK_RET_LEFT Count:13237564
WTCHG_328670_216 Sample:10D_DARK_RET_RIGHT Count:16354197
WTCHG_328670_217 Sample:14A_DARK_TEL_LEFT Count:19189283
WTCHG_328670_218 Sample:14B_DARK_TEL_RIGHT Count:14401929
WTCHG_328670_219 Sample:14C_DARK_RET_LEFT Count:4473086
WTCHG_328670_220 Sample:14D_DARK_RET_RIGHT Count:5078432
WTCHG_328670_233 Sample:29A_6HLIGHT_TEL_LEFT Count:7834320
WTCHG_328670_234 Sample:29B_6HLIGHT_TEL_RIGHT Count:18453221
WTCHG_328670_235 Sample:29C_6HLIGHT_RET_LEFT Count:17376052
WTCHG_328670_236 Sample:29D_6HLIGHT_RET_RIGHT Count:9388101
WTCHG_328670_237 Sample:31A_6HLIGHT_TEL_LEFT Count:13398756
WTCHG_328670_238 Sample:31B_6HLIGHT_TEL_RIGHT Count:13515330
WTCHG_328670_239 Sample:31C_6HLIGHT_RET_LEFT Count:6772601
WTCHG_328670_240 Sample:31D_6HLIGHT_RET_RIGHT Count:6723865
WTCHG_328670_251 Sample:49C_24HLIGHT_RET_LEFT Count:4590925
WTCHG_328670_252 Sample:49D_24HLIGHT_RET_RIGHT Count:5049950
WTCHG_328670_253 Sample:50A_24HLIGHT_TEL_LEFT Count:21780719
WTCHG_328670_254 Sample:50B_24HLIGHT_TEL_RIGHT Count:16920263
WTCHG_328670_255 Sample:50C_24HLIGHT_RET_LEFT Count:4791542
WTCHG_328670_256 Sample:50D_24HLIGHT_RET_RIGHT Count:5950143
WTCHG_328670_257 Sample:54A_24HLIGHT_TEL_LEFT Count:22089522
WTCHG_328670_258 Sample:54B_24HLIGHT_TEL_RIGHT Count:4620560
WTCHG_328670_259 Sample:54C_24HLIGHT_RET_LEFT Count:9967688
WTCHG_328670_295 Sample:25C_6HLIGHT_RET_LEFT Count:19304576
WTCHG_328670_296 Sample:25D_6HLIGHT_RET_RIGHT Count:10406265
WTCHG_328670_301 Sample:54D_24HLIGHT_RET_RIGHT Count:11198668""".split("\n")


SAMPLE_DIC_COUNT = defaultdict(int)
name_set = set([])
count = 0
for i in third_meta:
    sample, condition, count = i.split()
    sample = sample.rstrip()
    condition = condition.split("_")[1:]
    condition = "".join(condition)
    if condition.startswith("LIGHT") or condition.startswith("DARK"):
        SAMPLE_DIC_COUNT[condition] += 1
        count = SAMPLE_DIC_COUNT[condition]
        condition = condition + "_" + str(count)
    if condition.startswith("6H"):
        condition = condition[2:] + "_6H"
        SAMPLE_DIC_COUNT[condition] += 1
        count = SAMPLE_DIC_COUNT[condition]
        condition = condition + "_" + str(count)
    if condition.startswith("24H"):
        condition = condition[3:] + "_24H"
        SAMPLE_DIC_COUNT[condition] += 1
        count = SAMPLE_DIC_COUNT[condition]
        condition = condition + "_" + str(count)
        
    SAMPLE_DIC_COUNT[sample.rstrip()] = condition.rstrip()

third = """WTCHG_328669_209_paired_R1.fq.gz  WTCHG_328669_247_paired_R1.fq.gz  WTCHG_328669_289_paired_R1.fq.gz  WTCHG_328670_217_paired_R1.fq.gz  WTCHG_328670_251_paired_R1.fq.gz
WTCHG_328669_210_paired_R1.fq.gz  WTCHG_328669_248_paired_R1.fq.gz  WTCHG_328669_290_paired_R1.fq.gz  WTCHG_328670_218_paired_R1.fq.gz  WTCHG_328670_252_paired_R1.fq.gz
WTCHG_328669_221_paired_R1.fq.gz  WTCHG_328669_249_paired_R1.fq.gz  WTCHG_328669_291_paired_R1.fq.gz  WTCHG_328670_219_paired_R1.fq.gz  WTCHG_328670_253_paired_R1.fq.gz
WTCHG_328669_222_paired_R1.fq.gz  WTCHG_328669_250_paired_R1.fq.gz  WTCHG_328669_292_paired_R1.fq.gz  WTCHG_328670_220_paired_R1.fq.gz  WTCHG_328670_254_paired_R1.fq.gz
WTCHG_328669_223_paired_R1.fq.gz  WTCHG_328669_273_paired_R1.fq.gz  WTCHG_328669_293_paired_R1.fq.gz  WTCHG_328670_233_paired_R1.fq.gz  WTCHG_328670_255_paired_R1.fq.gz
WTCHG_328669_224_paired_R1.fq.gz  WTCHG_328669_274_paired_R1.fq.gz  WTCHG_328669_294_paired_R1.fq.gz  WTCHG_328670_234_paired_R1.fq.gz  WTCHG_328670_256_paired_R1.fq.gz
WTCHG_328669_241_paired_R1.fq.gz  WTCHG_328669_275_paired_R1.fq.gz  WTCHG_328670_211_paired_R1.fq.gz  WTCHG_328670_235_paired_R1.fq.gz  WTCHG_328670_257_paired_R1.fq.gz
WTCHG_328669_242_paired_R1.fq.gz  WTCHG_328669_276_paired_R1.fq.gz  WTCHG_328670_212_paired_R1.fq.gz  WTCHG_328670_236_paired_R1.fq.gz  WTCHG_328670_258_paired_R1.fq.gz
WTCHG_328669_243_paired_R1.fq.gz  WTCHG_328669_277_paired_R1.fq.gz  WTCHG_328670_213_paired_R1.fq.gz  WTCHG_328670_237_paired_R1.fq.gz  WTCHG_328670_259_paired_R1.fq.gz
WTCHG_328669_244_paired_R1.fq.gz  WTCHG_328669_278_paired_R1.fq.gz  WTCHG_328670_214_paired_R1.fq.gz  WTCHG_328670_238_paired_R1.fq.gz  WTCHG_328670_295_paired_R1.fq.gz
WTCHG_328669_245_paired_R1.fq.gz  WTCHG_328669_279_paired_R1.fq.gz  WTCHG_328670_215_paired_R1.fq.gz  WTCHG_328670_239_paired_R1.fq.gz  WTCHG_328670_296_paired_R1.fq.gz
WTCHG_328669_246_paired_R1.fq.gz  WTCHG_328669_280_paired_R1.fq.gz  WTCHG_328670_216_paired_R1.fq.gz  WTCHG_328670_240_paired_R1.fq.gz  WTCHG_328670_301_paired_R1.fq.gz
""".split()
    

third_path = "/storage/home/users/jw279/data/chickendata/thrid/"
second = "/storage/home/users/jw279/data/chickendata/secondsetrecovery/"
first_path = "/storage/home/users/jw279/data/chickendata/first_set/"

f_out = open("STAR_chickcmd.sh", "w")
print("\nwritin star cmd to STAR_chickcmd.sh\n")

f_out.write("cd /storage/home/users/pjt6/chicken_data\n")


f_counts = open("chick_counts_cmd.sh", "w")

print("\nwritin DEcmd to chick_DE_exon_cmd.sh\n")


f_counts.write("cd /storage/home/users/pjt6/chicken_data\n")
#python /dexseq_count.py -p yes -f bam -r pos Gallus_gallus.GRCg6a.99.exons.gtf bam_sorted.bam bam_sorted.bam.exons.counts
#/shelf/apps/pjt6/apps/STAR-master/bin/Linux_x86_64_static/STAR --genomeDir star_indicies/ --limitGenomeGenerateRAM 455554136874 --limitBAMsortRAM 455554136874 --runThreadN 16 --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFilterMismatchNmax 7  --outFilterMultimapNmax 5 --outFileNamePrefix Gp --readFilesIn  R1.fq.gz R2.fq.gz


count = 0
file_to_sample_dict = dict()

for i in third:
    count =  count +1
    r1 = "/storage/home/users/jw279/data/chickendata/thrid/%s" % i
    temp = i.split("_paired_R1.fq.gz")[0]

    temp = temp.rstrip()
    if temp in SAMPLE_DIC_COUNT:
        cond = SAMPLE_DIC_COUNT[temp]
    else:
        break
    temp = temp + "_paired_R2.fq.gz"
    r2 =  "/storage/home/users/jw279/data/chickendata/thrid/" + temp
    cmd = "/shelf/apps/pjt6/apps/STAR-master/bin/Linux_x86_64_static/STAR --genomeDir star_indicies/ --limitGenomeGenerateRAM 455554136874 --limitBAMsortRAM 455554136874 --runThreadN 16 --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFilterMismatchNmax 7  --outFilterMultimapNmax 5 --outFileNamePrefix %s --readFilesIn %s %s \n" % (cond, r1, r2)
    f_out.write(cmd)
    countscmd = "python ./dexseq_count.py -p yes -f bam -r pos Gallus_gallus.GRCg6a.99.exons.gtf %s*.bam %s.exons.counts\n" % (cond, cond)
    f_counts.write(countscmd)
    outname = "%s" % (cond)
    file_to_sample_dict[outname] = cond

f_out.close()
f_counts.close()

w = ""
long = ""

for keys, vals in sorted(file_to_sample_dict.items()):
    w = w + keys + ", "
    long = long + keys + "\n"

print(w)

print("\n")
print(long)
