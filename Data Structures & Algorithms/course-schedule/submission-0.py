class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1
        
        complete = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            index = q.popleft()
            complete += 1
            for nxt in graph[index]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return complete == numCourses