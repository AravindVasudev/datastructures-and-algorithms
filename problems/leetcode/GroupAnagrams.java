class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

      for (String str : strs) {
        String sortedStr = sortStr(str);
        if (map.containsKey(sortedStr)) {
          map.get(sortedStr).add(str);
        } else {
          List<String> list = new ArrayList<>();
          list.add(str);

          map.put(sortedStr, list);
        }
      }

      return new ArrayList<List<String>>(map.values());
    }

    private String sortStr(String s) {
      char[] sArr = s.toCharArray();
      Arrays.sort(sArr);
      return new String(sArr);
    }
}
