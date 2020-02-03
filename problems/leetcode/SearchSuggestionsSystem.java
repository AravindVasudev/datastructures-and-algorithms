// https://leetcode.com/problems/search-suggestions-system/
class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        List<List<String>> result = new ArrayList<>();
        int searchWordLen = searchWord.length();
        Arrays.sort(products);

        for (int i = 0; i < searchWordLen; i++) {
            List<String> curResult = new ArrayList<>();
            String curSearchWord = searchWord.substring(0, i + 1);
            for (int j = 0; j < products.length && curResult.size() < 3; j++) {
                if (products[j].startsWith(curSearchWord)) {
                    curResult.add(products[j]);
                }
            }

            result.add(curResult);
        }

        return result;
    }
}
