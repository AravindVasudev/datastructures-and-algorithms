import java.util.*;

public class NaughtyStudents {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        List<String> punishmentList = Arrays.asList(kb.next().split(","));
        Set<String> punishmentSet = new HashSet<>(punishmentList);

        int iterationCount = kb.nextInt();
        Map<String, List<String>> relationMap = new HashMap<>();
        String[] relation;
        for (int i = 0; i < iterationCount; i++) {
            relation = kb.next().split("->");

            if (punishmentSet.contains(relation[0])) {
                punishmentSet.add(relation[1]);
            }

            if (relationMap.containsKey(relation[1])) {
                punishmentSet.addAll(relationMap.get(relation[1]));
            }

            if (relationMap.containsKey(relation[0])) {
                relationMap.get(relation[0]).add(relation[1]);
            } else {
                relationMap.put(relation[0], new ArrayList<>(Arrays.asList(relation[1])));
            }
        }

        System.out.println(punishmentSet);
    }
}
