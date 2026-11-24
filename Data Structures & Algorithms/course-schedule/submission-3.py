class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        complete = 0
        while q:
            cur = q.popleft()
            complete += 1
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return complete == numCourses