import os
import sys
from optparse import OptionParser
import datetime
from collections import defaultdict

f_in = open("GRCg6a.cds_VS_GCF_000002315.5_GRCg6a_rna.tab", "r")

code_to_name = dict()
code_to_name_reduced = dict()
name_to_code = dict()

for line in f_in:
    data = line.split("\t")
    name = data[0]
    code = data[1]
    name_to_code[name.rstrip()] = code.rstrip()
    code_to_name[code.rstrip()] = name.rstrip()
    code_to_name_reduced[code.split(".")[0]] = name.rstrip()
f_in.close()

wanted = """

""".split()

codes = """
DDT
FXYD6
CTGF
SCPEP1
FJX1
KATNBL1
FLOT2
USP1
C2orf88
CLK2
SYNGR3
KIAA0907
LCLAT1
TGFB1
DBN1
SRA1
TBX3
STK40
GCDH
MARCKSL1
BAHCC1
UMPS
SLC8A2
KCNMB4
SAP130
CALML4
LFNG
IVD
HS6ST1
ARHGDIB
CDC25B
WDR24
RHBDL1
ARL6IP5
PPIB
RHOB
CBX4
DDX23
DPYSL3
MAB21L1
DCTN2
SALL1
FEZ1
XPO1
PRDX1
AACS
NREP
HDAC1
SPPL2B
PDK3
ZNF706
EXOC4
TWF1
GLRX5
CDHR1
ATP1A1
TMED1
HSPA4L
ABTB1
STARD4
CHORDC1
ATP6V1H
TMEM254
ANO5
CETN1
GNPDA1
INSIG1
PDE3B
SLC1A2
PTDSS1
PRELID3B
MED8
RBP1
LBH
NUP188
PDHX
MAP6
GTF2E2
PCDH8
ACKR3
CLPX


""".split()
for i in wanted:
    print(name_to_code[i])

old_gene_of_interest = set([])
for i in codes:
    if i in code_to_name_reduced:
        print(code_to_name_reduced[i.rstrip()], "\t", i)
        old_gene_of_interest.add(code_to_name_reduced[i.rstrip()])


dark_TEL_left_up = set("""ARFGEF3.p1	ENSGALT00000047106.2
FAT3.p1	ENSGALT00000101402.1
YRDC.p1	ENSGALT00000100422.1
TMCC2.p1	ENSGALT00000050468.2
SPATA13.p1	ENSGALT00000102304.1
PLEKHH1.p1	ENSGALT00000063079.2
GOT2.p1	ENSGALT00000089124.2
RASGEF1A.p1	ENSGALT00000034231.5
CENPF.p1	ENSGALT00000084212.2
MAPK8IP1.p1	ENSGALT00000054366.2
PLEKHM3.p1	ENSGALT00000070770.2
USP24.p1	ENSGALT00000059062.2
CTCF.p1	ENSGALT00000002811.4
FLNB.p1	ENSGALT00000055290.2
TBC1D4.p1	ENSGALT00000056657.2
DCBLD2.p1	ENSGALT00000102657.1
KBTBD4.p1	ENSGALT00000013128.6
MYO18A.p1	ENSGALT00000100461.1
STAG2.p1	ENSGALT00000063371.2
IL17RD.p1	ENSGALT00000008827.6
RFX2.p1	ENSGALT00000095394.1
KCNMA1.p1	ENSGALT00000085233.2""".split("\n"))


