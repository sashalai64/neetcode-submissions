class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list) # {pre: course}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            courses[pre].append(course)
            indegree[course] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                numCourses -= 1
        
        while q:
            for _ in range(len(q)):
                pre = q.popleft()

                for course in courses[pre]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        q.append(course)
                        numCourses -= 1
        
        return numCourses == 0
        




