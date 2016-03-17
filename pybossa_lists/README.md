# Pybossa_lists

This directory contains the results of our review of lists that have been loaded into Pybossa. 

In the case of the student reviews, we have a column labeled "student confidence." Here's how that works:
 - If the students all agree, and they don't choose "not_known," then confidence is 1
 - If they either choose one option or "not known," then the answer they have selected is shown, and then the confidence is the fraction of them that selected it. So, if two students say it is a trawler, and one says "not known," then it will be labeled as a trawler with 0.66 confidence
 - If the students disagree, then the confidence is .3 or lower. The actual calculation is .3 * (# reponses without "not_known") / number of responses
 - If they all say "not_known," the confidence is 0
 - If there is not a confidence column, then we had only one reviewer for the list
