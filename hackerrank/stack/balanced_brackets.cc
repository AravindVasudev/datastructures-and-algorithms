#include <bits/stdc++.h>

using namespace std;

string isBalanced(string str) {
    // Complete this function
    stack<char> s;
    map<char, char> m;
    
    m['('] = ')';
    m['{'] = '}';
    m['['] = ']';
    
    for (char c : str) {
        if (c == '(' || c == '[' || c == '{') s.push(c);
        else if (s.empty() || c != m[s.top()]) return "NO";
        else s.pop();
    }
    
    return s.empty() ? "YES" : "NO";
}

int main() {
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        string s;
        cin >> s;
        string result = isBalanced(s);
        cout << result << endl;
    }
    return 0;
}