dark_RET_up_right_vs_left = set("""PRKA.p1	ENSGALT00000077603.2
SYNE1.p1	ENSGALT00000048947.2
PLXNA2.p1	ENSGALT00000101458.1
RBM43.p1	ENSGALT00000099806.1
EP400.p1	ENSGALT00000095730.1
Hsp110.p1	ENSGALT00000098212.1
PIGQ.p1	ENSGALT00000098671.1
APC.p1	ENSGALT00000056056.2
PPP2R5C.p1	ENSGALT00000086659.2
AFF2.p1	ENSGALT00000095758.1
USP34.p1	ENSGALT00000107765.1
KMT2C.p1	ENSGALT00000101855.1
ACOT7.p1	ENSGALT00000087758.2
CADM1.p1	ENSGALT00000057839.2
RAPGEF2.p1	ENSGALT00000076253.2
PCDH1.p1	ENSGALT00000104852.1
ALG8.p1	ENSGALT00000088712.2
ANK1.p1	ENSGALT00000091547.1
GRIP2.p1	ENSGALT00000049228.2""".split("\n"))


dark_RET_up_left_vs_right = set("""DARS.p1	ENSGALT00000050094.2
BMT2.p1	ENSGALT00000097526.1
SDC4.p1	ENSGALT00000006265.5
ANKRD11.p1	ENSGALT00000108365.1
TXNRD2.p1	ENSGALT00000079571.3
CAMSAP1.p1	ENSGALT00000061740.2
GSN.p1	ENSGALT00000084418.2
tre-2/USP6,.p1	ENSGALT00000069912.2
FRYL.p1	ENSGALT00000096883.1
BCOR.p1	ENSGALT00000036653.4
ZNF438.p1	ENSGALT00000107568.1
FRMD3.p1	ENSGALT00000020544.6
LAMA5.p1	ENSGALT00000095348.1
KIF16B.p1	ENSGALT00000102380.1
NPRL3.p1	ENSGALT00000039730.4
SYNE3.p1	ENSGALT00000108144.1
GCN1.p1	ENSGALT00000104567.1
ARL2BP.p1	ENSGALT00000061751.2
PRDM15.p1	ENSGALT00000090664.1
WDR26.p1	ENSGALT00000104120.1""".split("\n"))

dark_TEL_up_right_vs_left = set("""LOC107050835.p1	ENSGALT00000095050.1
RASAL2.p1	ENSGALT00000099296.1
PTPN4.p1	ENSGALT00000018933.6
TRAF2.p1	ENSGALT00000067256.2
POLR3B.p1	ENSGALT00000108225.1
GLRX3.p1	ENSGALT00000107907.1
ENOX2.p1	ENSGALT00000050546.2
RPGR.p1	ENSGALT00000094542.1
ZFPM2.p1	ENSGALT00000095082.1
FAM133B.p1	ENSGALT00000015427.6
RBBP6.p1	ENSGALT00000104922.1
DNMBP.p1	ENSGALT00000011823.7
SHPRH.p1	ENSGALT00000103639.1
DOCK10.p1	ENSGALT00000095459.1
EPHA5.p1	ENSGALT00000102752.1
LOC107051050.p1	ENSGALT00000100676.1
DDHD2.p1	ENSGALT00000053432.2
NCOA6.p1	ENSGALT00000071428.2
LCOR.p1	ENSGALT00000068230.2
BRD8.p1	ENSGALT00000092628.1
GRIA3.p1	ENSGALT00000100542.1
NDC1.p1	ENSGALT00000079159.2
DISP1.p1	ENSGALT00000101847.1""".split("\n"))

dark_TEL_up_left_vs_right = set("""ARFGEF3.p1	ENSGALT00000047106.2
FAT3.p1	ENSGALT00000101402.1
YRDC.p1	ENSGALT00000100422.1
TMCC2.p1	ENSGALT00000050468.2
SPATA13.p1	ENSGALT00000102304.1
PLEKHH1.p1	ENSGALT00000063079.2
GOT2.p1	ENSGALT00000089124.2
RASGEF1A.p1	ENSGALT00000034231.5
CENPF.p1	ENSGALT00000084212.2
MAPK8IP1.p1	ENSGALT00000054366.2
PLEKHM3.p1	ENSGALT00000070770.2
USP24.p1	ENSGALT00000059062.2
CTCF.p1	ENSGALT00000002811.4
FLNB.p1	ENSGALT00000055290.2
TBC1D4.p1	ENSGALT00000056657.2
DCBLD2.p1	ENSGALT00000102657.1
KBTBD4.p1	ENSGALT00000013128.6
MYO18A.p1	ENSGALT00000100461.1
STAG2.p1	ENSGALT00000063371.2
IL17RD.p1	ENSGALT00000008827.6
RFX2.p1	ENSGALT00000095394.1
KCNMA1.p1	ENSGALT00000085233.2""".split("\n"))

