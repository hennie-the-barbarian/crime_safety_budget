PEW RESEARCH CENTER
Wave 100 American Trends Panel 
Dates: Nov. 30 - Dec. 12, 2021
Mode: Web
Sample: Subsample with Black and Hispanic oversample from KnowledgePanel
Language: English and Spanish
N=14,497

***************************************************************************************************************************
NOTES

The sample consisted of a general population ATP subsample that included all ATP panel members who identified Black or Hispanic.
The sample also included a census of all KnowledgePanel members that identified as Black and a subsample of KnowledgePanel members that identified as Hispanic.
Hispanic KnowledgePanel members that responded to ATP W86 National Survey of Latinos (NSL) were sampled with certainty. Black KnowledgePanel members that responded to ATP W97 Black Voices Survey were sampled with certainty. 

The Wave 100 dataset contains the following created variables. SPSS syntax for how these variable were computed is included below in the SYNTAX section.
 
PRIMARY_LANGUAGE_W100
netpos
netneg
BIO54_count_W100
BIO54_count_dropG_W100

Variable PRIMARY_LANGUAGE_W100 was computed for all Hispanic respondents in W100 to classify them as English dominant, bilingual or Spanish dominant. 
Netpos and netneg are variables created to capture whether respondents chose “yes” to any of the positive or negative items in EDSTEM3, which asked their most recent school experience in science, technology, engineering and mathematics.
BIO54_count_W100 is a variable created to capture the number of items respondents said “happened to them recently” or “in the past, but not recently” from the BIO54 series, which asked about experiences getting healthcare. 
BIO54_count_dropG_W100 is a count variable excluding item G, which was asked of only women.

For a small number of respondents with high risk of identification, certain values have been randomly swapped with those of lower risk cases with similar characteristics.


***************************************************************************************************************************
WEIGHTS 


WEIGHT_W100 is the weight for the sample. Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************
Releases from this survey:

April 7, 2022 "Black Americans’ Views of and Engagement With Science"
https://www.pewresearch.org/science/2022/04/07/black-americans-views-of-and-engagement-with-science/

June 14, 2022 "Hispanic Americans’ Trust in and Engagement With Science"
https://www.pewresearch.org/science/2022/06/14/hispanic-americans-trust-in-and-engagement-with-science/

November 10, 2022 "Americans report more engagement with science news than in 2017"
https://www.pewresearch.org/fact-tank/2022/11/10/americans-report-more-engagement-with-science-news-than-in-2017/

***************************************************************************************************************************
SYNTAX

**PRIMARY_LANGUAGE

compute Spnspk=LAN1_W100.
compute Spnrd=LAN2_W100.
compute Engspk=LAN3_W100.
compute Engrd=LAN4_W100.
EXECUTE.
 
recode Spnspk Spnrd Engspk Engrd (1=2)(2=1) (3 thru 4=0) (99=SYSMIS).
 
compute English = Engspk + Engrd.
compute Spanish = Spnspk + Spnrd.
EXECUTE.
 
compute Language = English - Spanish.
compute PRIMARY_LANGUAGE_W100 = Language.
EXECUTE.
 
recode PRIMARY_LANGUAGE_W100 (2,3,4=1)(-1,0,1=2)(-2,-3,-4=3) (SYSMIS=99).
if missing(LAN1_W100) PRIMARY_LANGUAGE_W100=$sysmis.
ADD VALUE LABELS PRIMARY_LANGUAGE_W100 (1) English dominant (2) Bilingual (3) Spanish dominant (99) Refused on at least one LAN1-4.
VARIABLE LABELS PRIMARY_LANGUAGE_W100 Primary language of respondent.
EXECUTE.

**EDSTEM3 Yes to any three

COMPUTE netpos =5. 
if sysmis (EDSTEM3_A_W100) netpos=999.
IF (EDSTEM3_A_W100 =1) OR (EDSTEM3_C_W100 =1) OR (EDSTEM3_F_W100 =1) netpos =1.
IF (EDSTEM3_A_W100 =2) AND (EDSTEM3_C_W100 =2) AND (EDSTEM3_F_W100 =2) netpos =2.
IF (EDSTEM3_A_W100 =99) OR (EDSTEM3_C_W100 =99) OR (EDSTEM3_F_W100 =99) netpos =9.
fre netpos.

COMPUTE netneg =5. 
if sysmis (EDSTEM3_A_W100) netneg=999.
IF (EDSTEM3_B_W100 =1) OR (EDSTEM3_D_W100 =1) OR (EDSTEM3_E_W100 =1) netneg =1.
IF (EDSTEM3_B_W100 =2) AND (EDSTEM3_D_W100 =2) AND (EDSTEM3_E_W100 =2) netneg =2.
IF (EDSTEM3_B_W100 =99) OR (EDSTEM3_D_W100 =99) OR (EDSTEM3_E_W100 =99) netneg =9.
fre netneg.

variable labels netpos "Yes to any EDSTEM3 positive items (EDSTEM3A,C,F)".
variable labels netneg "No to any  EDSTEM3 negative items (EDSTEM3B,D,E)".
value labels netpos netneg 1 "yes to any of 3" 2 "No to all 3" 9 "Refused to any of 3"  999 "Not asked".

**BIO54 COUNT VARIABLE
**general count

count BIO54_count_W100=BIO54_a_W100 to BIO54_g_W100 (1,2).

**at least one refused gets dropped into no answer

if (BIO54_a_W100=99 or BIO54_b_W100=99 or BIO54_c_W100=99 or BIO54_d_W100=99 or BIO54_e_W100=99 or BIO54_f_W100=99 or BIO54_g_W100=99) BIO54_count_W100=99.

variable labels BIO54_count_W100 "Count of how many items in BIO54 have happened to respondent recently or in the past (BIO54=1,2)".

**BIO54 dropping last item (asked only of women)
**general count

count BIO54_count_dropG_W100=BIO54_a_W100 to BIO54_f_W100 (1,2).

**at least one refused gets dropped into no answer

if (BIO54_a_W100=99 or BIO54_b_W100=99 or BIO54_c_W100=99 or BIO54_d_W100=99 or BIO54_e_W100=99 or BIO54_f_W100=99) BIO54_count_dropG_W100=99.

variable labels BIO54_count_dropG_W100 "Count of how many items in BIO54 have happened to respondent recently or in the past, dropping item G (BIO54=1,2)".
