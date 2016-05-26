import libs.thompson as thmp
proportionList = thmp.BBThompsonList(
		self.get_theta(key="Treatment"), ["1","2","3"])
self.action["Treatments"] = proportionList.thompson()