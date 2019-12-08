class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> uniqueEmails = new HashSet<>();
        
        for (String email : emails) {
            String[] emailArr = email.split("@", 2);
            uniqueEmails.add(emailArr[0].split("\\+")[0].replace(".", "") + "@" + emailArr[1]);
        }
        
        return uniqueEmails.size();
    }
}