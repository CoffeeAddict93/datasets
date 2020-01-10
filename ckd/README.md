# Chronic kidney disease dataset

From <https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease>

The file `original/chronic_kidney_disease_full.arff` contains the full source information at the top of the file.

The data are blood tests and other measures from patients with and without CKD.
There are 400 rows, one per patient; these are patients seen over a period of
about two months at some point before July 2015, in a hospital in Tamil Nadu,
India; maybe [Apollo Reach
Karaikudi](https://www.purplehealth.com/10765-DrSoundarapandianPS).

Of the 400 rows, 250 correspond to patients *with* CKD and the remaining 150
rows correspond to patients *without* CKD.  This information is in the "Class"
column of the dataset.

L. Jerlin Rubini created the data, with the collaboration of Doctors P.
Soundarapandian and P. Eswaran. See the original file or the link above for
details.

See the [citation request](https://archive.ics.uci.edu/ml/citation_policy.html)
for the original website policy for citing datasets; please do follow that if you publish an analysis of these data.

The file `chronic_kidney_disease_full.arff` is a patched version of the
original at `original/chronic_kidney_disease_full.arff`.  See the output of
`diff` for details.  The changes are because the [ARFF
file](https://www.cs.waikato.ac.nz/ml/weka/arff.html) appears to be mal-formed,
and therefore causes errors when reading with Scipy.  Specifically:

* The value in line 399, starting `75,70`, has an extra missing field specified
  with double commas: `,,`.

The [Foundations of Data Science](https://www.inferentialthinking.com) (FDS) [version of this file](https://www.inferentialthinking.com/data/ckd.csv) differs from the processed version (`processed/ckd_full.csv`) in these ways:

* The FDS version recodes the last column, `Class`, to 0 for "notckd" and 1 for
  "ckd".
* The FDS version has dropped all rows with NA, with something like
  `df.dropna(how='any')`.
* There is one row that is not present in the FDS version, for reasons that
  weren't obvious to me.  It corresponds to line 371 in the input ARFF file,
  and begins with `60,90,1.010,3`.

The file `processed/ckd_clean.csv` is like the FDS version, but retaining the
extra row.
