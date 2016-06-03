# Import the thompson sampling libraries
import libs.thompson as thmp

# Create a Thompson sampling variance list
# Should pass a list of variances
varList = thmp.ThompsonVarList(self.get_theta(key="Treatment"), ["1","2"])

# Select the action with the highest posterior variance
self.action["Treatment"] = varList.experimentThompson()