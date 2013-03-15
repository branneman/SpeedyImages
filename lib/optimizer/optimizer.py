class optimizer:

    def checkDependencies(self):

        tools = []

        for tool in self.tools:
            if not tool().checkDependency():
                del self.tools[self.tools.index(tool)]
                tools.append(tool)

        return tools