LIGHT_RET_RIGHT_6H_UP = set("""PRKACB.p1	ENSGALT00000078406.2
ZNF236.p1	ENSGALT00000056093.2
PTPRVP.p1	ENSGALT00000098251.1
RIMS2.p1	ENSGALT00000093663.1
KIF16B.p1	ENSGALT00000102380.1
ARHGAP10.p1	ENSGALT00000016293.5
FNDC3A.p1	ENSGALT00000091251.1
NFE2L1.p1	ENSGALT00000093748.1
BAG3.p1	ENSGALT00000088658.2
KIAA1462.p1	ENSGALT00000100158.1""".split("\n"))


LIGHT_RET_LEFT_6H_UP = set("""STARD4.p1	ENSGALT00000000320.4
CDC42BPA.p1	ENSGALT00000098004.1
JMJD1C.p1	ENSGALT00000077715.2
LAMP2.p1	ENSGALT00000090439.1
ASAP3.p1	ENSGALT00000091877.1
RB1.p1	ENSGALT00000107323.1
KCNQ3.p1	ENSGALT00000071034.2
GARNL3.p1	ENSGALT00000104302.1
NOTCH1.p1	ENSGALT00000003754.7
GOLGB1.p1	ENSGALT00000093670.1
tre-2/USP6,.p1	ENSGALT00000069912.2""".split("\n"))

LIGHT_TEL_RIGHT_6H = set("""ADGRL3.p1	ENSGALT00000057115.2
TNFRSF21.p1	ENSGALT00000079677.2
CHST10.p1	ENSGALT00000027075.6
VRK1.p1	ENSGALT00000018109.6
SPAG17.p1	ENSGALT00000071598.2
AKAP6.p1	ENSGALT00000051855.2
ZNF236.p1	ENSGALT00000056093.2
TRAF3.p1	ENSGALT00000018576.5
ARHGAP12.p1	ENSGALT00000060659.2
KIAA1462.p1	ENSGALT00000104510.1
KIF16B.p1	ENSGALT00000047833.2
CACNA1C.p1	ENSGALT00000107443.1
EEA1.p1	ENSGALT00000076937.2
EP400.p1	ENSGALT00000095730.1
BRAF.p1	ENSGALT00000103955.1
CEP164.p1	ENSGALT00000092171.1
TTC3.p1	ENSGALT00000096299.1
TKT.p1	ENSGALT00000065839.2
GAPVD1.p1	ENSGALT00000063661.2
MGARP.p1	ENSGALT00000090939.1
NPEPPS.p1	ENSGALT00000067237.3
GALE.p1	ENSGALT00000006441.6
PIGN.p1	ENSGALT00000107038.1
COL19A1.p1	ENSGALT00000061315.3""".split("\n"))

LIGHT_TEL_LEFT_6H = set("""ADAMTS18.p1	ENSGALT00000094853.1
DARS.p1	ENSGALT00000050094.2
LZTS2.p1	ENSGALT00000039298.4
ROBO2.p1	ENSGALT00000073443.2
LAMP2.p1	ENSGALT00000090439.1
SVIL.p1	ENSGALT00000104275.1
CAMK2D.p1	ENSGALT00000090825.1
F13A1.p1	ENSGALT00000099036.1""".split("\n"))



