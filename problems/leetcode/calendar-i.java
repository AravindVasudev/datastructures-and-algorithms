class MyCalendar {
    TreeMap<Integer, Integer> calendar = new TreeMap<>();
    
    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start);
        Integer next = calendar.ceilingKey(start);
        
        if ((prev == null || calendar.get(prev) <= start) &&
            (next == null || next >= end)) {
            calendar.put(start, end);
            return true;
        }
        
        return false;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
