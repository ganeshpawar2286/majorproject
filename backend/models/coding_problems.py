"""
Curated Multi-Language Problem Bank & Code Boilerplate Stubs for PrepWise AI Coding Assessment.
Supports Python, Java, C, C++, SQL, DSA, and Web Development.
"""

CODING_PROBLEMS = [
    {
        "id": "py-two-sum",
        "title": "Two Sum Target Finder",
        "subject": "Python",
        "category": "DATA-STRUCTURES",
        "difficulty": "Easy",
        "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.",
        "input_format": "nums = [2, 7, 11, 15], target = 9",
        "output_format": "[0, 1]",
        "starter_code": {
            "python": "def two_sum(nums, target):\n    # Write your Python solution here\n    hash_map = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in hash_map:\n            return [hash_map[diff], i]\n        hash_map[num] = i\n    return []\n\n# Test invocation\nprint(two_sum([2, 7, 11, 15], 9))",
            "java": "import java.util.HashMap;\n\npublic class Solution {\n    public static int[] twoSum(int[] nums, int target) {\n        HashMap<Integer, Integer> map = new HashMap<>();\n        for (int i = 0; i < nums.length; i++) {\n            int diff = target - nums[i];\n            if (map.containsKey(diff)) {\n                return new int[] { map.get(diff), i };\n            }\n            map.put(nums[i], i);\n        }\n        return new int[]{};\n    }\n    public static void main(String[] args) {\n        int[] res = twoSum(new int[]{2, 7, 11, 15}, 9);\n        System.out.println(\"[\" + res[0] + \", \" + res[1] + \"]\");\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nvector<int> twoSum(vector<int>& nums, int target) {\n    unordered_map<int, int> mp;\n    for (int i = 0; i < nums.size(); i++) {\n        int diff = target - nums[i];\n        if (mp.count(diff)) return {mp[diff], i};\n        mp[nums[i]] = i;\n    }\n    return {};\n}\n\nint main() {\n    vector<int> nums = {2, 7, 11, 15};\n    vector<int> res = twoSum(nums, 9);\n    cout << \"[\" << res[0] << \", \" << res[1] << \"]\" << endl;\n    return 0;\n}",
            "c": "#include <stdio.h>\n\nvoid twoSum(int nums[], int size, int target) {\n    for (int i = 0; i < size; i++) {\n        for (int j = i + 1; j < size; j++) {\n            if (nums[i] + nums[j] == target) {\n                printf(\"[%d, %d]\\n\", i, j);\n                return;\n            }\n        }\n    }\n}\n\nint main() {\n    int nums[] = {2, 7, 11, 15};\n    twoSum(nums, 4, 9);\n    return 0;\n}"
        },
        "sample_test_cases": [
            {"input": "[2, 7, 11, 15], 9", "expected_output": "[0, 1]"},
            {"input": "[3, 2, 4], 6", "expected_output": "[1, 2]"}
        ]
    },
    {
        "id": "sql-dept-highest-salary",
        "title": "Department Highest Salary",
        "subject": "SQL",
        "category": "DATABASE-DESIGN",
        "difficulty": "Medium",
        "description": "Write a SQL query to find employees who have the highest salary in each of the departments. Your query should return Department Name, Employee Name, and Salary.",
        "input_format": "Tables: Employee(id, name, salary, department_id), Department(id, name)",
        "output_format": "Department | Employee | Salary",
        "starter_code": {
            "sql": "-- Write your SQL query below\nSELECT d.name AS Department, e.name AS Employee, e.salary AS Salary\nFROM Employee e\nJOIN Department d ON e.department_id = d.id\nWHERE e.salary = (\n    SELECT MAX(salary) \n    FROM Employee \n    WHERE department_id = e.department_id\n);\n"
        },
        "sample_test_cases": [
            {"input": "Employee & Department Tables", "expected_output": "IT | Joe | 90000\nSales | Henry | 80000"}
        ]
    },
    {
        "id": "dsa-valid-parentheses",
        "title": "Valid Parentheses Evaluator",
        "subject": "DSA",
        "category": "SOFTWARE-DEVELOPMENT",
        "difficulty": "Easy",
        "description": "Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. Open brackets must be closed by the same type of brackets and in the correct order.",
        "input_format": "s = '()[]{}'",
        "output_format": "True",
        "starter_code": {
            "python": "def is_valid(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top_element = stack.pop() if stack else '#'\n            if mapping[char] != top_element:\n                return False\n        else:\n            stack.append(char)\n    return not stack\n\n# Test invocation\nprint(is_valid('()[]{}'))",
            "java": "import java.util.Stack;\n\npublic class Solution {\n    public static boolean isValid(String s) {\n        Stack<Character> stack = new Stack<>();\n        for (char c : s.toCharArray()) {\n            if (c == '(') stack.push(')');\n            else if (c == '{') stack.push('}');\n            else if (c == '[') stack.push(']');\n            else if (stack.isEmpty() || stack.pop() != c) return false;\n        }\n        return stack.isEmpty();\n    }\n    public static void main(String[] args) {\n        System.out.println(isValid(\"()[]{}\"));\n    }\n}",
            "cpp": "#include <iostream>\n#include <stack>\n#include <string>\nusing namespace std;\n\nbool isValid(string s) {\n    stack<char> st;\n    for (char c : s) {\n        if (c == '(') st.push(')');\n        else if (c == '{') st.push('}');\n        else if (c == '[') st.push(']');\n        else {\n            if (st.empty() || st.top() != c) return false;\n            st.pop();\n        }\n    }\n    return st.empty();\n}\n\nint main() {\n    cout << (isValid(\"()[]{}\") ? \"True\" : \"False\") << endl;\n    return 0;\n}"
        },
        "sample_test_cases": [
            {"input": "'()[]{}'", "expected_output": "True"},
            {"input": "'(]'", "expected_output": "False"}
        ]
    },
    {
        "id": "c-reverse-string-pointers",
        "title": "Reverse String Using Pointers",
        "subject": "C",
        "category": "SOFTWARE-DEVELOPMENT",
        "difficulty": "Medium",
        "description": "Write a C function that reverses a null-terminated string in-place using two pointers without using string library functions like `strrev`.",
        "input_format": "char str[] = 'PrepWise'",
        "output_format": "'esiWperP'",
        "starter_code": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nvoid reverseString(char* str) {\n    int left = 0;\n    int right = strlen(str) - 1;\n    while (left < right) {\n        char temp = str[left];\n        str[left] = str[right];\n        str[right] = temp;\n        left++;\n        right--;\n    }\n}\n\nint main() {\n    char str[] = \"PrepWise\";\n    reverseString(str);\n    printf(\"%s\\n\", str);\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nvoid reverseString(string& str) {\n    int left = 0, right = str.length() - 1;\n    while (left < right) {\n        swap(str[left++], str[right--]);\n    }\n}\n\nint main() {\n    string str = \"PrepWise\";\n    reverseString(str);\n    cout << str << endl;\n    return 0;\n}"
        },
        "sample_test_cases": [
            {"input": "'PrepWise'", "expected_output": "'esiWperP'"},
            {"input": "'Python'", "expected_output": "'nohtyP'"}
        ]
    }
]

def get_problems_by_subject(subject=None, difficulty=None):
    """Filters problem bank by subject language and difficulty level"""
    filtered = CODING_PROBLEMS
    if subject and subject.lower() != 'all':
        filtered = [p for p in filtered if p['subject'].lower() == subject.lower()]
    if difficulty and difficulty.lower() != 'all':
        filtered = [p for p in filtered if p['difficulty'].lower() == difficulty.lower()]
    return filtered
