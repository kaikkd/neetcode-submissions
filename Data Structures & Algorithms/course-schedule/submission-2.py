class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        q = deque()

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        complete = 0
        while q:
            cur_course = q.popleft()
            complete += 1
            for nxt in graph[cur_course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return complete == numCourses