// https://leetcode.com/problems/course-schedule/
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int edge = 0; edge < prerequisites.length; edge++) {
            graph[prerequisites[edge][0]].add(prerequisites[edge][1]);
        }
        
        System.out.println(Arrays.toString(graph));
        
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < numCourses; i++) {
            Set<Integer> recurStack = new HashSet<>();
            if (!seen.contains(i) && hasCycle(graph, seen, recurStack, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    private boolean hasCycle(List<Integer>[] graph, Set<Integer> seen, Set<Integer> recurStack, int curNode) {
        if (recurStack.contains(curNode)) {
            return true;
        }
        
        if (seen.contains(curNode)) {
            return false;
        }
        
        seen.add(curNode);
        recurStack.add(curNode);

        for (int edge : graph[curNode]) {
            if (hasCycle(graph, seen, recurStack, edge)) {
                return true;
            }
        }
        
        recurStack.remove(curNode);
        return false;
    }
}
