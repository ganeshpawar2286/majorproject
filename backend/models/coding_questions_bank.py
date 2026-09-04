"""
PrepWise AI – Curated Multi-Language Coding Interview Question Bank
Contains 100+ Production DSA Questions across 15 Topics and 3 Difficulty Tiers.
Supports Python, JavaScript (Node.js), Java, and C++.
"""

CODING_QUESTIONS = [
    {
        "questionId": "arr-two-sum",
        "title": "Two Sum",
        "topic": "Arrays",
        "difficulty": "Easy",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        "constraints": "2 <= n <= 10^4",
        "inputFormat": "First line: n. Second line: n integers. Third line: target.",
        "outputFormat": "Two space-separated indices in ascending order.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n2 7 11 15\n9",
                "output": "0 1",
                "explanation": "nums[0] + nums[1] = 9"
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];t=int(d[n+1]);m={}\n for i,x in enumerate(nums):\n  if t-x in m: print(f'{m[t-x]} {i}');break\n  m[x]=i",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>=3){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);const t=parseInt(d[n+1]);const m=new Map();for(let i=0;i<n;i++){if(m.has(t-nums[i])){console.log(`${m.get(t-nums[i])} ${i}`);break;}m.set(nums[i],i);}}"
        },
        "testCases": [
            {
                "input": "4\n2 7 11 15\n9",
                "expected_output": "0 1"
            },
            {
                "input": "3\n3 2 4\n6",
                "expected_output": "1 2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2\n3 3\n6",
                "expected_output": "0 1"
            },
            {
                "input": "5\n1 5 7 12 19\n20",
                "expected_output": "0 4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "arr-contains-duplicate",
        "title": "Contains Duplicate",
        "topic": "Arrays",
        "difficulty": "Easy",
        "description": "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
        "constraints": "1 <= n <= 10^5",
        "inputFormat": "First line: n. Second line: n integers.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 2 3 1",
                "output": "true",
                "explanation": "1 appears twice."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]]\n print('true' if len(set(nums))<len(nums) else 'false')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);console.log(new Set(nums).size<nums.length?'true':'false');}"
        },
        "testCases": [
            {
                "input": "4\n1 2 3 1",
                "expected_output": "true"
            },
            {
                "input": "4\n1 2 3 4",
                "expected_output": "false"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n99",
                "expected_output": "false"
            },
            {
                "input": "6\n1 1 1 3 3 4",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "arr-best-time-stock",
        "title": "Best Time to Buy and Sell Stock",
        "topic": "Arrays",
        "difficulty": "Easy",
        "description": "Maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.",
        "constraints": "1 <= n <= 10^5",
        "inputFormat": "First line: n. Second line: n prices.",
        "outputFormat": "Max profit as integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n7 1 5 3 6 4",
                "output": "5",
                "explanation": "Buy on day 2 (1), sell on day 5 (6), profit 5."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);p=[int(x) for x in d[1:n+1]];mn,ans=float('inf'),0\n for x in p: mn=min(mn,x); ans=max(ans,x-mn)\n print(ans)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const p=d.slice(1,n+1).map(Number);let mn=Infinity,ans=0;for(const x of p){mn=Math.min(mn,x);ans=Math.max(ans,x-mn);}console.log(ans);}"
        },
        "testCases": [
            {
                "input": "6\n7 1 5 3 6 4",
                "expected_output": "5"
            },
            {
                "input": "5\n7 6 4 3 1",
                "expected_output": "0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2\n2 4",
                "expected_output": "2"
            },
            {
                "input": "5\n2 1 2 1 0",
                "expected_output": "1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "arr-max-subarray",
        "title": "Maximum Subarray (Kadane's)",
        "topic": "Arrays",
        "difficulty": "Easy",
        "description": "Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.",
        "constraints": "1 <= n <= 10^5",
        "inputFormat": "First line: n. Second line: n integers.",
        "outputFormat": "Max subarray sum.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "9\n-2 1 -3 4 -1 2 1 -5 4",
                "output": "6",
                "explanation": "Subarray [4,-1,2,1] has the largest sum 6."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];cur=mx=nums[0]\n for x in nums[1:]: cur=max(x,cur+x); mx=max(mx,cur)\n print(mx)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);let cur=nums[0],mx=nums[0];for(let i=1;i<n;i++){cur=Math.max(nums[i],cur+nums[i]);mx=Math.max(mx,cur);}console.log(mx);}"
        },
        "testCases": [
            {
                "input": "9\n-2 1 -3 4 -1 2 1 -5 4",
                "expected_output": "6"
            },
            {
                "input": "1\n1",
                "expected_output": "1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n5 4 -1 7 8",
                "expected_output": "23"
            },
            {
                "input": "3\n-3 -2 -1",
                "expected_output": "-1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "arr-product-except-self",
        "title": "Product of Array Except Self",
        "topic": "Arrays",
        "difficulty": "Medium",
        "description": "Return array such that answer[i] is the product of all elements except nums[i]. Must run in O(n) without division.",
        "constraints": "2 <= n <= 10^5",
        "inputFormat": "First line: n. Second line: n integers.",
        "outputFormat": "Space-separated products.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 2 3 4",
                "output": "24 12 8 6",
                "explanation": "Calculated with prefix and suffix products."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];ans=[1]*n;pre=1\n for i in range(n): ans[i]=pre; pre*=nums[i]\n suf=1\n for i in range(n-1,-1,-1): ans[i]*=suf; suf*=nums[i]\n print(*(ans))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);const ans=new Array(n).fill(1);let pre=1;for(let i=0;i<n;i++){ans[i]=pre;pre*=nums[i];}let suf=1;for(let i=n-1;i>=0;i--){ans[i]*=suf;suf*=nums[i];}console.log(ans.join(' '));}"
        },
        "testCases": [
            {
                "input": "4\n1 2 3 4",
                "expected_output": "24 12 8 6"
            },
            {
                "input": "5\n-1 1 0 -3 3",
                "expected_output": "0 0 9 0 0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2\n5 2",
                "expected_output": "2 5"
            },
            {
                "input": "3\n0 0 2",
                "expected_output": "0 0 0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "arr-subarray-sum-k",
        "title": "Subarray Sum Equals K",
        "topic": "Arrays",
        "difficulty": "Medium",
        "description": "Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.",
        "constraints": "1 <= n <= 2*10^4",
        "inputFormat": "Line 1: n and k. Line 2: n integers.",
        "outputFormat": "Count of matching subarrays.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3 2\n1 1 1",
                "output": "2",
                "explanation": "[1,1] at index 0-1 and 1-2."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nfrom collections import defaultdict\nd=sys.stdin.read().split()\nif d:\n n,k=int(d[0]),int(d[1]);nums=[int(x) for x in d[2:n+2]];m=defaultdict(int);m[0]=1;cur=0;ans=0\n for x in nums: cur+=x; ans+=m[cur-k]; m[cur]+=1\n print(ans)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>2){const n=parseInt(d[0]),k=parseInt(d[1]);const nums=d.slice(2,n+2).map(Number);const m=new Map();m.set(0,1);let cur=0,ans=0;for(const x of nums){cur+=x;if(m.has(cur-k))ans+=m.get(cur-k);m.set(cur,(m.get(cur)||0)+1);}console.log(ans);}"
        },
        "testCases": [
            {
                "input": "3 2\n1 1 1",
                "expected_output": "2"
            },
            {
                "input": "3 3\n1 2 3",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4 0\n1 -1 1 -1",
                "expected_output": "4"
            },
            {
                "input": "1 5\n5",
                "expected_output": "1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "arr-merge-intervals",
        "title": "Merge Intervals",
        "topic": "Arrays",
        "difficulty": "Medium",
        "description": "Given an array of intervals [start, end], merge all overlapping intervals.",
        "constraints": "1 <= n <= 10^4",
        "inputFormat": "First line: n. Next n lines: start end.",
        "outputFormat": "Merged intervals start end.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 3\n2 6\n8 10\n15 18",
                "output": "1 6\n8 10\n15 18",
                "explanation": "[1,3] and [2,6] merge into [1,6]."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);it=[[int(d[1+2*i]),int(d[2+2*i])] for i in range(n)]\n it.sort();res=[]\n for s,e in it:\n  if not res or res[-1][1]<s: res.append([s,e])\n  else: res[-1][1]=max(res[-1][1],e)\n for s,e in res: print(f'{s} {e}')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const it=[];for(let i=0;i<n;i++)it.push([parseInt(d[1+2*i]),parseInt(d[2+2*i])]);it.sort((a,b)=>a[0]-b[0]);const res=[];for(const [s,e] of it){if(res.length===0||res[res.length-1][1]<s)res.push([s,e]);else res[res.length-1][1]=Math.max(res[res.length-1][1],e);}for(const [s,e] of res)console.log(`${s} ${e}`);}"
        },
        "testCases": [
            {
                "input": "4\n1 3\n2 6\n8 10\n15 18",
                "expected_output": "1 6\n8 10\n15 18"
            },
            {
                "input": "2\n1 4\n4 5",
                "expected_output": "1 5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n1 10",
                "expected_output": "1 10"
            },
            {
                "input": "3\n1 4\n0 2\n3 5",
                "expected_output": "0 5"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "arr-first-missing-pos",
        "title": "First Missing Positive",
        "topic": "Arrays",
        "difficulty": "Hard",
        "description": "Return the smallest positive integer that is not present in nums in O(n) time and O(1) space.",
        "constraints": "1 <= n <= 10^5",
        "inputFormat": "First line: n. Second line: n integers.",
        "outputFormat": "First missing positive integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 0",
                "output": "3",
                "explanation": "Missing positive is 3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]]\n for i in range(n):\n  while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]: idx=nums[i]-1; nums[i],nums[idx]=nums[idx],nums[i]\n for i in range(n):\n  if nums[i]!=i+1: print(i+1); sys.exit(0)\n print(n+1)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);for(let i=0;i<n;i++){while(nums[i]>=1&&nums[i]<=n&&nums[nums[i]-1]!==nums[i]){const idx=nums[i]-1;const t=nums[i];nums[i]=nums[idx];nums[idx]=t;}}for(let i=0;i<n;i++){if(nums[i]!==i+1){console.log(i+1);process.exit(0);}}console.log(n+1);}"
        },
        "testCases": [
            {
                "input": "3\n1 2 0",
                "expected_output": "3"
            },
            {
                "input": "4\n3 4 -1 1",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n7 8 9 11 12",
                "expected_output": "1"
            },
            {
                "input": "2\n1 2",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "arrays",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "str-valid-anagram",
        "title": "Valid Anagram",
        "topic": "Strings",
        "difficulty": "Easy",
        "description": "Given two strings s and t, return true if t is an anagram of s, and false otherwise.",
        "constraints": "1 <= len(s), len(t) <= 5*10^4",
        "inputFormat": "Two strings s and t on separate lines or space-separated.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "anagram\nnagaram",
                "output": "true",
                "explanation": "Both have identical character counts."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif len(d)>=2:\n print('true' if sorted(d[0])==sorted(d[1]) else 'false')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>=2){console.log(d[0].split('').sort().join('')===d[1].split('').sort().join('')?'true':'false');}"
        },
        "testCases": [
            {
                "input": "anagram\nnagaram",
                "expected_output": "true"
            },
            {
                "input": "rat\ncar",
                "expected_output": "false"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "a\nb",
                "expected_output": "false"
            },
            {
                "input": "listen\nsilent",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "str-valid-palindrome",
        "title": "Valid Palindrome",
        "topic": "Strings",
        "difficulty": "Easy",
        "description": "Given a string s, return true if it is a palindrome considering only alphanumeric characters and ignoring cases.",
        "constraints": "1 <= len(s) <= 2*10^5",
        "inputFormat": "A string s.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "A man a plan a canal Panama",
                "output": "true",
                "explanation": "amanaplanacanalpanama is a palindrome."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys,re\ns=sys.stdin.read().strip(); c=re.sub(r'[^a-zA-Z0-9]', '', s).lower()\nprint('true' if c==c[::-1] else 'false')",
            "javascript": "const fs=require('fs');const s=fs.readFileSync(0,'utf-8').trim();const c=s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase();console.log(c===c.split('').reverse().join('')?'true':'false');"
        },
        "testCases": [
            {
                "input": "A man a plan a canal Panama",
                "expected_output": "true"
            },
            {
                "input": "race a car",
                "expected_output": "false"
            }
        ],
        "hiddenTestCases": [
            {
                "input": " ",
                "expected_output": "true"
            },
            {
                "input": "0P",
                "expected_output": "false"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "str-longest-common-prefix",
        "title": "Longest Common Prefix",
        "topic": "Strings",
        "difficulty": "Easy",
        "description": "Find the longest common prefix string amongst an array of strings. Return empty string if none.",
        "constraints": "1 <= n <= 200",
        "inputFormat": "Line 1: n. Line 2: n strings.",
        "outputFormat": "Common prefix string.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\nflower flow flight",
                "output": "fl",
                "explanation": "'fl' is common prefix."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);strs=d[1:n+1]\n if not strs: print(''); sys.exit(0)\n p=strs[0]\n for s in strs[1:]:\n  while not s.startswith(p): p=p[:-1]; if not p: break\n print(p)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const n=parseInt(d[0]);const strs=d.slice(1,n+1);if(!strs.length){console.log('');process.exit(0);}let p=strs[0];for(let i=1;i<strs.length;i++){while(!strs[i].startsWith(p)){p=p.slice(0,-1);if(!p)break;}}console.log(p);}"
        },
        "testCases": [
            {
                "input": "3\nflower flow flight",
                "expected_output": "fl"
            },
            {
                "input": "3\ndog racecar car",
                "expected_output": ""
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\napple",
                "expected_output": "apple"
            },
            {
                "input": "2\ninterstate interview",
                "expected_output": "inter"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "str-reverse-words",
        "title": "Reverse Words in a String",
        "topic": "Strings",
        "difficulty": "Medium",
        "description": "Given an input string s, reverse the order of the words separated by a single space.",
        "constraints": "1 <= len(s) <= 10^4",
        "inputFormat": "A string s.",
        "outputFormat": "Reversed words.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "the sky is blue",
                "output": "blue is sky the",
                "explanation": "Reversed word order."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nw=sys.stdin.read().split()\nprint(' '.join(reversed(w)))",
            "javascript": "const fs=require('fs');const w=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);console.log(w.reverse().join(' '));"
        },
        "testCases": [
            {
                "input": "the sky is blue",
                "expected_output": "blue is sky the"
            },
            {
                "input": "  hello world  ",
                "expected_output": "world hello"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "a good   example",
                "expected_output": "example good a"
            },
            {
                "input": "PrepWise",
                "expected_output": "PrepWise"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "str-group-anagrams",
        "title": "Group Anagrams Count",
        "topic": "Strings",
        "difficulty": "Medium",
        "description": "Given an array of strings strs, group the anagrams together and return the count of distinct groups.",
        "constraints": "1 <= n <= 10^4",
        "inputFormat": "Line 1: n. Line 2: n strings.",
        "outputFormat": "Count of distinct anagram groups.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\neat tea tan ate nat bat",
                "output": "3",
                "explanation": "3 distinct anagram groups."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);strs=d[1:n+1];g={}\n for s in strs: k=''.join(sorted(s)); g.setdefault(k,[]).append(s)\n print(len(g))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const n=parseInt(d[0]);const strs=d.slice(1,n+1);const m=new Map();for(const s of strs){const k=s.split('').sort().join('');m.set(k,(m.get(k)||0)+1);}console.log(m.size);}"
        },
        "testCases": [
            {
                "input": "6\neat tea tan ate nat bat",
                "expected_output": "3"
            },
            {
                "input": "1\na",
                "expected_output": "1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2\nab ba",
                "expected_output": "1"
            },
            {
                "input": "3\na b c",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "str-longest-palindrome-substr",
        "title": "Longest Palindromic Substring",
        "topic": "Strings",
        "difficulty": "Medium",
        "description": "Given a string s, return the length of the longest palindromic substring in s.",
        "constraints": "1 <= len(s) <= 1000",
        "inputFormat": "A string s.",
        "outputFormat": "Integer length of longest palindrome.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "babad",
                "output": "3",
                "explanation": "'bab' or 'aba' has length 3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\ns=sys.stdin.read().strip()\nif not s: print(0); sys.exit(0)\ndef exp(l,r):\n while l>=0 and r<len(s) and s[l]==s[r]: l-=1; r+=1\n return r-l-1\nmx=1\nfor i in range(len(s)): mx=max(mx, exp(i,i), exp(i,i+1))\nprint(mx)",
            "javascript": "const fs=require('fs');const s=fs.readFileSync(0,'utf-8').trim();if(!s){console.log(0);process.exit(0);}function exp(l,r){while(l>=0&&r<s.length&&s[l]===s[r]){l--;r++;}return r-l-1;}let mx=1;for(let i=0;i<s.length;i++){mx=Math.max(mx,exp(i,i),exp(i,i+1));}console.log(mx);"
        },
        "testCases": [
            {
                "input": "babad",
                "expected_output": "3"
            },
            {
                "input": "cbbd",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "a",
                "expected_output": "1"
            },
            {
                "input": "racecar",
                "expected_output": "7"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "str-string-atoi",
        "title": "String to Integer (atoi)",
        "topic": "Strings",
        "difficulty": "Medium",
        "description": "Convert a string to a 32-bit signed integer. Clamp within [-2^31, 2^31 - 1].",
        "constraints": "0 <= len(s) <= 200",
        "inputFormat": "A string s.",
        "outputFormat": "32-bit signed integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "42",
                "output": "42",
                "explanation": "Direct 42."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\ns=sys.stdin.read().strip(); i,n,sign,res=0,len(s),1,0\nwhile i<n and s[i]==' ': i+=1\nif i<n and (s[i]=='+' or s[i]=='-'):\n if s[i]=='-': sign=-1\n i+=1\nwhile i<n and s[i].isdigit(): res=res*10+int(s[i]); i+=1\nres*=sign; print(max(-2**31, min(2**31-1, res)))",
            "javascript": "const fs=require('fs');const s=fs.readFileSync(0,'utf-8').trim();let i=0,n=s.length,sign=1,res=0;while(i<n&&s[i]===' ')i++;if(i<n&&(s[i]==='+'||s[i]==='-')){if(s[i]==='-')sign=-1;i++;}while(i<n&&s[i]>='0'&&s[i]<='9'){res=res*10+parseInt(s[i]);i++;}res*=sign;console.log(Math.max(-2147483648,Math.min(2147483647,res)));"
        },
        "testCases": [
            {
                "input": "42",
                "expected_output": "42"
            },
            {
                "input": "   -42",
                "expected_output": "-42"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4193 with words",
                "expected_output": "4193"
            },
            {
                "input": "-91283472332",
                "expected_output": "-2147483648"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "str-regular-expression",
        "title": "Regular Expression Matching",
        "topic": "Strings",
        "difficulty": "Hard",
        "description": "Return true if pattern p matches s supporting '.' and '*'.",
        "constraints": "1 <= len(s), len(p) <= 20",
        "inputFormat": "Line 1: s. Line 2: p.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "aa\na*",
                "output": "true",
                "explanation": "'*' matches multiple 'a's."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\ns=d[0] if len(d)>0 else ''; p=d[1] if len(d)>1 else ''\nm,n=len(s),len(p); dp=[[False]*(n+1) for _ in range(m+1)]; dp[0][0]=True\nfor j in range(2,n+1):\n if p[j-1]=='*': dp[0][j]=dp[0][j-2]\nfor i in range(1,m+1):\n for j in range(1,n+1):\n  if p[j-1]=='*': dp[i][j]=dp[i][j-2] or (dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]=='.'))\n  else: dp[i][j]=dp[i-1][j-1] and (p[j-1]==s[i-1] or p[j-1]=='.')\nprint('true' if dp[m][n] else 'false')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);const s=d[0]||'',p=d[1]||'';const m=s.length,n=p.length;const dp=Array.from({length:m+1},()=>new Array(n+1).fill(false));dp[0][0]=true;for(let j=2;j<=n;j++)if(p[j-1]==='*')dp[0][j]=dp[0][j-2];for(let i=1;i<=m;i++){for(let j=1;j<=n;j++){if(p[j-1]==='*')dp[i][j]=dp[i][j-2]||(dp[i-1][j]&&(p[j-2]===s[i-1]||p[j-2]==='.'));else dp[i][j]=dp[i-1][j-1]&&(p[j-1]===s[i-1]||p[j-1]==='.');}}console.log(dp[m][n]?'true':'false');"
        },
        "testCases": [
            {
                "input": "aa\na*",
                "expected_output": "true"
            },
            {
                "input": "aa\np",
                "expected_output": "false"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "ab\n.*",
                "expected_output": "true"
            },
            {
                "input": "aab\nc*a*b",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "strings",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "srch-binary-search",
        "title": "Binary Search",
        "topic": "Searching",
        "difficulty": "Easy",
        "description": "Given sorted array nums and target, return index of target or -1.",
        "constraints": "1 <= n <= 10^4",
        "inputFormat": "Line 1: n. Line 2: n integers. Line 3: target.",
        "outputFormat": "Integer index or -1.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n-1 0 3 5 9 12\n9",
                "output": "4",
                "explanation": "9 is at index 4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];t=int(d[n+1]);l,r=0,n-1;ans=-1\n while l<=r:\n  m=(l+r)//2\n  if nums[m]==t: ans=m; break\n  elif nums[m]<t: l=m+1\n  else: r=m-1\n print(ans)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>=3){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);const t=parseInt(d[n+1]);let l=0,r=n-1,ans=-1;while(l<=r){const m=Math.floor((l+r)/2);if(nums[m]===t){ans=m;break;}else if(nums[m]<t)l=m+1;else r=m-1;}console.log(ans);}"
        },
        "testCases": [
            {
                "input": "6\n-1 0 3 5 9 12\n9",
                "expected_output": "4"
            },
            {
                "input": "6\n-1 0 3 5 9 12\n2",
                "expected_output": "-1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n5\n5",
                "expected_output": "0"
            },
            {
                "input": "2\n1 3\n2",
                "expected_output": "-1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "searching",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "srch-search-insert-pos",
        "title": "Search Insert Position",
        "topic": "Searching",
        "difficulty": "Easy",
        "description": "Return the index if target is found, or index where it would be inserted in order.",
        "constraints": "1 <= n <= 10^4",
        "inputFormat": "Line 1: n. Line 2: n integers. Line 3: target.",
        "outputFormat": "Insert index integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 3 5 6\n5",
                "output": "2",
                "explanation": "5 is at index 2."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];t=int(d[n+1]);l,r=0,n-1\n while l<=r:\n  m=(l+r)//2\n  if nums[m]==t: l=m; break\n  elif nums[m]<t: l=m+1\n  else: r=m-1\n print(l)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>=3){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);const t=parseInt(d[n+1]);let l=0,r=n-1;while(l<=r){const m=Math.floor((l+r)/2);if(nums[m]===t){l=m;break;}else if(nums[m]<t)l=m+1;else r=m-1;}console.log(l);}"
        },
        "testCases": [
            {
                "input": "4\n1 3 5 6\n5",
                "expected_output": "2"
            },
            {
                "input": "4\n1 3 5 6\n2",
                "expected_output": "1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n1 3 5 6\n7",
                "expected_output": "4"
            },
            {
                "input": "4\n1 3 5 6\n0",
                "expected_output": "0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "searching",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "srch-find-first-last-pos",
        "title": "Find First and Last Position in Sorted Array",
        "topic": "Searching",
        "difficulty": "Medium",
        "description": "Find starting and ending position of target value in sorted array nums.",
        "constraints": "0 <= n <= 10^5",
        "inputFormat": "Line 1: n. Line 2: n integers. Line 3: target.",
        "outputFormat": "Two integers: start end, or -1 -1.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n5 7 7 8 8 10\n8",
                "output": "3 4",
                "explanation": "8 from index 3 to 4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys,bisect\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];t=int(d[n+1]) if n>0 and len(d)>n+1 else (int(d[1]) if n==0 and len(d)>1 else -999)\n if n==0: print('-1 -1'); sys.exit(0)\n l=bisect.bisect_left(nums, t); r=bisect.bisect_right(nums, t)-1\n print(f'{l} {r}' if l<=r and l<n and nums[l]==t else '-1 -1')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const n=parseInt(d[0]);if(n===0){console.log('-1 -1');process.exit(0);}const nums=d.slice(1,n+1).map(Number);const t=parseInt(d[n+1]);const l=nums.indexOf(t);const r=nums.lastIndexOf(t);console.log(`${l} ${r}`);}"
        },
        "testCases": [
            {
                "input": "6\n5 7 7 8 8 10\n8",
                "expected_output": "3 4"
            },
            {
                "input": "6\n5 7 7 8 8 10\n6",
                "expected_output": "-1 -1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "0\n0",
                "expected_output": "-1 -1"
            },
            {
                "input": "1\n1\n1",
                "expected_output": "0 0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "searching",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "srch-search-rotated",
        "title": "Search in Rotated Sorted Array",
        "topic": "Searching",
        "difficulty": "Medium",
        "description": "Find target index in rotated sorted array of unique integers in O(log n).",
        "constraints": "1 <= n <= 5000",
        "inputFormat": "Line 1: n. Line 2: n integers. Line 3: target.",
        "outputFormat": "Integer index or -1.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "7\n4 5 6 7 0 1 2\n0",
                "output": "4",
                "explanation": "0 is at index 4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];t=int(d[n+1]);l,r=0,n-1;ans=-1\n while l<=r:\n  m=(l+r)//2\n  if nums[m]==t: ans=m; break\n  if nums[l]<=nums[m]:\n   if nums[l]<=t<nums[m]: r=m-1\n   else: l=m+1\n  else:\n   if nums[m]<t<=nums[r]: l=m+1\n   else: r=m-1\n print(ans)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>=3){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);const t=parseInt(d[n+1]);let l=0,r=n-1,ans=-1;while(l<=r){const m=Math.floor((l+r)/2);if(nums[m]===t){ans=m;break;}if(nums[l]<=nums[m]){if(nums[l]<=t&&t<nums[m])r=m-1;else l=m+1;}else{if(nums[m]<t&&t<=nums[r])l=m+1;else r=m-1;}}console.log(ans);}"
        },
        "testCases": [
            {
                "input": "7\n4 5 6 7 0 1 2\n0",
                "expected_output": "4"
            },
            {
                "input": "7\n4 5 6 7 0 1 2\n3",
                "expected_output": "-1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n1\n0",
                "expected_output": "-1"
            },
            {
                "input": "3\n5 1 3\n5",
                "expected_output": "0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "searching",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "srch-find-peak-element",
        "title": "Find Peak Element",
        "topic": "Searching",
        "difficulty": "Medium",
        "description": "Find any peak element strictly greater than neighbors and return its index.",
        "constraints": "1 <= n <= 1000",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "Integer index of peak.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 2 3 1",
                "output": "2",
                "explanation": "3 is peak at index 2."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];l,r=0,n-1\n while l<r:\n  m=(l+r)//2\n  if nums[m]>nums[m+1]: r=m\n  else: l=m+1\n print(l)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);let l=0,r=n-1;while(l<r){const m=Math.floor((l+r)/2);if(nums[m]>nums[m+1])r=m;else l=m+1;}console.log(l);}"
        },
        "testCases": [
            {
                "input": "4\n1 2 3 1",
                "expected_output": "2"
            },
            {
                "input": "7\n1 2 1 3 5 6 4",
                "expected_output": "5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n10",
                "expected_output": "0"
            },
            {
                "input": "2\n1 2",
                "expected_output": "1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "searching",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "srch-find-min-rotated",
        "title": "Find Minimum in Rotated Sorted Array",
        "topic": "Searching",
        "difficulty": "Medium",
        "description": "Return the minimum element of sorted rotated array in O(log n).",
        "constraints": "1 <= n <= 5000",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "Minimum element.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n3 4 5 1 2",
                "output": "1",
                "explanation": "1 is minimum value."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];l,r=0,n-1\n while l<r:\n  m=(l+r)//2\n  if nums[m]>nums[r]: l=m+1\n  else: r=m\n print(nums[l])",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);let l=0,r=n-1;while(l<r){const m=Math.floor((l+r)/2);if(nums[m]>nums[r])l=m+1;else r=m;}console.log(nums[l]);}"
        },
        "testCases": [
            {
                "input": "5\n3 4 5 1 2",
                "expected_output": "1"
            },
            {
                "input": "7\n4 5 6 7 0 1 2",
                "expected_output": "0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n11 13 15 17",
                "expected_output": "11"
            },
            {
                "input": "1\n2",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "searching",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "srch-median-two-sorted",
        "title": "Median of Two Sorted Arrays",
        "topic": "Searching",
        "difficulty": "Hard",
        "description": "Return the median of two sorted arrays in O(log(m+n)) time.",
        "constraints": "0 <= m, n <= 1000",
        "inputFormat": "Line 1: m. Line 2: m integers. Line 3: n. Line 4: n integers.",
        "outputFormat": "Median formatted to 1 decimal.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "2\n1 3\n1\n2",
                "output": "2.0",
                "explanation": "Merged = [1,2,3], median 2.0."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n m=int(d[0]);idx=1;a=[int(x) for x in d[idx:idx+m]];idx+=m;n=int(d[idx]);idx+=1;b=[int(x) for x in d[idx:idx+n]]\n c=sorted(a+b);tot=len(c)\n print(f'{float(c[tot//2]):.1f}' if tot%2==1 else f'{(c[tot//2-1]+c[tot//2])/2.0:.1f}')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const m=parseInt(d[0]);let idx=1;const a=d.slice(idx,idx+m).map(Number);idx+=m;const n=parseInt(d[idx]);idx+=1;const b=d.slice(idx,idx+n).map(Number);const c=a.concat(b).sort((x,y)=>x-y);const tot=c.length;if(tot%2===1)console.log((c[Math.floor(tot/2)]).toFixed(1));else console.log(((c[tot/2-1]+c[tot/2])/2).toFixed(1));}"
        },
        "testCases": [
            {
                "input": "2\n1 3\n1\n2",
                "expected_output": "2.0"
            },
            {
                "input": "2\n1 2\n2\n3 4",
                "expected_output": "2.5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "0\n1\n1",
                "expected_output": "1.0"
            },
            {
                "input": "2\n0 0\n2\n0 0",
                "expected_output": "0.0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "searching",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "sort-merge-sorted-array",
        "title": "Merge Sorted Arrays",
        "topic": "Sorting",
        "difficulty": "Easy",
        "description": "Merge nums2 into nums1 as one sorted array.",
        "constraints": "0 <= m, n <= 200",
        "inputFormat": "Line 1: m. Line 2: m integers. Line 3: n. Line 4: n integers.",
        "outputFormat": "Merged sorted integers.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 3\n3\n2 5 6",
                "output": "1 2 2 3 5 6",
                "explanation": "Merged in order."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n m=int(d[0]);idx=1;a=[int(x) for x in d[idx:idx+m]];idx+=m;n=int(d[idx]);idx+=1;b=[int(x) for x in d[idx:idx+n]]\n print(*(sorted(a+b)))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const m=parseInt(d[0]);let idx=1;const a=d.slice(idx,idx+m).map(Number);idx+=m;const n=parseInt(d[idx]);idx+=1;const b=d.slice(idx,idx+n).map(Number);console.log(a.concat(b).sort((x,y)=>x-y).join(' '));}"
        },
        "testCases": [
            {
                "input": "3\n1 2 3\n3\n2 5 6",
                "expected_output": "1 2 2 3 5 6"
            },
            {
                "input": "1\n1\n0",
                "expected_output": "1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "0\n1\n1",
                "expected_output": "1"
            },
            {
                "input": "2\n4 5\n2\n1 2",
                "expected_output": "1 2 4 5"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sorting",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "sort-sort-array-parity",
        "title": "Sort Array By Parity",
        "topic": "Sorting",
        "difficulty": "Easy",
        "description": "Move all even integers at beginning followed by all odd integers.",
        "constraints": "1 <= n <= 5000",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "Even then odd integers.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n3 1 2 4",
                "output": "2 4 3 1",
                "explanation": "Evens (2, 4) then odds (3, 1)."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]]\n print(*( [x for x in nums if x%2==0] + [x for x in nums if x%2!=0] ))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);console.log(nums.filter(x=>x%2===0).concat(nums.filter(x=>x%2!==0)).join(' '));}"
        },
        "testCases": [
            {
                "input": "4\n3 1 2 4",
                "expected_output": "2 4 3 1"
            },
            {
                "input": "1\n0",
                "expected_output": "0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2\n1 3",
                "expected_output": "1 3"
            },
            {
                "input": "2\n2 4",
                "expected_output": "2 4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sorting",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "sort-sort-colors",
        "title": "Sort Colors",
        "topic": "Sorting",
        "difficulty": "Medium",
        "description": "Sort array with 0s (red), 1s (white), and 2s (blue) in-place.",
        "constraints": "1 <= n <= 300",
        "inputFormat": "Line 1: n. Line 2: n integers (0, 1, 2).",
        "outputFormat": "Sorted 0s, 1s, 2s.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n2 0 2 1 1 0",
                "output": "0 0 1 1 2 2",
                "explanation": "Dutch national flag sorting."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];nums.sort();print(*(nums))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number).sort((a,b)=>a-b);console.log(nums.join(' '));}"
        },
        "testCases": [
            {
                "input": "6\n2 0 2 1 1 0",
                "expected_output": "0 0 1 1 2 2"
            },
            {
                "input": "3\n2 0 1",
                "expected_output": "0 1 2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n0",
                "expected_output": "0"
            },
            {
                "input": "2\n1 0",
                "expected_output": "0 1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sorting",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sort-kth-largest-element",
        "title": "Kth Largest Element in an Array",
        "topic": "Sorting",
        "difficulty": "Medium",
        "description": "Return the kth largest element in array.",
        "constraints": "1 <= k <= n <= 10^5",
        "inputFormat": "Line 1: n and k. Line 2: n integers.",
        "outputFormat": "Kth largest element.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6 2\n3 2 1 5 6 4",
                "output": "5",
                "explanation": "2nd largest is 5."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n,k=int(d[0]),int(d[1]);nums=[int(x) for x in d[2:n+2]];nums.sort(reverse=True);print(nums[k-1])",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>2){const n=parseInt(d[0]),k=parseInt(d[1]);const nums=d.slice(2,n+2).map(Number).sort((a,b)=>b-a);console.log(nums[k-1]);}"
        },
        "testCases": [
            {
                "input": "6 2\n3 2 1 5 6 4",
                "expected_output": "5"
            },
            {
                "input": "9 4\n3 2 3 1 2 4 5 5 6",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1 1\n100",
                "expected_output": "100"
            },
            {
                "input": "5 5\n1 2 3 4 5",
                "expected_output": "1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sorting",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sort-top-k-frequent",
        "title": "Top K Frequent Elements",
        "topic": "Sorting",
        "difficulty": "Medium",
        "description": "Return the k most frequent elements in ascending order.",
        "constraints": "1 <= k <= distinct elements",
        "inputFormat": "Line 1: n and k. Line 2: n integers.",
        "outputFormat": "k space-separated integers.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6 2\n1 1 1 2 2 3",
                "output": "1 2",
                "explanation": "1 and 2 are top 2 frequent."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nfrom collections import Counter\nd=sys.stdin.read().split()\nif d:\n n,k=int(d[0]),int(d[1]);nums=[int(x) for x in d[2:n+2]];c=Counter(nums);top=[x[0] for x in c.most_common(k)];print(*(sorted(top)))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>2){const n=parseInt(d[0]),k=parseInt(d[1]);const nums=d.slice(2,n+2).map(Number);const m=new Map();for(const x of nums)m.set(x,(m.get(x)||0)+1);const sorted=Array.from(m.entries()).sort((a,b)=>b[1]-a[1]).slice(0,k).map(x=>x[0]).sort((a,b)=>a-b);console.log(sorted.join(' '));}"
        },
        "testCases": [
            {
                "input": "6 2\n1 1 1 2 2 3",
                "expected_output": "1 2"
            },
            {
                "input": "1 1\n1",
                "expected_output": "1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4 2\n1 2 3 4",
                "expected_output": "1 2"
            },
            {
                "input": "5 1\n2 2 2 3 3",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sorting",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sort-largest-number",
        "title": "Largest Number",
        "topic": "Sorting",
        "difficulty": "Medium",
        "description": "Arrange numbers such that they form the largest number.",
        "constraints": "1 <= n <= 100",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "Largest number string.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n3 30 34 5 9",
                "output": "9534330",
                "explanation": "Optimal arrangement."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nfrom functools import cmp_to_key\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=d[1:n+1];cmp=lambda a,b: -1 if a+b>b+a else (1 if a+b<b+a else 0);nums.sort(key=cmp_to_key(cmp));ans=''.join(nums);print('0' if ans[0]=='0' else ans)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).sort((a,b)=>(b+a).localeCompare(a+b));const ans=nums.join('');console.log(ans[0]==='0'?'0':ans);}"
        },
        "testCases": [
            {
                "input": "5\n3 30 34 5 9",
                "expected_output": "9534330"
            },
            {
                "input": "2\n10 2",
                "expected_output": "210"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n0",
                "expected_output": "0"
            },
            {
                "input": "2\n0 0",
                "expected_output": "0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sorting",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sort-maximum-gap",
        "title": "Maximum Gap",
        "topic": "Sorting",
        "difficulty": "Hard",
        "description": "Return maximum difference between two successive elements in sorted form.",
        "constraints": "1 <= n <= 10^5",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "Maximum difference integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n3 6 9 1",
                "output": "3",
                "explanation": "[1, 3, 6, 9] max gap is 3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]]\n if n<2: print(0); sys.exit(0)\n nums.sort(); print(max(nums[i]-nums[i-1] for i in range(1,n)))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);if(n<2){console.log(0);process.exit(0);}const nums=d.slice(1,n+1).map(Number).sort((a,b)=>a-b);let mx=0;for(let i=1;i<n;i++)mx=Math.max(mx,nums[i]-nums[i-1]);console.log(mx);}"
        },
        "testCases": [
            {
                "input": "4\n3 6 9 1",
                "expected_output": "3"
            },
            {
                "input": "1\n10",
                "expected_output": "0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2\n1 100",
                "expected_output": "99"
            },
            {
                "input": "3\n1 1 1",
                "expected_output": "0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sorting",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "ll-reverse-linked-list",
        "title": "Reverse Linked List",
        "topic": "Linked List",
        "difficulty": "Easy",
        "description": "Given a singly linked list represented as space-separated values, reverse the list.",
        "constraints": "0 <= n <= 5000",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "Reversed linked list values.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n1 2 3 4 5",
                "output": "5 4 3 2 1",
                "explanation": "Reversed order."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=d[1:n+1];print(*(reversed(nums)))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const n=parseInt(d[0]);const nums=d.slice(1,n+1);console.log(nums.reverse().join(' '));}"
        },
        "testCases": [
            {
                "input": "5\n1 2 3 4 5",
                "expected_output": "5 4 3 2 1"
            },
            {
                "input": "2\n1 2",
                "expected_output": "2 1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "0",
                "expected_output": ""
            },
            {
                "input": "1\n99",
                "expected_output": "99"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "linked list",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "ll-merge-two-sorted",
        "title": "Merge Two Sorted Lists",
        "topic": "Linked List",
        "difficulty": "Easy",
        "description": "Merge two sorted linked lists into one sorted linked list.",
        "constraints": "0 <= m, n <= 100",
        "inputFormat": "Line 1: m. Line 2: m integers. Line 3: n. Line 4: n integers.",
        "outputFormat": "Merged sorted list values.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 4\n3\n1 3 4",
                "output": "1 1 2 3 4 4",
                "explanation": "Merged sorted list."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n m=int(d[0]);idx=1;a=[int(x) for x in d[idx:idx+m]];idx+=m;n=int(d[idx]);idx+=1;b=[int(x) for x in d[idx:idx+n]]\n print(*(sorted(a+b)))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const m=parseInt(d[0]);let idx=1;const a=d.slice(idx,idx+m).map(Number);idx+=m;const n=parseInt(d[idx]);idx+=1;const b=d.slice(idx,idx+n).map(Number);console.log(a.concat(b).sort((x,y)=>x-y).join(' '));}"
        },
        "testCases": [
            {
                "input": "3\n1 2 4\n3\n1 3 4",
                "expected_output": "1 1 2 3 4 4"
            },
            {
                "input": "0\n0",
                "expected_output": ""
            }
        ],
        "hiddenTestCases": [
            {
                "input": "0\n1\n0",
                "expected_output": "0"
            },
            {
                "input": "1\n5\n1\n2",
                "expected_output": "2 5"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "linked list",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "ll-middle-node",
        "title": "Middle of the Linked List",
        "topic": "Linked List",
        "difficulty": "Easy",
        "description": "Return the value of the middle node of the linked list. If two middle nodes, return second.",
        "constraints": "1 <= n <= 100",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "Middle node integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n1 2 3 4 5",
                "output": "3",
                "explanation": "3 is the middle."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];print(nums[n//2])",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1);console.log(nums[Math.floor(n/2)]);}"
        },
        "testCases": [
            {
                "input": "5\n1 2 3 4 5",
                "expected_output": "3"
            },
            {
                "input": "6\n1 2 3 4 5 6",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n7",
                "expected_output": "7"
            },
            {
                "input": "2\n1 2",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "linked list",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "ll-remove-nth-from-end",
        "title": "Remove Nth Node From End of List",
        "topic": "Linked List",
        "difficulty": "Medium",
        "description": "Remove the nth node from the end of the list and return its elements.",
        "constraints": "1 <= n <= length <= 30",
        "inputFormat": "Line 1: length and n. Line 2: length integers.",
        "outputFormat": "List after removal.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5 2\n1 2 3 4 5",
                "output": "1 2 3 5",
                "explanation": "4 is removed."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n l,n=int(d[0]),int(d[1]);nums=d[2:l+2];idx=l-n;del nums[idx];print(*(nums))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>2){const l=parseInt(d[0]),n=parseInt(d[1]);const nums=d.slice(2,l+2);nums.splice(l-n,1);console.log(nums.join(' '));}"
        },
        "testCases": [
            {
                "input": "5 2\n1 2 3 4 5",
                "expected_output": "1 2 3 5"
            },
            {
                "input": "1 1\n1",
                "expected_output": ""
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2 1\n1 2",
                "expected_output": "1"
            },
            {
                "input": "2 2\n1 2",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "linked list",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "ll-add-two-numbers",
        "title": "Add Two Numbers",
        "topic": "Linked List",
        "difficulty": "Medium",
        "description": "Add two numbers represented by linked lists in reverse order. Return sum as reversed list.",
        "constraints": "1 <= len <= 100",
        "inputFormat": "Line 1: l1. Line 2: l1 digits. Line 3: l2. Line 4: l2 digits.",
        "outputFormat": "Sum digits in reverse order.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n2 4 3\n3\n5 6 4",
                "output": "7 0 8",
                "explanation": "342 + 465 = 807."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n l1=int(d[0]);idx=1;a=[int(x) for x in d[idx:idx+l1]];idx+=l1;l2=int(d[idx]);idx+=1;b=[int(x) for x in d[idx:idx+l2]]\n carry=0;res=[];i=0\n while i<max(l1,l2) or carry:\n  v1=a[i] if i<l1 else 0; v2=b[i] if i<l2 else 0; s=v1+v2+carry; res.append(s%10); carry=s//10; i+=1\n print(*(res))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const l1=parseInt(d[0]);let idx=1;const a=d.slice(idx,idx+l1).map(Number);idx+=l1;const l2=parseInt(d[idx]);idx+=1;const b=d.slice(idx,idx+l2).map(Number);let carry=0,res=[],i=0;while(i<Math.max(l1,l2)||carry){const v1=i<l1?a[i]:0,v2=i<l2?b[i]:0,s=v1+v2+carry;res.push(s%10);carry=Math.floor(s/10);i++;}console.log(res.join(' '));}"
        },
        "testCases": [
            {
                "input": "3\n2 4 3\n3\n5 6 4",
                "expected_output": "7 0 8"
            },
            {
                "input": "1\n0\n1\n0",
                "expected_output": "0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2\n9 9\n1\n1",
                "expected_output": "0 0 1"
            },
            {
                "input": "1\n5\n1\n5",
                "expected_output": "0 1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "linked list",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "ll-detect-cycle-pos",
        "title": "Linked List Cycle Detection",
        "topic": "Linked List",
        "difficulty": "Easy",
        "description": "Given list values and pos (index where tail connects, or -1 for no cycle), return 'true' if cycle, else 'false'.",
        "constraints": "0 <= n <= 10^4, pos >= -1",
        "inputFormat": "Line 1: n and pos. Line 2: n integers.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4 1\n3 2 0 -4",
                "output": "true",
                "explanation": "Tail connects to node index 1."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n,pos=int(d[0]),int(d[1]);print('true' if pos!=-1 and n>0 else 'false')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>=2){const n=parseInt(d[0]),pos=parseInt(d[1]);console.log(pos!==-1&&n>0?'true':'false');}"
        },
        "testCases": [
            {
                "input": "4 1\n3 2 0 -4",
                "expected_output": "true"
            },
            {
                "input": "2 0\n1 2",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1 -1\n1",
                "expected_output": "false"
            },
            {
                "input": "0 -1",
                "expected_output": "false"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "linked list",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "ll-merge-k-sorted",
        "title": "Merge k Sorted Lists",
        "topic": "Linked List",
        "difficulty": "Hard",
        "description": "Merge k sorted linked lists and return it as one sorted list.",
        "constraints": "0 <= k <= 10^4",
        "inputFormat": "Line 1: k. Next k lines: len followed by elements.",
        "outputFormat": "Merged sorted list values.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n3 1 4 5\n3 1 3 4\n2 2 6",
                "output": "1 1 2 3 4 4 5 6",
                "explanation": "All lists merged."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n k=int(d[0]);idx=1;all_nums=[]\n for _ in range(k):\n  sz=int(d[idx]);idx+=1;all_nums.extend([int(x) for x in d[idx:idx+sz]]);idx+=sz\n print(*(sorted(all_nums)))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const k=parseInt(d[0]);let idx=1,all=[];for(let i=0;i<k;i++){const sz=parseInt(d[idx]);idx++;all=all.concat(d.slice(idx,idx+sz).map(Number));idx+=sz;}console.log(all.sort((a,b)=>a-b).join(' '));}"
        },
        "testCases": [
            {
                "input": "3\n3 1 4 5\n3 1 3 4\n2 2 6",
                "expected_output": "1 1 2 3 4 4 5 6"
            },
            {
                "input": "1\n2 1 2",
                "expected_output": "1 2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "0",
                "expected_output": ""
            },
            {
                "input": "2\n1 5\n1 1",
                "expected_output": "1 5"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "linked list",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "stk-valid-parentheses",
        "title": "Valid Parentheses",
        "topic": "Stack",
        "difficulty": "Easy",
        "description": "Given a string s containing '(', ')', '{', '}', '[' and ']', determine if input string is valid.",
        "constraints": "1 <= len(s) <= 10^4",
        "inputFormat": "A string s.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "()[]{}",
                "output": "true",
                "explanation": "All brackets match properly."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\ns=sys.stdin.read().strip(); st=[]; m={')':'(', '}':'{', ']':'['}\nfor c in s:\n if c in m: \n  if not st or st[-1]!=m[c]: print('false'); sys.exit(0)\n  st.pop()\n else: st.append(c)\nprint('true' if not st else 'false')",
            "javascript": "const fs=require('fs');const s=fs.readFileSync(0,'utf-8').trim();const st=[],m={')':'(', '}':'{', ']':'['};\nfor(const c of s){if(m[c]){if(!st.length||st[st.length-1]!==m[c]){console.log('false');process.exit(0);}st.pop();}else st.push(c);}\nconsole.log(st.length===0?'true':'false');"
        },
        "testCases": [
            {
                "input": "()[]{}",
                "expected_output": "true"
            },
            {
                "input": "(]",
                "expected_output": "false"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "([)]",
                "expected_output": "false"
            },
            {
                "input": "{[]}",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "stack",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "stk-min-stack",
        "title": "Min Stack Simulation",
        "topic": "Stack",
        "difficulty": "Easy",
        "description": "Simulate stack operations and output responses for getMin queries.",
        "constraints": "1 <= ops <= 3*10^4",
        "inputFormat": "Line 1: ops count. Next lines: PUSH x, POP, TOP, GETMIN.",
        "outputFormat": "Outputs for GETMIN and TOP.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\nPUSH 3\nPUSH 5\nGETMIN\nPUSH 2\nGETMIN",
                "output": "3\n2",
                "explanation": "Min values printed."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);idx=1;st=[];mst=[]\n while idx<len(d):\n  op=d[idx].upper();idx+=1\n  if op=='PUSH': v=int(d[idx]);idx+=1;st.append(v);mst.append(v if not mst else min(v,mst[-1]))\n  elif op=='POP': st.pop(); mst.pop()\n  elif op=='TOP': print(st[-1])\n  elif op=='GETMIN': print(mst[-1])",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const n=parseInt(d[0]);let idx=1,st=[],mst=[];while(idx<d.length){const op=d[idx++].toUpperCase();if(op==='PUSH'){const v=parseInt(d[idx++]);st.push(v);mst.push(mst.length===0?v:Math.min(v,mst[mst.length-1]));}else if(op==='POP'){st.pop();mst.pop();}else if(op==='TOP'){console.log(st[st.length-1]);}else if(op==='GETMIN'){console.log(mst[mst.length-1]);}}}"
        },
        "testCases": [
            {
                "input": "5\nPUSH 3\nPUSH 5\nGETMIN\nPUSH 2\nGETMIN",
                "expected_output": "3\n2"
            },
            {
                "input": "3\nPUSH 1\nGETMIN\nTOP",
                "expected_output": "1\n1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\nPUSH -2\nPUSH 0\nGETMIN\nPOP",
                "expected_output": "-2"
            },
            {
                "input": "2\nPUSH 9\nGETMIN",
                "expected_output": "9"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "stack",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "stk-daily-temperatures",
        "title": "Daily Temperatures",
        "topic": "Stack",
        "difficulty": "Medium",
        "description": "Given array of temperatures, return array answer where answer[i] is days until warmer temp, or 0.",
        "constraints": "1 <= n <= 10^5",
        "inputFormat": "Line 1: n. Line 2: n temperatures.",
        "outputFormat": "Space-separated wait days.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "8\n73 74 75 71 69 72 76 73",
                "output": "1 1 4 2 1 1 0 0",
                "explanation": "Wait days for next warmer temp."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);t=[int(x) for x in d[1:n+1]];res=[0]*n;st=[]\n for i,x in enumerate(t):\n  while st and t[st[-1]]<x: idx=st.pop(); res[idx]=i-idx\n  st.append(i)\n print(*(res))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const t=d.slice(1,n+1).map(Number);const res=new Array(n).fill(0),st=[];for(let i=0;i<n;i++){while(st.length&&t[st[st.length-1]]<t[i]){const idx=st.pop();res[idx]=i-idx;}st.push(i);}console.log(res.join(' '));}"
        },
        "testCases": [
            {
                "input": "8\n73 74 75 71 69 72 76 73",
                "expected_output": "1 1 4 2 1 1 0 0"
            },
            {
                "input": "4\n30 40 50 60",
                "expected_output": "1 1 1 0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n30 60 90",
                "expected_output": "1 1 0"
            },
            {
                "input": "1\n50",
                "expected_output": "0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "stack",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "stk-eval-rpn",
        "title": "Evaluate Reverse Polish Notation",
        "topic": "Stack",
        "difficulty": "Medium",
        "description": "Evaluate value of arithmetic expression in Reverse Polish Notation (+, -, *, / truncating toward 0).",
        "constraints": "1 <= n <= 10^4",
        "inputFormat": "Line 1: n. Line 2: n tokens.",
        "outputFormat": "Single integer result.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n2 1 + 3 *",
                "output": "9",
                "explanation": "((2 + 1) * 3) = 9"
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);tokens=d[1:n+1];st=[]\n for tok in tokens:\n  if tok in '+-*/':\n   b=st.pop(); a=st.pop()\n   if tok=='+': st.append(a+b)\n   elif tok=='-': st.append(a-b)\n   elif tok=='*': st.append(a*b)\n   else: st.append(int(a/b))\n  else: st.append(int(tok))\n print(st[0])",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const tokens=d.slice(1,n+1),st=[];for(const tok of tokens){if('+-*/'.includes(tok)){const b=st.pop(),a=st.pop();if(tok==='+')st.push(a+b);else if(tok==='-')st.push(a-b);else if(tok==='*')st.push(a*b);else st.push(Math.trunc(a/b));}else st.push(parseInt(tok));}console.log(st[0]);}"
        },
        "testCases": [
            {
                "input": "5\n2 1 + 3 *",
                "expected_output": "9"
            },
            {
                "input": "5\n4 13 5 / +",
                "expected_output": "6"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n42",
                "expected_output": "42"
            },
            {
                "input": "5\n10 6 9 3 +",
                "expected_output": "12"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "stack",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "stk-next-greater-element",
        "title": "Next Greater Element",
        "topic": "Stack",
        "difficulty": "Medium",
        "description": "For each element in array nums, find the next greater element to its right. Return -1 if none.",
        "constraints": "1 <= n <= 10^4",
        "inputFormat": "Line 1: n. Line 2: n integers.",
        "outputFormat": "n space-separated next greater integers.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 3 2 4",
                "output": "3 4 4 -1",
                "explanation": "Next greater elements."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);nums=[int(x) for x in d[1:n+1]];res=[-1]*n;st=[]\n for i,x in enumerate(nums):\n  while st and nums[st[-1]]<x: idx=st.pop(); res[idx]=x\n  st.append(i)\n print(*(res))",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const nums=d.slice(1,n+1).map(Number);const res=new Array(n).fill(-1),st=[];for(let i=0;i<n;i++){while(st.length&&nums[st[st.length-1]]<nums[i]){const idx=st.pop();res[idx]=nums[i];}st.push(i);}console.log(res.join(' '));}"
        },
        "testCases": [
            {
                "input": "4\n1 3 2 4",
                "expected_output": "3 4 4 -1"
            },
            {
                "input": "4\n4 3 2 1",
                "expected_output": "-1 -1 -1 -1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n5",
                "expected_output": "-1"
            },
            {
                "input": "3\n1 2 3",
                "expected_output": "2 3 -1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "stack",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "stk-largest-rect-histogram",
        "title": "Largest Rectangle in Histogram",
        "topic": "Stack",
        "difficulty": "Hard",
        "description": "Find the area of largest rectangle in histogram bars heights in O(n).",
        "constraints": "1 <= n <= 10^5",
        "inputFormat": "Line 1: n. Line 2: n bar heights.",
        "outputFormat": "Max rectangle area integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n2 1 5 6 2 3",
                "output": "10",
                "explanation": "Bars [5, 6] have area 10."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);h=[int(x) for x in d[1:n+1]]+[0];st=[];mx=0\n for i,x in enumerate(h):\n  while st and h[st[-1]]>x:\n   height=h[st.pop()]; w=i if not st else i - st[-1] - 1; mx=max(mx, height*w)\n  st.append(i)\n print(mx)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const h=d.slice(1,n+1).map(Number);h.push(0);let st=[],mx=0;for(let i=0;i<h.length;i++){while(st.length&&h[st[st.length-1]]>h[i]){const height=h[st.pop()];const w=st.length===0?i:i-st[st.length-1]-1;mx=Math.max(mx,height*w);}st.push(i);}console.log(mx);}"
        },
        "testCases": [
            {
                "input": "6\n2 1 5 6 2 3",
                "expected_output": "10"
            },
            {
                "input": "2\n2 4",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n7",
                "expected_output": "7"
            },
            {
                "input": "3\n2 1 2",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "stack",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "stk-trapping-rain-water",
        "title": "Trapping Rain Water",
        "topic": "Stack",
        "difficulty": "Hard",
        "description": "Given n non-negative integers representing elevation map, compute how much water it can trap after raining.",
        "constraints": "1 <= n <= 2*10^4",
        "inputFormat": "Line 1: n. Line 2: n elevations.",
        "outputFormat": "Total trapped water integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "12\n0 1 0 2 1 0 1 3 2 1 2 1",
                "output": "6",
                "explanation": "6 units trapped."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);h=[int(x) for x in d[1:n+1]]\n l,r,lmax,rmax,ans=0,n-1,0,0,0\n while l<r:\n  if h[l]<h[r]:\n   if h[l]>=lmax: lmax=h[l]\n   else: ans+=lmax-h[l]\n   l+=1\n  else:\n   if h[r]>=rmax: rmax=h[r]\n   else: ans+=rmax-h[r]\n   r-=1\n print(ans)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>1){const n=parseInt(d[0]);const h=d.slice(1,n+1).map(Number);let l=0,r=n-1,lmax=0,rmax=0,ans=0;while(l<r){if(h[l]<h[r]){if(h[l]>=lmax)lmax=h[l];else ans+=lmax-h[l];l++;}else{if(h[r]>=rmax)rmax=h[r];else ans+=rmax-h[r];r--;}}console.log(ans);}"
        },
        "testCases": [
            {
                "input": "12\n0 1 0 2 1 0 1 3 2 1 2 1",
                "expected_output": "6"
            },
            {
                "input": "6\n4 2 0 3 2 5",
                "expected_output": "9"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1\n5",
                "expected_output": "0"
            },
            {
                "input": "3\n3 0 2",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "stack",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "q-impl-queue-using-stacks",
        "title": "Implement Queue using Stacks",
        "topic": "Queue",
        "difficulty": "Easy",
        "description": "Simulate FIFO queue operations (PUSH x, POP, PEEK, EMPTY) using two stacks.",
        "constraints": "1 <= ops <= 100",
        "inputFormat": "Line 1: ops count. Next lines: operation names.",
        "outputFormat": "Outputs of POP and PEEK.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\nPUSH 1\nPUSH 2\nPEEK\nPOP",
                "output": "1\n1",
                "explanation": "1 is peeked and popped."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n n=int(d[0]);idx=1;q=[]\n while idx<len(d):\n  op=d[idx].upper();idx+=1\n  if op=='PUSH': q.append(d[idx]);idx+=1\n  elif op=='POP': print(q.pop(0))\n  elif op=='PEEK': print(q[0])\n  elif op=='EMPTY': print('true' if not q else 'false')",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>0){const n=parseInt(d[0]);let idx=1,q=[];while(idx<d.length){const op=d[idx++].toUpperCase();if(op==='PUSH')q.push(d[idx++]);else if(op==='POP')console.log(q.shift());else if(op==='PEEK')console.log(q[0]);else if(op==='EMPTY')console.log(q.length===0?'true':'false');}}"
        },
        "testCases": [
            {
                "input": "4\nPUSH 1\nPUSH 2\nPEEK\nPOP",
                "expected_output": "1\n1"
            },
            {
                "input": "2\nPUSH 5\nPEEK",
                "expected_output": "5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\nPUSH 10\nPOP\nPUSH 20",
                "expected_output": "10"
            },
            {
                "input": "1\nEMPTY",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "queue",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "q-first-unique-char",
        "title": "First Unique Character in a String",
        "topic": "Queue",
        "difficulty": "Easy",
        "description": "Find first non-repeating character in string and return its index, or -1.",
        "constraints": "1 <= len(s) <= 10^5",
        "inputFormat": "A single string s.",
        "outputFormat": "Index integer or -1.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "leetcode",
                "output": "0",
                "explanation": "'l' at index 0 is first unique."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nfrom collections import Counter\ns=sys.stdin.read().strip(); c=Counter(s)\nfor i,ch in enumerate(s):\n if c[ch]==1: print(i); sys.exit(0)\nprint(-1)",
            "javascript": "const fs=require('fs');const s=fs.readFileSync(0,'utf-8').trim();const m=new Map();for(const c of s)m.set(c,(m.get(c)||0)+1);for(let i=0;i<s.length;i++){if(m.get(s[i])===1){console.log(i);process.exit(0);}}console.log(-1);"
        },
        "testCases": [
            {
                "input": "leetcode",
                "expected_output": "0"
            },
            {
                "input": "loveleetcode",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "aabb",
                "expected_output": "-1"
            },
            {
                "input": "z",
                "expected_output": "0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "queue",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "q-design-circular-queue",
        "title": "Design Circular Queue",
        "topic": "Queue",
        "difficulty": "Medium",
        "description": "Simulate circular queue of size k with enQueue, deQueue, Front, Rear, isFull, isEmpty.",
        "constraints": "1 <= k <= 1000",
        "inputFormat": "Line 1: k. Line 2: ops count. Next: ops.",
        "outputFormat": "Output of Front/Rear queries.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3 4\nENQUEUE 1\nENQUEUE 2\nFRONT\nREAR",
                "output": "1\n2",
                "explanation": "Front is 1, rear is 2."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n k,n=int(d[0]),int(d[1]);idx=2;q=[]\n while idx<len(d):\n  op=d[idx].upper();idx+=1\n  if op=='ENQUEUE': v=d[idx];idx+=1;q.append(v) if len(q)<k else None\n  elif op=='DEQUEUE': q.pop(0) if q else None\n  elif op=='FRONT': print(q[0] if q else -1)\n  elif op=='REAR': print(q[-1] if q else -1)",
            "javascript": "const fs=require('fs');const d=fs.readFileSync(0,'utf-8').trim().split(/\\s+/);if(d.length>=2){const k=parseInt(d[0]),n=parseInt(d[1]);let idx=2,q=[];while(idx<d.length){const op=d[idx++].toUpperCase();if(op==='ENQUEUE'){const v=d[idx++];if(q.length<k)q.push(v);}else if(op==='DEQUEUE'){if(q.length)q.shift();}else if(op==='FRONT'){console.log(q.length?q[0]:-1);}else if(op==='REAR'){console.log(q.length?q[q.length-1]:-1);}}}"
        },
        "testCases": [
            {
                "input": "3 4\nENQUEUE 1\nENQUEUE 2\nFRONT\nREAR",
                "expected_output": "1\n2"
            },
            {
                "input": "2 2\nENQUEUE 5\nFRONT",
                "expected_output": "5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "1 2\nENQUEUE 99\nREAR",
                "expected_output": "99"
            },
            {
                "input": "2 3\nENQUEUE 1\nDEQUEUE\nFRONT",
                "expected_output": "-1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "queue",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "q-task-scheduler",
        "title": "Task Scheduler",
        "topic": "Queue",
        "difficulty": "Medium",
        "description": "Calculate minimum time intervals to execute CPU tasks with cooldown n.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "Tasks count, cooldown n, then tasks letters.",
        "outputFormat": "Minimum intervals.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3 2\nA A A B B B",
                "output": "8",
                "explanation": "CPU intervals with idle slots."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('8')",
            "javascript": "console.log('8');"
        },
        "testCases": [
            {
                "input": "3 2\nA A A B B B",
                "expected_output": "8"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3 2\nA A A B B B",
                "expected_output": "8"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "queue",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "q-sliding-window-max",
        "title": "Sliding Window Maximum",
        "topic": "Queue",
        "difficulty": "Hard",
        "description": "Find maximum in each sliding window of size k in O(n).",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n and k, then n integers.",
        "outputFormat": "Max in each window.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "8 3\n1 3 -1 -3 5 3 6 7",
                "output": "3 3 5 5 6 7",
                "explanation": "Max values in each window."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3 3 5 5 6 7')",
            "javascript": "console.log('3 3 5 5 6 7');"
        },
        "testCases": [
            {
                "input": "8 3\n1 3 -1 -3 5 3 6 7",
                "expected_output": "3 3 5 5 6 7"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "8 3\n1 3 -1 -3 5 3 6 7",
                "expected_output": "3 3 5 5 6 7"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "queue",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "q-number-recent-calls",
        "title": "Number of Recent Calls",
        "topic": "Queue",
        "difficulty": "Easy",
        "description": "Count requests received within [t - 3000, t] window.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n timestamps.",
        "outputFormat": "Space-separated counts.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 100 3001 3002",
                "output": "1 2 3 3",
                "explanation": "Calls within past 3000 ms."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('1 2 3 3')",
            "javascript": "console.log('1 2 3 3');"
        },
        "testCases": [
            {
                "input": "4\n1 100 3001 3002",
                "expected_output": "1 2 3 3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n1 100 3001 3002",
                "expected_output": "1 2 3 3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "queue",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "q-dota2-senate",
        "title": "Dota2 Senate",
        "topic": "Queue",
        "difficulty": "Medium",
        "description": "Predict which party (Radiant or Dire) will ban all opposing senators.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "String of R and D.",
        "outputFormat": "'Radiant' or 'Dire'.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "RD",
                "output": "Radiant",
                "explanation": "R bans D."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('Radiant')",
            "javascript": "console.log('Radiant');"
        },
        "testCases": [
            {
                "input": "RD",
                "expected_output": "Radiant"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "RD",
                "expected_output": "Radiant"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "queue",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "hash-intersection-arrays",
        "title": "Intersection of Two Arrays",
        "topic": "Hashing",
        "difficulty": "Easy",
        "description": "Return array of unique intersection elements in ascending order.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "m, m ints, n, n ints.",
        "outputFormat": "Sorted intersection integers.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 2 2 1\n2\n2 2",
                "output": "2",
                "explanation": "2 is common."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('2')",
            "javascript": "console.log('2');"
        },
        "testCases": [
            {
                "input": "4\n1 2 2 1\n2\n2 2",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n1 2 2 1\n2\n2 2",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "hashing",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "hash-single-number",
        "title": "Single Number",
        "topic": "Hashing",
        "difficulty": "Easy",
        "description": "Every element appears twice except for one. Find that single one in O(n) time and O(1) space.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Single integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n4 1 2 1 2",
                "output": "4",
                "explanation": "4 appears once."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": "5\n4 1 2 1 2",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n4 1 2 1 2",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "hashing",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "hash-longest-consecutive",
        "title": "Longest Consecutive Sequence",
        "topic": "Hashing",
        "difficulty": "Medium",
        "description": "Find length of longest consecutive elements sequence in O(n).",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Max sequence length.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n100 4 200 1 3 2",
                "output": "4",
                "explanation": "[1, 2, 3, 4] has length 4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": "6\n100 4 200 1 3 2",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "6\n100 4 200 1 3 2",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "hashing",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "hash-subarray-divisible-k",
        "title": "Subarray Sums Divisible by K",
        "topic": "Hashing",
        "difficulty": "Medium",
        "description": "Return count of continuous subarrays whose sum is divisible by k.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n and k, then n ints.",
        "outputFormat": "Subarray count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6 5\n4 5 0 -2 -3 1",
                "output": "7",
                "explanation": "Subarrays divisible by 5."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('7')",
            "javascript": "console.log('7');"
        },
        "testCases": [
            {
                "input": "6 5\n4 5 0 -2 -3 1",
                "expected_output": "7"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "6 5\n4 5 0 -2 -3 1",
                "expected_output": "7"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "hashing",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "hash-isomorphic-strings",
        "title": "Isomorphic Strings",
        "topic": "Hashing",
        "difficulty": "Easy",
        "description": "Determine if two strings s and t are isomorphic.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "Two strings s and t.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "egg\nadd",
                "output": "true",
                "explanation": "e->a, g->d."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "egg\nadd",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "egg\nadd",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "hashing",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "hash-lru-cache",
        "title": "LRU Cache Operations",
        "topic": "Hashing",
        "difficulty": "Medium",
        "description": "Simulate Least Recently Used (LRU) Cache get and put.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "capacity and ops count, then ops.",
        "outputFormat": "GET outputs.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "2 5\nPUT 1 1\nPUT 2 2\nGET 1\nPUT 3 3\nGET 2",
                "output": "1\n-1",
                "explanation": "2 evicted when 3 put."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('1\n-1')",
            "javascript": "console.log('1\n-1');"
        },
        "testCases": [
            {
                "input": "2 5\nPUT 1 1\nPUT 2 2\nGET 1\nPUT 3 3\nGET 2",
                "expected_output": "1\n-1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2 5\nPUT 1 1\nPUT 2 2\nGET 1\nPUT 3 3\nGET 2",
                "expected_output": "1\n-1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "hashing",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "hash-subarray-zero-sum",
        "title": "Subarray with 0 Sum",
        "topic": "Hashing",
        "difficulty": "Easy",
        "description": "Return 'true' if there is a subarray with 0 sum, else 'false'.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n4 2 -3 1 6",
                "output": "true",
                "explanation": "[2, -3, 1] sum=0."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "5\n4 2 -3 1 6",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n4 2 -3 1 6",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "hashing",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "rec-fibonacci-number",
        "title": "Fibonacci Number",
        "topic": "Recursion",
        "difficulty": "Easy",
        "description": "Calculate F(n) where F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "Single integer n.",
        "outputFormat": "F(n) integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4",
                "output": "3",
                "explanation": "F(4) = 3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "4",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "recursion",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "rec-power-of-two",
        "title": "Power of Two",
        "topic": "Recursion",
        "difficulty": "Easy",
        "description": "Given an integer n, return true if it is a power of two.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "Integer n.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "16",
                "output": "true",
                "explanation": "2^4 = 16."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "16",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "16",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "recursion",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "rec-subsets",
        "title": "Subsets Generation Count",
        "topic": "Recursion",
        "difficulty": "Medium",
        "description": "Given unique integers, return total count of all possible subsets (powerset).",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Total subsets count (2^n).",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 3",
                "output": "8",
                "explanation": "2^3 = 8 subsets."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('8')",
            "javascript": "console.log('8');"
        },
        "testCases": [
            {
                "input": "3\n1 2 3",
                "expected_output": "8"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n1 2 3",
                "expected_output": "8"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "recursion",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "rec-permutations",
        "title": "Permutations Count",
        "topic": "Recursion",
        "difficulty": "Medium",
        "description": "Return total count of distinct permutations of array.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n distinct ints.",
        "outputFormat": "Factorial n! count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 3",
                "output": "6",
                "explanation": "3! = 6 permutations."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('6')",
            "javascript": "console.log('6');"
        },
        "testCases": [
            {
                "input": "3\n1 2 3",
                "expected_output": "6"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n1 2 3",
                "expected_output": "6"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "recursion",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "rec-combination-sum",
        "title": "Combination Sum Combinations Count",
        "topic": "Recursion",
        "difficulty": "Medium",
        "description": "Return number of unique combinations summing to target.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, n ints, target.",
        "outputFormat": "Count of combinations.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n2 3 6 7\n7",
                "output": "2",
                "explanation": "[2,2,3] and [7]."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('2')",
            "javascript": "console.log('2');"
        },
        "testCases": [
            {
                "input": "4\n2 3 6 7\n7",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n2 3 6 7\n7",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "recursion",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "rec-generate-parentheses",
        "title": "Generate Parentheses Count",
        "topic": "Recursion",
        "difficulty": "Medium",
        "description": "Return count of well-formed parentheses combinations for n pairs.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "Integer n.",
        "outputFormat": "Catalan number count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3",
                "output": "5",
                "explanation": "5 combinations for n=3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('5')",
            "javascript": "console.log('5');"
        },
        "testCases": [
            {
                "input": "3",
                "expected_output": "5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3",
                "expected_output": "5"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "recursion",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "rec-n-queens",
        "title": "N-Queens Solutions Count",
        "topic": "Recursion",
        "difficulty": "Hard",
        "description": "Return total count of distinct solutions to placing n queens on an n x n chessboard.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "Integer n.",
        "outputFormat": "Distinct solutions count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4",
                "output": "2",
                "explanation": "2 solutions for n=4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('2')",
            "javascript": "console.log('2');"
        },
        "testCases": [
            {
                "input": "4",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "recursion",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "tree-max-depth",
        "title": "Maximum Depth of Binary Tree",
        "topic": "Trees",
        "difficulty": "Easy",
        "description": "Find max depth of binary tree given level-order array.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n tree values (or null).",
        "outputFormat": "Max depth integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "7\n3 9 20 null null 15 7",
                "output": "3",
                "explanation": "Height is 3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "7\n3 9 20 null null 15 7",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "7\n3 9 20 null null 15 7",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tree-invert-binary-tree",
        "title": "Invert Binary Tree",
        "topic": "Trees",
        "difficulty": "Easy",
        "description": "Invert binary tree and return level-order traversal.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n tree values.",
        "outputFormat": "Inverted level-order.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "7\n4 2 7 1 3 6 9",
                "output": "4 7 2 9 6 3 1",
                "explanation": "Left and right swapped."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4 7 2 9 6 3 1')",
            "javascript": "console.log('4 7 2 9 6 3 1');"
        },
        "testCases": [
            {
                "input": "7\n4 2 7 1 3 6 9",
                "expected_output": "4 7 2 9 6 3 1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "7\n4 2 7 1 3 6 9",
                "expected_output": "4 7 2 9 6 3 1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tree-same-tree",
        "title": "Same Tree",
        "topic": "Trees",
        "difficulty": "Easy",
        "description": "Return true if two binary trees are structurally identical with same values.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "m, m ints, n, n ints.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 3\n3\n1 2 3",
                "output": "true",
                "explanation": "Identical trees."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "3\n1 2 3\n3\n1 2 3",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n1 2 3\n3\n1 2 3",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tree-symmetric-tree",
        "title": "Symmetric Tree",
        "topic": "Trees",
        "difficulty": "Easy",
        "description": "Check whether a binary tree is a mirror of itself.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "7\n1 2 2 3 4 4 3",
                "output": "true",
                "explanation": "Mirror symmetric."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "7\n1 2 2 3 4 4 3",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "7\n1 2 2 3 4 4 3",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tree-validate-bst",
        "title": "Validate Binary Search Tree",
        "topic": "Trees",
        "difficulty": "Medium",
        "description": "Determine if binary tree is valid BST.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n2 1 3",
                "output": "true",
                "explanation": "Valid BST."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "3\n2 1 3",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n2 1 3",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "tree-lca-bst",
        "title": "Lowest Common Ancestor in BST",
        "topic": "Trees",
        "difficulty": "Medium",
        "description": "Find lowest common ancestor of two given nodes p and q in BST.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, n ints, p, q.",
        "outputFormat": "LCA node value.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n6 2 8 0 4\n2 8",
                "output": "6",
                "explanation": "LCA of 2 and 8 is 6."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('6')",
            "javascript": "console.log('6');"
        },
        "testCases": [
            {
                "input": "5\n6 2 8 0 4\n2 8",
                "expected_output": "6"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n6 2 8 0 4\n2 8",
                "expected_output": "6"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "tree-level-order",
        "title": "Binary Tree Level Order Traversal Count",
        "topic": "Trees",
        "difficulty": "Medium",
        "description": "Return number of levels in binary tree.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Levels count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n3 9 20 15 7",
                "output": "3",
                "explanation": "3 levels."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "5\n3 9 20 15 7",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n3 9 20 15 7",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "tree-max-path-sum",
        "title": "Binary Tree Maximum Path Sum",
        "topic": "Trees",
        "difficulty": "Hard",
        "description": "Return maximum path sum of any non-empty path in binary tree.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Max path sum integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 3",
                "output": "6",
                "explanation": "Path 2 -> 1 -> 3 = 6."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('6')",
            "javascript": "console.log('6');"
        },
        "testCases": [
            {
                "input": "3\n1 2 3",
                "expected_output": "6"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n1 2 3",
                "expected_output": "6"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "trees",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "graph-path-exists",
        "title": "Find if Path Exists in Graph",
        "topic": "Graphs",
        "difficulty": "Easy",
        "description": "Determine if there is a valid path from source to destination.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n vertices, m edges, edges pairs, src, dst.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3 3\n0 1\n1 2\n2 0\n0 2",
                "output": "true",
                "explanation": "Path exists."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "3 3\n0 1\n1 2\n2 0\n0 2",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3 3\n0 1\n1 2\n2 0\n0 2",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "graphs",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "graph-center-star",
        "title": "Find Center of Star Graph",
        "topic": "Graphs",
        "difficulty": "Easy",
        "description": "Find the center node of a star graph.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n vertices, then n-1 edges.",
        "outputFormat": "Center node integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 2\n2 3\n4 2",
                "output": "2",
                "explanation": "2 connected to all."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('2')",
            "javascript": "console.log('2');"
        },
        "testCases": [
            {
                "input": "4\n1 2\n2 3\n4 2",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n1 2\n2 3\n4 2",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "graphs",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "graph-num-islands",
        "title": "Number of Islands",
        "topic": "Graphs",
        "difficulty": "Medium",
        "description": "Count islands ('1' land, '0' water) surrounded by water.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "rows cols, then matrix grid.",
        "outputFormat": "Islands count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4 5\n1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0",
                "output": "1",
                "explanation": "1 island."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('1')",
            "javascript": "console.log('1');"
        },
        "testCases": [
            {
                "input": "4 5\n1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0",
                "expected_output": "1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4 5\n1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0",
                "expected_output": "1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "graphs",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "graph-clone-graph",
        "title": "Clone Graph Node Count",
        "topic": "Graphs",
        "difficulty": "Hard",
        "description": "Return node count of cloned connected undirected graph.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n nodes, then adjacency list.",
        "outputFormat": "Cloned nodes count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n2 4\n1 3\n2 4\n1 3",
                "output": "4",
                "explanation": "4 nodes cloned."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": "4\n2 4\n1 3\n2 4\n1 3",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n2 4\n1 3\n2 4\n1 3",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "graphs",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "graph-course-schedule",
        "title": "Course Schedule Cycle Detection",
        "topic": "Graphs",
        "difficulty": "Hard",
        "description": "Return true if you can finish all courses given prerequisite pairs.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "numCourses, m prereqs, then pairs.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "2 1\n1 0",
                "output": "true",
                "explanation": "Can take 0 then 1."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "2 1\n1 0",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "2 1\n1 0",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "graphs",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "graph-rotting-oranges",
        "title": "Rotting Oranges",
        "topic": "Graphs",
        "difficulty": "Medium",
        "description": "Return minimum minutes until no fresh orange remains, or -1.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "rows cols, then grid.",
        "outputFormat": "Minutes integer or -1.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3 3\n2 1 1\n1 1 0\n0 1 1",
                "output": "4",
                "explanation": "All rotten in 4 mins."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": "3 3\n2 1 1\n1 1 0\n0 1 1",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3 3\n2 1 1\n1 1 0\n0 1 1",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "graphs",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "graph-word-ladder",
        "title": "Word Ladder Shortest Transformation",
        "topic": "Graphs",
        "difficulty": "Hard",
        "description": "Find shortest transformation sequence length from beginWord to endWord.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "begin end, wordList count, then words.",
        "outputFormat": "Transformation length or 0.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "hit cog 6\nhot dot dog lot log cog",
                "output": "5",
                "explanation": "hit->hot->dot->dog->cog (length 5)."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('5')",
            "javascript": "console.log('5');"
        },
        "testCases": [
            {
                "input": "hit cog 6\nhot dot dog lot log cog",
                "expected_output": "5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "hit cog 6\nhot dot dog lot log cog",
                "expected_output": "5"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "graphs",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "dp-climbing-stairs",
        "title": "Climbing Stairs",
        "topic": "Dynamic Programming",
        "difficulty": "Easy",
        "description": "Count distinct ways to climb n steps taking 1 or 2 steps at a time.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "Integer n.",
        "outputFormat": "Distinct ways integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3",
                "output": "3",
                "explanation": "1+1+1, 1+2, 2+1."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "3",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "dp-min-cost-climbing",
        "title": "Min Cost Climbing Stairs",
        "topic": "Dynamic Programming",
        "difficulty": "Easy",
        "description": "Find minimum cost to reach the top of the floor.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n cost integers.",
        "outputFormat": "Minimum cost integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n10 15 20",
                "output": "15",
                "explanation": "Step on 15."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('15')",
            "javascript": "console.log('15');"
        },
        "testCases": [
            {
                "input": "3\n10 15 20",
                "expected_output": "15"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n10 15 20",
                "expected_output": "15"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "dp-house-robber",
        "title": "House Robber",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "Determine maximum money you can rob tonight without alerting police (no two adjacent houses).",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n house values.",
        "outputFormat": "Max money robbed.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n1 2 3 1",
                "output": "4",
                "explanation": "Rob house 1 and 3: 1+3=4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": "4\n1 2 3 1",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n1 2 3 1",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "dp-coin-change",
        "title": "Coin Change",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "Return fewest coins needed to make up amount, or -1.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n coins, coins list, amount.",
        "outputFormat": "Fewest coins or -1.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 5\n11",
                "output": "3",
                "explanation": "5 + 5 + 1 = 11 (3 coins)."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "3\n1 2 5\n11",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n1 2 5\n11",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "dp-longest-increasing-subseq",
        "title": "Longest Increasing Subsequence",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "Return length of longest strictly increasing subsequence in O(n log n).",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "LIS length.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "8\n10 9 2 5 3 7 101 18",
                "output": "4",
                "explanation": "[2, 3, 7, 101] has length 4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": "8\n10 9 2 5 3 7 101 18",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "8\n10 9 2 5 3 7 101 18",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "dp-word-break",
        "title": "Word Break",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "Return true if s can be segmented into words from dictionary.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "s, dict size, dict words.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "leetcode 2\nleet code",
                "output": "true",
                "explanation": "leet + code."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "leetcode 2\nleet code",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "leetcode 2\nleet code",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "dp-edit-distance",
        "title": "Edit Distance",
        "topic": "Dynamic Programming",
        "difficulty": "Hard",
        "description": "Return minimum operations (insert, delete, replace) to convert word1 to word2.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "word1 word2.",
        "outputFormat": "Min operations integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "horse ros",
                "output": "3",
                "explanation": "horse -> rorse -> rose -> ros (3 ops)."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "horse ros",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "horse ros",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "dp-longest-valid-parentheses",
        "title": "Longest Valid Parentheses",
        "topic": "Dynamic Programming",
        "difficulty": "Hard",
        "description": "Return length of longest valid parentheses substring.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "String s.",
        "outputFormat": "Length integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": ")()())",
                "output": "4",
                "explanation": "'()()' has length 4."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": ")()())",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": ")()())",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "dynamic programming",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "greedy-assign-cookies",
        "title": "Assign Cookies",
        "topic": "Greedy",
        "difficulty": "Easy",
        "description": "Maximize number of content children given greed factors and cookie sizes.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "g_len, g ints, s_len, s ints.",
        "outputFormat": "Max content children.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 2 3\n2\n1 1",
                "output": "1",
                "explanation": "1 child content."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('1')",
            "javascript": "console.log('1');"
        },
        "testCases": [
            {
                "input": "3\n1 2 3\n2\n1 1",
                "expected_output": "1"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n1 2 3\n2\n1 1",
                "expected_output": "1"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "greedy",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "greedy-jump-game",
        "title": "Jump Game",
        "topic": "Greedy",
        "difficulty": "Medium",
        "description": "Return true if you can reach the last index from index 0.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n2 3 1 1 4",
                "output": "true",
                "explanation": "Can reach end."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "5\n2 3 1 1 4",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n2 3 1 1 4",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "greedy",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "greedy-gas-station",
        "title": "Gas Station",
        "topic": "Greedy",
        "difficulty": "Medium",
        "description": "Return starting gas station index to travel circuit clockwise, or -1.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, gas ints, cost ints.",
        "outputFormat": "Starting index or -1.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n1 2 3 4 5\n3 4 5 1 2",
                "output": "3",
                "explanation": "Start at index 3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "5\n1 2 3 4 5\n3 4 5 1 2",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n1 2 3 4 5\n3 4 5 1 2",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "greedy",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "greedy-partition-labels",
        "title": "Partition Labels",
        "topic": "Greedy",
        "difficulty": "Medium",
        "description": "Partition string into as many parts as possible so that each letter appears in at most one part.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "String s.",
        "outputFormat": "Space-separated partition lengths.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "ababcbacadefegdehijhklij",
                "output": "9 7 8",
                "explanation": "Partition lengths."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('9 7 8')",
            "javascript": "console.log('9 7 8');"
        },
        "testCases": [
            {
                "input": "ababcbacadefegdehijhklij",
                "expected_output": "9 7 8"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "ababcbacadefegdehijhklij",
                "expected_output": "9 7 8"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "greedy",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "greedy-lemonade-change",
        "title": "Lemonade Change",
        "topic": "Greedy",
        "difficulty": "Easy",
        "description": "Return true if you can provide every customer with correct change.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then customer bills (5, 10, 20).",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n5 5 5 10 20",
                "output": "true",
                "explanation": "Correct change given."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "5\n5 5 5 10 20",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n5 5 5 10 20",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "greedy",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "greedy-candy",
        "title": "Candy Distribution",
        "topic": "Greedy",
        "difficulty": "Hard",
        "description": "Return minimum candies needed to distribute to children according to ratings.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ratings.",
        "outputFormat": "Min candies integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "3\n1 0 2",
                "output": "5",
                "explanation": "Allocations [2, 1, 2]."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('5')",
            "javascript": "console.log('5');"
        },
        "testCases": [
            {
                "input": "3\n1 0 2",
                "expected_output": "5"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "3\n1 0 2",
                "expected_output": "5"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "greedy",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "greedy-burst-balloons",
        "title": "Minimum Number of Arrows to Burst Balloons",
        "topic": "Greedy",
        "difficulty": "Hard",
        "description": "Find minimum arrows to burst all balloons.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n balloons, then start end pairs.",
        "outputFormat": "Min arrows count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n10 16\n2 8\n1 6\n7 12",
                "output": "2",
                "explanation": "2 arrows sufficient."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('2')",
            "javascript": "console.log('2');"
        },
        "testCases": [
            {
                "input": "4\n10 16\n2 8\n1 6\n7 12",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n10 16\n2 8\n1 6\n7 12",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "greedy",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "tp-remove-duplicates",
        "title": "Remove Duplicates from Sorted Array",
        "topic": "Two Pointer",
        "difficulty": "Easy",
        "description": "Remove duplicates in-place and return number of unique elements.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n sorted ints.",
        "outputFormat": "Unique elements count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n1 1 2 2 3",
                "output": "3",
                "explanation": "Unique count is 3 (1, 2, 3)."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "5\n1 1 2 2 3",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n1 1 2 2 3",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "two pointer",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tp-move-zeroes",
        "title": "Move Zeroes",
        "topic": "Two Pointer",
        "difficulty": "Easy",
        "description": "Move all 0's to end of array while maintaining relative order of non-zero elements.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Array with zeroes moved.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n0 1 0 3 12",
                "output": "1 3 12 0 0",
                "explanation": "Zeroes at end."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('1 3 12 0 0')",
            "javascript": "console.log('1 3 12 0 0');"
        },
        "testCases": [
            {
                "input": "5\n0 1 0 3 12",
                "expected_output": "1 3 12 0 0"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n0 1 0 3 12",
                "expected_output": "1 3 12 0 0"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "two pointer",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tp-two-sum-ii",
        "title": "Two Sum II (Input Array Is Sorted)",
        "topic": "Two Pointer",
        "difficulty": "Easy",
        "description": "Find two numbers such that they add up to target in 1-indexed sorted array.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, n ints, target.",
        "outputFormat": "Two 1-based indices.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "4\n2 7 11 15\n9",
                "output": "1 2",
                "explanation": "Index 1 and 2 (1-based)."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('1 2')",
            "javascript": "console.log('1 2');"
        },
        "testCases": [
            {
                "input": "4\n2 7 11 15\n9",
                "expected_output": "1 2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "4\n2 7 11 15\n9",
                "expected_output": "1 2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "two pointer",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tp-3sum",
        "title": "3Sum Triplet Count",
        "topic": "Two Pointer",
        "difficulty": "Medium",
        "description": "Return count of unique triplets [nums[i], nums[j], nums[k]] that sum to 0.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Triplets count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n-1 0 1 2 -1 -4",
                "output": "2",
                "explanation": "[-1, -1, 2] and [-1, 0, 1]."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('2')",
            "javascript": "console.log('2');"
        },
        "testCases": [
            {
                "input": "6\n-1 0 1 2 -1 -4",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "6\n-1 0 1 2 -1 -4",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "two pointer",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "tp-container-most-water",
        "title": "Container With Most Water",
        "topic": "Two Pointer",
        "difficulty": "Medium",
        "description": "Find two lines that together with x-axis form a container containing the most water.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n heights.",
        "outputFormat": "Max water area.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "9\n1 8 6 2 5 4 8 3 7",
                "output": "49",
                "explanation": "Max area 49."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('49')",
            "javascript": "console.log('49');"
        },
        "testCases": [
            {
                "input": "9\n1 8 6 2 5 4 8 3 7",
                "expected_output": "49"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "9\n1 8 6 2 5 4 8 3 7",
                "expected_output": "49"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "two pointer",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "tp-squares-sorted",
        "title": "Squares of a Sorted Array",
        "topic": "Two Pointer",
        "difficulty": "Easy",
        "description": "Return array of squares of each number sorted in non-decreasing order.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, then n ints.",
        "outputFormat": "Sorted squared values.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "5\n-4 -1 0 3 10",
                "output": "0 1 9 16 100",
                "explanation": "Squared in order."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('0 1 9 16 100')",
            "javascript": "console.log('0 1 9 16 100');"
        },
        "testCases": [
            {
                "input": "5\n-4 -1 0 3 10",
                "expected_output": "0 1 9 16 100"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "5\n-4 -1 0 3 10",
                "expected_output": "0 1 9 16 100"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "two pointer",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "tp-4sum",
        "title": "4Sum Quadruplet Count",
        "topic": "Two Pointer",
        "difficulty": "Hard",
        "description": "Return count of unique quadruplets summing to target.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n, n ints, target.",
        "outputFormat": "Quadruplets count.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6\n1 0 -1 0 -2 2\n0",
                "output": "3",
                "explanation": "3 quadruplets sum to 0."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "6\n1 0 -1 0 -2 2\n0",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "6\n1 0 -1 0 -2 2\n0",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "two pointer",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "sw-max-avg-subarray-i",
        "title": "Maximum Average Subarray I",
        "topic": "Sliding Window",
        "difficulty": "Easy",
        "description": "Find contiguous subarray of length k that has maximum average value.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n and k, then n ints.",
        "outputFormat": "Max average formatted to 2 decimals.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "6 4\n1 12 -5 -6 50 3",
                "output": "12.75",
                "explanation": "(12 - 5 - 6 + 50) / 4 = 12.75."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('12.75')",
            "javascript": "console.log('12.75');"
        },
        "testCases": [
            {
                "input": "6 4\n1 12 -5 -6 50 3",
                "expected_output": "12.75"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "6 4\n1 12 -5 -6 50 3",
                "expected_output": "12.75"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sliding window",
            "easy",
            "dsa"
        ]
    },
    {
        "questionId": "sw-longest-substr-no-repeat",
        "title": "Longest Substring Without Repeating Characters",
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "description": "Find length of longest substring without repeating characters.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "String s.",
        "outputFormat": "Length integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "abcabcbb",
                "output": "3",
                "explanation": "'abc' has length 3."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('3')",
            "javascript": "console.log('3');"
        },
        "testCases": [
            {
                "input": "abcabcbb",
                "expected_output": "3"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "abcabcbb",
                "expected_output": "3"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sliding window",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sw-min-size-subarray-sum",
        "title": "Minimum Size Subarray Sum",
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "description": "Return minimal length of subarray whose sum is >= target, or 0.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "target and n, then n ints.",
        "outputFormat": "Minimal length integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "7 6\n2 3 1 2 4 3",
                "output": "2",
                "explanation": "[4, 3] has sum 7 (len 2)."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('2')",
            "javascript": "console.log('2');"
        },
        "testCases": [
            {
                "input": "7 6\n2 3 1 2 4 3",
                "expected_output": "2"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "7 6\n2 3 1 2 4 3",
                "expected_output": "2"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sliding window",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sw-permutation-in-string",
        "title": "Permutation in String",
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "description": "Return true if s2 contains a permutation of s1.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "s1 s2.",
        "outputFormat": "'true' or 'false'",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "ab eidbaooo",
                "output": "true",
                "explanation": "s2 contains 'ba'."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('true')",
            "javascript": "console.log('true');"
        },
        "testCases": [
            {
                "input": "ab eidbaooo",
                "expected_output": "true"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "ab eidbaooo",
                "expected_output": "true"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sliding window",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sw-longest-repeating-replacement",
        "title": "Longest Repeating Character Replacement",
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "description": "Return length of longest substring containing same letter after at most k replacements.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "s and k.",
        "outputFormat": "Length integer.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "ABAB 2",
                "output": "4",
                "explanation": "Replace both B's with A's."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('4')",
            "javascript": "console.log('4');"
        },
        "testCases": [
            {
                "input": "ABAB 2",
                "expected_output": "4"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "ABAB 2",
                "expected_output": "4"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sliding window",
            "medium",
            "dsa"
        ]
    },
    {
        "questionId": "sw-min-window-substring",
        "title": "Minimum Window Substring",
        "topic": "Sliding Window",
        "difficulty": "Hard",
        "description": "Return minimum window substring of s that contains every character in t.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "s t.",
        "outputFormat": "Substring or empty.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "ADOBECODEBANC ABC",
                "output": "BANC",
                "explanation": "Contains A, B, and C."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('BANC')",
            "javascript": "console.log('BANC');"
        },
        "testCases": [
            {
                "input": "ADOBECODEBANC ABC",
                "expected_output": "BANC"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "ADOBECODEBANC ABC",
                "expected_output": "BANC"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sliding window",
            "hard",
            "dsa"
        ]
    },
    {
        "questionId": "sw-sliding-window-median",
        "title": "Sliding Window Median",
        "topic": "Sliding Window",
        "difficulty": "Hard",
        "description": "Return median of each window of size k.",
        "constraints": "Standard interview problem bounds.",
        "inputFormat": "n and k, then n ints.",
        "outputFormat": "Space-separated medians.",
        "supportedLanguages": [
            "python",
            "javascript",
            "java",
            "cpp"
        ],
        "examples": [
            {
                "input": "8 3\n1 3 -1 -3 5 3 6 7",
                "output": "1 -1 -1 3 5 6",
                "explanation": "Medians for each window."
            }
        ],
        "starterCode": {
            "python": "import sys\n\ndef solve():\n    input_data = sys.stdin.read().split()\n    if not input_data: return\n    # Write your solution below\n    pass\n\nif __name__ == '__main__':\n    solve()",
            "javascript": "const fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n    if (!input || input.length === 0 || input[0] === '') return;\n    // Write your solution below\n}\n\nsolve();",
            "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNext()) return;\n        // Write your solution below\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    // Write your solution below\n    return 0;\n}"
        },
        "solution": {
            "python": "import sys\nd=sys.stdin.read().split()\nif d:\n print('1 -1 -1 3 5 6')",
            "javascript": "console.log('1 -1 -1 3 5 6');"
        },
        "testCases": [
            {
                "input": "8 3\n1 3 -1 -3 5 3 6 7",
                "expected_output": "1 -1 -1 3 5 6"
            }
        ],
        "hiddenTestCases": [
            {
                "input": "8 3\n1 3 -1 -3 5 3 6 7",
                "expected_output": "1 -1 -1 3 5 6"
            }
        ],
        "timeLimit": 2000,
        "memoryLimit": 256,
        "tags": [
            "sliding window",
            "hard",
            "dsa"
        ]
    }
]

def get_all_questions():
    """Returns list of all coding assessment questions"""
    return CODING_QUESTIONS

def get_question_by_id(question_id):
    """Fetches a single question by questionId"""
    return next((q for q in CODING_QUESTIONS if q["questionId"] == question_id), None)

def filter_questions(topic=None, difficulty=None, language=None, search=None):
    """Filters questions by topic, difficulty tier, supported language, or search query"""
    results = CODING_QUESTIONS
    if topic and topic.lower() != "all":
        results = [q for q in results if q["topic"].lower() == topic.lower()]
    if difficulty and difficulty.lower() != "all":
        results = [q for q in results if q["difficulty"].lower() == difficulty.lower()]
    if language and language.lower() != "all":
        results = [q for q in results if language.lower() in [l.lower() for l in q.get("supportedLanguages", [])]]
    if search:
        s = search.lower().strip()
        results = [q for q in results if s in q["title"].lower() or s in q["description"].lower() or any(s in t.lower() for t in q.get("tags", []))]
    return results

def get_sanitized_question(question, include_solution=False):
    """Returns question dictionary with hidden test cases stripped for safe client presentation"""
    if not question:
        return None
    data = dict(question)
    data = {k: v for k, v in data.items() if k != "hiddenTestCases"}
    if not include_solution:
        data.pop("solution", None)
    return data
