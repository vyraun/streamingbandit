# Thompson sampling for bernoulli 
# See "old" tools.py
from libs.base import *

class BBThompsonList(List):
    """ Class to draw decisions using a Bernoulli Bandit Thompson sampler.
    """
    def __init__(self, objects, value_names):
        """ Create an instance of a BB Thompson Sampler.

        :param dict objects: A dict of dict of thetas (which should be \
        proportions, see documentation of Proportions on how it should look like.)
        :param list value_names: A list with the possible value names for the \
        actions
        """
        super(BBThompsonList, self).__init__(objects, Proportion, value_names)

    # Summary is done with AB setrewards
    def thompson(self):
        """ Draw decision using the Bernoulli Bandit Thompson sampler.

        :returns string choice: The choice of action that's made.
        """
        min_prob = 0
        choice = None
        for key, obj in self.base_list.items():
            theta = obj.get_dict()
            a = float(theta['p']) * int(theta['n'])
            b = int(theta['n']) - a
            draw = np.random.beta(a,b)
            if draw > min_prob:
                min_prob = draw
                # We want to return something of the form of an action choice.
                # Do we return 
                choice = key
        return choice
        



class ThompsonVarList(List):
    """ Class to allocate observations in 2 group a within subjects desing
    such as to maximize the precision of the estimated effect size 
    (assuming unequal variance of the two groups)
    """
    
    def __init__(self, objects, value_names):
        """ Create instance of a BB Thompson Variance Sampler
        by creating a variance list
        """
        super(BBThompsonList, self).__init__(objects, Variance, value_names)


    def experimentThompson(self):
        """ Obtain draw and allocate to minimize estimation precision
        """
        max_criterion = 0
        choice = None
        for key, obj in self.base_list.items():

            # Get the objects
            theta = obj.get_dict()

            # Get sum of squares and N
            SS = float(theta['s'])            
            n = int(theta['n']) 
            
            # Computer criterion based on posterior variance
            criterion = self._postVariance(SS,n) / n
            
            # Return condition with hightest criterion
            if criterion > max_criterion:
                max_criterion = draw
                choice = key
        return choice
  
      
    def _postVariance(self, SS, n):
        """ Obtain a sample from the posterior variance given 
        the sum of squares (SS) and the sample size n
        """ 
        s2 = SS / np.random.chisquare(n-1)
        return(math.sqrt(s2))
    
    
    def _postMean(self, m, SS, n):
        """ Obtain a sample from the posterior mean of a normal normal
        model (CURRNTLY NOT USED)
        """
        s2 = self._postVariance(SS, n)
        mean = np.random.normal(m, (math.sqrt(s2)/ math.sqrt(n)))
        return(mean)
    