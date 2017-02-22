class Cell:
    def __init__(self,dependency,bydependency):
        self.mDependency = dependency
        self.mByDependency = bydependency

    def setDependencey(self,dependency):
        self.mDependency = dependency
    def setByDependencey(self,bydependency):
        self.mByDependency = bydependency

    def getDependencey(self):
        return self.mDependency
    def getByDependencey(self):
        return self.mByDependency