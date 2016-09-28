import numpy as np
import pandas as pd
import scipy.stats as stats

# rolling dice and null hypothesis is the dice is fair or not
# it looks fitness of data
observed = np.array([22, 24, 38, 30, 46, 44])
expected = np.array([1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0]) * np.sum(observed)

(t, p) = stats.chisquare(observed, expected, ddof=1)
print 'Test t=%f p-value = %f' % (t, p)

alpha = 0.05  # significance level

if p <= alpha:
    # we reject null hypothesis
    print 'Null hypothesis (dice is fair) is unlikely to except'
else:
    # we reject alternative hypothesis
    print 'Null hypothesis (dice is fair) cannot be rejected'


# another example
# this example is based on: http://www.simafore.com/blog/bid/54885/5-simple-steps-to-apply-chi-square-test-for-business-analytics
# Null Hypothesis is variables are independent

# data is saved as csv file in dataset.csv
df = pd.read_csv('./dataset/dataset.csv',header=1,sep=';',index_col=0)
# after reading data only to do is use chi square test for independence
# stats package have chi2_contingency method to check chi-squared test for independence

chiStats = stats.chi2_contingency(observed= df)
print 'Test t=%f p-value=%f' % (chiStats[0], chiStats[1])
#critical value = 0.1
alpha = 0.05
critical_value = crit = stats.chi2.ppf(q = 1 - alpha, # Find the critical value for 95% confidence*
                      df = chiStats[2]) #degree of freedom

observed_chi_val = chiStats[0]
#if observed chi-square < critical chi-square, then variables are not related
#if observed chi-square > critical chi-square, then variables are not independent (and hence may be related).

if observed_chi_val <= critical_value:
    # observed value is not in critical area therefore we accept null hypothesis
    print 'Null hypothesis cannot be rejected (variables are not related)'
else:
    # observed value is in critical area therefore we reject null hypothesis
    print 'Null hypothesis cannot be excepted (variables are not independent)'