# Example implementation of comparison of 2 groups using
# the method detailed in: The Use of Thompson Sampling to Increase estimation precision
import libs.base as base

# Get exsiting variance
var = base.Variance(self.get_theta(key="Treatment"))

# Update the variance
var.update(self.reward["value"])

# Store updated variance
self.set_theta(var, key="Treatment", value=self.action["Treatment"])