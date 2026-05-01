class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list) # {pre: [course]}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            courses[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        res = []

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            pre = q.popleft()
            numCourses -= 1
            res.append(pre)

            for course in courses[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return res if numCourses == 0 else []