LIGHT_RET_LEFT_24H_up = set("""SREBF1.p1	ENSGALT00000084111.2
ATG16L1.p1	ENSGALT00000059856.2
MICAL3.p1	ENSGALT00000094832.1
PKD1.p1	ENSGALT00000080444.2
BECN1.p1	ENSGALT00000083880.2
PPFIBP1.p1	ENSGALT00000091325.1
""".split("\n"))


LIGHT_RET_RIGHT_24H_up = set("""PUM1.p1	ENSGALT00000103445.1
SCAP.p1	ENSGALT00000093336.1
ITPR2.p1	ENSGALT00000066797.2
CAST.p1	ENSGALT00000060443.2
MEGF10.p1	ENSGALT00000023694.6
SPAST.p1	ENSGALT00000084658.2
NFYB.p1	ENSGALT00000067128.2
PCNT.p1	ENSGALT00000097985.1
SEC31A.p1	ENSGALT00000097812.1
ARHGAP21.p1	ENSGALT00000103986.1
VPS33B.p1	ENSGALT00000080045.2
SESN3.p1	ENSGALT00000027810.6
CEP85L.p1	ENSGALT00000024023.6
EP400.p1	ENSGALT00000003682.6
MAP7D3.p1	ENSGALT00000096177.1
EEA1.p1	ENSGALT00000092765.1""".split("\n"))

LIGHT_TEL_LEFT_24H_up = set("""RASAL3.p1	ENSGALT00000072093.2
ATP13A3.p1	ENSGALT00000078141.2
TPR.p1	ENSGALT00000053904.2
UCKL1.p1	ENSGALT00000085040.2
RB1.p1	ENSGALT00000085752.2
LIMS1.p1	ENSGALT00000091197.1
EXOC6B.p1	ENSGALT00000103583.1
PTPRD.p1	ENSGALT00000058492.2
KIF26B.p1	ENSGALT00000093800.1
FAM208B.p1	ENSGALT00000096902.1
SEMA5B.p1	ENSGALT00000062580.2
BTRC.p1	ENSGALT00000049866.2
ERCC6L2.p1	ENSGALT00000020603.5
COG6.p1	ENSGALT00000027523.6
KIAA1462.p1	ENSGALT00000104510.1
ACTR2.p1	ENSGALT00000100056.1
COL5A2.p1	ENSGALT00000054594.2
ARAP3.p1	ENSGALT00000049754.2""".split("\n"))


DARK_LEFT_RET_VS_LIGHT_RET_LEFT_6H_UP = set("""PRKA.p1	ENSGALT00000077603.2
SVIL.p1	ENSGALT00000058082.2
KIF16B.p1	ENSGALT00000093660.1
RAPGEF2.p1	ENSGALT00000076253.2
RBM43.p1	ENSGALT00000099806.1
GRIP2.p1	ENSGALT00000049228.2
ARHGAP21.p1	ENSGALT00000093696.1
MAP4K4.p1	ENSGALT00000056835.2
SLC4A7.p1	ENSGALT00000095666.1
MXRA8.p1	ENSGALT00000104012.1
AFF2.p1	ENSGALT00000095758.1
inorganic.p1	ENSGALT00000067710.2
MEIS1.p1	ENSGALT00000080362.2
ASAP3.p1	ENSGALT00000091877.1
NIPSNAP2.p1	ENSGALT00000083622.2
Hsp110.p1	ENSGALT00000098212.1
KCNQ3.p1	ENSGALT00000071034.2
GARNL3.p1	ENSGALT00000104302.1
RB1.p1	ENSGALT00000107323.1
EMC2.p1	ENSGALT00000071770.2
NAV3.p1	ENSGALT00000104500.1""".split("\n"))


