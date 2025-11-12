class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Topological Sort
        if it has a cycle it is impossible to finish the courses

        ai->bi
        if bi->ai in graph then we can't complete 
            hypothetically impossible

       1-4
        
        """
        graph = collections.defaultdict(list)
        actualNodes = set()
        seen = set()
        q = deque()
        indegrees = [0]*numCourses
        for u,v in prerequisites:
            actualNodes.add(u)
            actualNodes.add(v)
            graph[v].append(u)
            indegrees[u] += 1
        for v,indeg in enumerate(indegrees):
            if v in actualNodes and indeg == 0 : 
                q.append(v)
        #print(indegrees)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0 :
                    q.append(nei) 
        #print(count)
        return not prerequisites or len(actualNodes) == count
