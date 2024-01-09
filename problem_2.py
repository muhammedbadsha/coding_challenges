class graph:
    def __init__(self,edge) -> None:
        self.edge=edge
        self.dict={}
        for start,end in self.edge:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start]=[end]
    
    def display(self):
        for key in self.dict:
            print(key,self.dict[key])

    def findLocation(self,start,end,path=[]):
        path=path+[start]
        if start == end:
            return [path]
        if start not in self.dict:
            return []
        paths=[]
        for i in self.dict[start]:
            if i not in path:
                new_path=self.findLocation(i,end,path)
                for j in new_path:
                    paths.append(j)
        return paths
    
    def findSmallest(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if start not in self.dict:
            return []
        paths=None
        for node in self.dict[start]:
            if node not in path:
                new_path=self.findSmallest(node,end,path)
                if new_path :
                    if paths is None or len(new_path)<len(paths):
                        paths=new_path
                    
        return paths

routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]
g=graph(routes)
print(g.findLocation("Mumbai","New York"))
print(g.findSmallest("Mumbai","New York"))

# Output

# [['Mumbai', 'Paris', 'Dubai', 'New York'], ['Mumbai', 'Paris', 'New York'], ['Mumbai', 'Dubai', 'New York']]

# ['Mumbai', 'Paris', 'New York']