DARK_RET_LEFT_VS_LIGHT_RET_LEFT_24H_UP = set("""EIF4G3.p1	ENSGALT00000099553.1
PRKA.p1	ENSGALT00000077603.2
ANK2.p1	ENSGALT00000096447.1
USP34.p1	ENSGALT00000107765.1
GRIP2.p1	ENSGALT00000049228.2
RAPGEF2.p1	ENSGALT00000076253.2
HIRA.p1	ENSGALT00000088059.2
PPP2R5C.p1	ENSGALT00000086659.2
MARK1.p1	ENSGALT00000099162.1
STK40.p1	ENSGALT00000073558.3
SVIL.p1	ENSGALT00000058082.2
CHST10.p1	ENSGALT00000044322.4
WNK2.p1	ENSGALT00000066447.2""".split("\n"))


LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_6H_up = set("""MYO19.p1	ENSGALT00000039165.4
CHST10.p1	ENSGALT00000027075.6
DENND5A.p1	ENSGALT00000009381.8
PRDM15.p1	ENSGALT00000090664.1
PTPRVP.p1	ENSGALT00000098251.1
phosphatidylcholine--retinol.p1	ENSGALT00000015091.6
AHR.p1	ENSGALT00000063813.2
CADPS2.p1	ENSGALT00000095573.1
HIRA.p1	ENSGALT00000088059.2
VIPAS39.p1	ENSGALT00000017028.7
SLC1A7.p1	ENSGALT00000017363.3
KIF16B.p1	ENSGALT00000102380.1
BCOR.p1	ENSGALT00000036653.4
EXOC6.p1	ENSGALT00000065035.2
HOMER1.p1	ENSGALT00000070212.2
BICD1.p1	ENSGALT00000021097.7
FNDC3A.p1	ENSGALT00000091251.1
NFE2L1.p1	ENSGALT00000093748.1
ABCA9.p1	ENSGALT00000034529.5
UBR2.p1	ENSGALT00000090827.1
ENPP4.p1	ENSGALT00000076315.2
ATP13A3.p1	ENSGALT00000078141.2
KIAA1462.p1	ENSGALT00000100158.1
SPEG.p1	ENSGALT00000107475.1""".split("\n"))


LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_24H_up = set("""WDR26.p1	ENSGALT00000104120.1
DARS.p1	ENSGALT00000050094.2
MKS1.p1	ENSGALT00000088883.2
FRYL.p1	ENSGALT00000096883.1
SACS.p1	ENSGALT00000092028.1
CHST10.p1	ENSGALT00000044322.4
BCOR.p1	ENSGALT00000036653.4
MYO19.p1	ENSGALT00000039165.4
ENPP4.p1	ENSGALT00000076315.2
VPS13D.p1	ENSGALT00000104471.1
ATP11C.p1	ENSGALT00000053632.2
SCHIP1.p1	ENSGALT00000064424.2
COL14A1.p1	ENSGALT00000053447.2
GSN.p1	ENSGALT00000084418.2""".split("\n"))


LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_6H_up = set("""YRDC.p1	ENSGALT00000100422.1
TMCC2.p1	ENSGALT00000050468.2
CEP85L.p1	ENSGALT00000062957.2
CTCF.p1	ENSGALT00000002811.4
MYCBP2.p1	ENSGALT00000107232.1
AKAP6.p1	ENSGALT00000051855.2
ATP13A3.p1	ENSGALT00000101706.1
FCHSD1.p1	ENSGALT00000096534.1
FAT3.p1	ENSGALT00000101402.1
RASGEF1A.p1	ENSGALT00000034231.5
EIF4G1.p1	ENSGALT00000049779.2
LRP1B.p1	ENSGALT00000080533.2
STARD13.p1	ENSGALT00000095934.1
HSPG2.p1	ENSGALT00000105103.1
KIF16B.p1	ENSGALT00000047833.2
SPINT1.p1	ENSGALT00000013800.7
MAPK8IP1.p1	ENSGALT00000054366.2
EEA1.p1	ENSGALT00000076937.2
ABCC3.p1	ENSGALT00000067806.2
HIRA.p1	ENSGALT00000088059.2
NAV2.p1	ENSGALT00000040276.4
IL17RD.p1	ENSGALT00000008827.6
TENM3.p1	ENSGALT00000086090.2
SORL1.p1	ENSGALT00000081956.2
MPDZ.p1	ENSGALT00000092157.1""".split("\n"))

LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_24H_up =  set("""YRDC.p1	ENSGALT00000100422.1
CEP85L.p1	ENSGALT00000062957.2
TMCC2.p1	ENSGALT00000050468.2
SUCO.p1	ENSGALT00000098043.1
LIMS1.p1	ENSGALT00000090376.2
ATP13A3.p1	ENSGALT00000101706.1
R3HCC1L.p1	ENSGALT00000105440.1
RFX2.p1	ENSGALT00000095394.1
FLNB.p1	ENSGALT00000055290.2
ARHGAP21.p1	ENSGALT00000093696.1
CENPF.p1	ENSGALT00000084212.2
MAPK8IP1.p1	ENSGALT00000054366.2
NAV1.p1	ENSGALT00000095619.1
IL11RA.p1	ENSGALT00000057968.2
DCP2.p1	ENSGALT00000000283.7
AKAP6.p1	ENSGALT00000051855.2
FGD3.p1	ENSGALT00000100503.1
USP24.p1	ENSGALT00000059062.2
NAV2.p1	ENSGALT00000040276.4
HIRA.p1	ENSGALT00000088059.2
EXOSC8.p1	ENSGALT00000027544.6
Diego.p1	ENSGALT00000091573.1
SPRED1.p1	ENSGALT00000102477.1
TRIP12.p1	ENSGALT00000004623.6
PPP2R5C.p1	ENSGALT00000108074.1
GRIPAP1.p1	ENSGALT00000094307.1""".split("\n"))


### now we have loaded all the DE genes into sets with their current
# and convetted names. lets compare:

cond = """dark_TEL_left_up
dark_RET_up_right_vs_left
dark_RET_up_left_vs_right
dark_TEL_up_right_vs_left
dark_TEL_up_left_vs_right
LIGHT_RET_RIGHT_6H_UP
LIGHT_RET_LEFT_6H_UP
LIGHT_TEL_RIGHT_6H
LIGHT_TEL_LEFT_6H
LIGHT_RET_LEFT_24H_up
LIGHT_RET_RIGHT_24H_up
LIGHT_TEL_LEFT_24H_up
DARK_LEFT_RET_VS_LIGHT_RET_LEFT_6H_UP
DARK_RET_LEFT_VS_LIGHT_RET_LEFT_24H_UP
LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_6H_up
LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_24H_up
LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_6H_up
LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_24H_up""".split()

# add all the de conditions to a dictionary
conditions_dict = dict()

conditions_dict['dark_TEL_left_up'] = dark_TEL_left_up
conditions_dict['dark_RET_up_right_vs_left'] = dark_RET_up_right_vs_left
conditions_dict['dark_RET_up_left_vs_right'] = dark_RET_up_left_vs_right
conditions_dict['dark_TEL_up_right_vs_left'] = dark_TEL_up_right_vs_left
conditions_dict['dark_TEL_up_left_vs_right'] = dark_TEL_up_left_vs_right
conditions_dict['LIGHT_RET_RIGHT_6H_UP'] = LIGHT_RET_RIGHT_6H_UP
conditions_dict['LIGHT_RET_LEFT_6H_UP'] = LIGHT_RET_LEFT_6H_UP
conditions_dict['LIGHT_TEL_RIGHT_6H'] = LIGHT_TEL_RIGHT_6H
conditions_dict['LIGHT_TEL_LEFT_6H'] = LIGHT_TEL_LEFT_6H
conditions_dict['LIGHT_RET_LEFT_24H_up'] = LIGHT_RET_LEFT_24H_up
conditions_dict['LIGHT_RET_RIGHT_24H_up'] = LIGHT_RET_RIGHT_24H_up
conditions_dict['LIGHT_TEL_LEFT_24H_up'] = LIGHT_TEL_LEFT_24H_up
conditions_dict['DARK_LEFT_RET_VS_LIGHT_RET_LEFT_6H_UP'] = DARK_LEFT_RET_VS_LIGHT_RET_LEFT_6H_UP
conditions_dict['DARK_RET_LEFT_VS_LIGHT_RET_LEFT_24H_UP'] = DARK_RET_LEFT_VS_LIGHT_RET_LEFT_24H_UP
conditions_dict['LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_6H_up'] = LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_6H_up
conditions_dict['LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_24H_up'] = LEFT_DARK_RET_VS_LIGHT_RET_RIGHT_24H_up
conditions_dict['LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_6H_up'] = LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_6H_up
conditions_dict['LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_24H_up'] = LEFT_DARK_TEL_VS_LIGHT_TEL_RIGHT_24H_up



