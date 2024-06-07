# Bannister-RDD
## "If I can do it, you can (just) do it too!" - Identification/Falsification of the Bannister Effect using RDD
An empirical investigation of the 'Bannister' effect.
[Bannister Spec (Draft)](https://felixreichel.com/bannister_spec.pdf)

### Preliminary-Results of (2):

#### (i):
A Bannister-like effect exists for the 5k if one
chooses the 2nd most plausible (arbitrary) threshold time of 800s, assuming it causes a Bannister-like effect. (13m+20s)

#### (ii): 
There are no significant 'jumps' in 5000m and 10000m running times where one would expect them to be plausible (e.g., 27' for 10k, etc.). 
Thus, my (preliminary!) conclusion is that Bannister effect remains a psychological myth and seems to be statistically significant at the 3% level. ;)

### (1) Observational Unit: One Mile World Record Progression Times (also known as the "Bannister" Effect)

#### RDD:

![Image](bannister/simp_rdd2_plot)

#### Kernel Reg.:

![Image](bannister/kernel_reg)

### (2) Observational Unit: New Observational unit

e.g., other record time progressions (i) in running (ii) over various distances (iii) in other sports providing
similar threshold values (with associated beliefs that no person can achieve better stated in a pre-period)
#### (i) 5k Bannister like threshold defined as 800 seconds yields:

![Image](10k_and_5k_bannister_like_progression_fx_question/5000m_rdd_first_date_below_800sec)

#### (i) 10k Bannister like threshold defined as 27 minutes yields:

![Image](10k_and_5k_bannister_like_progression_fx_question/10000m_rdd_first_date_below_27mins)

#### More interestingly, the RDD of 10k times using the 'real' Bannister Date yields:

![Image](10000m_rdd_bannister_date_treat)

It cannot be said if this hints towards a general steeper progression around this record time or fully dispels the existence of a Bannister effect.

Most interestingly, plotting an RDD of 5k record progression around the Bannister threshold shows no 'jump' at all.

Therefore, many other distances as observational units should be used (e.g., 800m, 3000m, 2000m, 21k).

### (3) Spillovers -> SUTVA Violation:

DiD (e.g., de-trending times by general time progression) and IV instrumenting the 
relevant Threshold Th and Y0 (where Threshold is associated with Bannister-like beliefs in a pre-period e.g., by assumption a sharp limit).

### (4) Extension 1: Estimating the degree of 'Bannister beliefs', if applicable for various other sports (e.g., ski-jumping).
