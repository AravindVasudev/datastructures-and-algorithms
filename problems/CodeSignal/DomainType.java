String[] domainType(String[] domains) {   
    Map<String, String> domainMap = new HashMap<>(4);
    
    // Populating
    domainMap.put("com", "commercial");
    domainMap.put("org", "organization");
    domainMap.put("net", "network");
    domainMap.put("info", "information");
    
    String[] labels = new String[domains.length];
    for (int i = 0; i < domains.length; i++) {
        String[] curDomainArr = domains[i].split("\\.");
        labels[i] = domainMap.getOrDefault(curDomainArr[curDomainArr.length - 1], "");
    }
    
    return labels;
}