#########################################################
# set up a dic of all the comparisons. 
comparisons_dict = dict()
# pairwise
for i in cond:
    for j in cond:
        if i == j: continue
        #print("%s_COMPARE_%s_intersection = %s.intersection(%s)\n" %(i,j,i,j))
        #print("%s_COMPARE_%s_intersection = %s.intersection(%s)\n" %(i,j,i,j))
        cond1 = conditions_dict[i.rstrip()]
        if j in conditions_dict:
            cond2 = conditions_dict[j.rstrip()]
        else:
            print("count not find: ", j)
            continue
        comp_name =  "%s_COMPARE_%s_intersection" % (i, j)
        result  = cond1.intersection(cond2)
        comparisons_dict[comp_name] = result

# 3 conditions
for i in cond:
    for j in cond:
        if i == j: continue
        for k in cond:
            if k == i: continue
            if k == j: continue
            #print("%s_COMPARE_%s_intersection = %s.intersection(%s)\n" %(i,j,i,j))
            #print("%s_COMPARE_%s_intersection = %s.intersection(%s)\n" %(i,j,i,j))
            cond1 = conditions_dict[i.rstrip()]
            cond2 = conditions_dict[j.rstrip()]
            cond3 = conditions_dict[k.rstrip()]
            comp_name =  "%s_COMPARE_%s_and_%s_intersection" % (i, j, k)
            result  = cond1.intersection(cond2, cond3)
        comparisons_dict[comp_name] = result

# 4 conditions. 
for i in cond:
    for j in cond:
        if i == j: continue
        for k in cond:
            if k == i: continue
            if k == j: continue
            for t in cond:
                if t == i: continue
                if t== j: continue
                if t == k: continue
                #print("%s_COMPARE_%s_intersection = %s.intersection(%s)\n" %(i,j,i,j))
                #print("%s_COMPARE_%s_intersection = %s.intersection(%s)\n" %(i,j,i,j))
                cond1 = conditions_dict[i.rstrip()]
                cond2 = conditions_dict[j.rstrip()]
                cond3 = conditions_dict[k.rstrip()]
                cond4 = conditions_dict[t.rstrip()]
                comp_name =  "%s_COMPARE_%s_and_%s_and_%s_intersection" % (i, j, k, t)
                result  = cond1.intersection(cond2, cond3, cond4)
            comparisons_dict[comp_name] = result

comparisons = open("DE_comparisonsDE_gene_IN_COMMON_.txt", "w")

####################################################
# write out all the common comparisons

comparisons.write("#PREVIUS_GENE_OF_INTEREST\tNUM_IN_COMMON\tcondition1\tOTHER_conditions\tGENE (with converted_name)\n")
for name, results in comparisons_dict.items():
    prev_GOI = "NO"
    name = name.replace("_COMPARE_", "\t")
    temp = ""
    for i in results:
        new_name = i.split("\t")[1]
        if new_name in old_gene_of_interest:
            prev_GOI = "YES"
        temp = temp + " " + i.replace("\t", ": ") + ", "
    data = "%s\t%d\t%s\t%s\n" % (prev_GOI, len(results), name, temp)
    comparisons.write(data)

comparisons.close()

##################################################
# set up some comparisions to get the differences:

#########################################################
# set up a dic of all the comparisons. 
comparisons_dict = dict()
# pairwise
for i in cond:
    for j in cond:
        if i == j: continue
        #print("%s_COMPARE_%s_difference = %s.difference(%s)\n" %(i,j,i,j))
        #print("%s_COMPARE_%s_difference = %s.difference(%s)\n" %(i,j,i,j))
        cond1 = conditions_dict[i.rstrip()]
        if j in conditions_dict:
            cond2 = conditions_dict[j.rstrip()]
        else:
            print("count not find: ", j)
            continue
        comp_name =  "%s_COMPARE_%s_difference" % (i, j)
        result  = cond1.difference(cond2)
        comparisons_dict[comp_name] = result

# 3 conditions
for i in cond:
    for j in cond:
        if i == j: continue
        for k in cond:
            if k == i: continue
            if k == j: continue
            #print("%s_COMPARE_%s_difference = %s.difference(%s)\n" %(i,j,i,j))
            #print("%s_COMPARE_%s_difference = %s.difference(%s)\n" %(i,j,i,j))
            cond1 = conditions_dict[i.rstrip()]
            cond2 = conditions_dict[j.rstrip()]
            cond3 = conditions_dict[k.rstrip()]
            comp_name =  "%s_COMPARE_%s_and_%s_difference" % (i, j, k)
            result  = cond1.difference(cond2, cond3)
        comparisons_dict[comp_name] = result

# 4 conditions. 
for i in cond:
    for j in cond:
        if i == j: continue
        for k in cond:
            if k == i: continue
            if k == j: continue
            for t in cond:
                if t == i: continue
                if t== j: continue
                if t == k: continue
                #print("%s_COMPARE_%s_difference = %s.difference(%s)\n" %(i,j,i,j))
                #print("%s_COMPARE_%s_difference = %s.difference(%s)\n" %(i,j,i,j))
                cond1 = conditions_dict[i.rstrip()]
                cond2 = conditions_dict[j.rstrip()]
                cond3 = conditions_dict[k.rstrip()]
                cond4 = conditions_dict[t.rstrip()]
                comp_name =  "%s_COMPARE_%s_and_%s_and_%s_difference" % (i, j, k, t)
                result  = cond1.difference(cond2, cond3, cond4)
            comparisons_dict[comp_name] = result

comparisons = open("DE_comparisons_DIFFERENT.txt", "w")

####################################################
# write out all the common comparisons

comparisons.write("#NUM_DIFFERENT\tcondition1\tother_conditions\tGENEs (with converted names)\n")
for name, results in comparisons_dict.items():
    name = name.replace("_COMPARE_", "\t")
    prev_GOI = "NO"
    temp = ""
    for i in results:
        if new_name in old_gene_of_interest:
            prev_GOI = "YES"
        temp = temp + " " + i.replace("\t", ": ") + ", "
    data = "%s\t%d\t%s\t%s\n" % (prev_GOI, len(results), name, temp)
    comparisons.write(data)

comparisons.close()



############################################
# count the genes the occur in multiple conds

gene_counter = defaultdict(int)
gene_to_conditions = defaultdict(str)
gene_to_conditions_count = defaultdict(int)


f_out = open("genes_conditions_found_in.txt", "w")


for name, results in conditions_dict.items():
    for i in results:
        #print(i)
        gene_counter[i] += 1
        gene_to_conditions[i] += name + ", "

f_out.write("#gene\tnewname\tnum_of_conditions_in\tconditions\n")
for gene, condition in gene_to_conditions.items():
    number = gene_counter[gene]
    data = "%s\t%d\t%s\n" % (gene, number, condition)
    f_out.write(data)

f_out.close()
    


            
    
		
