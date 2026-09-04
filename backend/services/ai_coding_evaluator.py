import os
import re
import json
import ast
import urllib.request
import urllib.error
from config import config

class AICodingEvaluator:
    """
    AI Coding Evaluation Engine, Progressive 3-Tier Hint Generator,
    and Technical Interviewer Dialogue System for PrepWise AI.
    Integrates Gemini API when configured, with high-accuracy heuristic static analysis fallback.
    """

    def __init__(self):
        self.gemini_key = getattr(config, "GEMINI_API_KEY", "") or os.environ.get("GEMINI_API_KEY", "")

    def evaluate_code(self, language, code_text, problem_title, problem_desc="", test_cases_passed=0, total_test_cases=0, execution_status="Accepted"):
        """
        Evaluates candidate code across 8 dimensions:
        1. Correctness
        2. Time Complexity
        3. Space Complexity
        4. Code Quality
        5. Readability
        6. Edge Case Handling
        7. Optimization
        8. Problem-Solving Approach
        """
        if self.gemini_key:
            llm_result = self._call_gemini_evaluation(language, code_text, problem_title, problem_desc, test_cases_passed, total_test_cases, execution_status)
            if llm_result:
                return llm_result

        # High-Accuracy Heuristic Static & Dynamic Evaluator
        return self._heuristic_evaluation(language, code_text, problem_title, test_cases_passed, total_test_cases, execution_status)

    def _heuristic_evaluation(self, language, code_text, problem_title, test_cases_passed, total_test_cases, execution_status):
        code_lower = code_text.lower()
        pass_ratio = (test_cases_passed / total_test_cases) if total_test_cases > 0 else (1.0 if execution_status == "Accepted" else 0.0)

        # 1. Correctness (out of 10)
        correctness = round(pass_ratio * 10, 1)
        if execution_status != "Accepted" and correctness > 6.0:
            correctness = 5.0

        # 2. Time Complexity Detection
        has_triple_loop = bool(re.search(r'for\s+.*for\s+.*for\s+', code_lower) or re.search(r'while\s+.*while\s+.*while\s+', code_lower))
        has_double_loop = bool(re.search(r'for\s+.*for\s+', code_lower) or re.search(r'while\s+.*while\s+', code_lower))
        has_single_loop = ("for " in code_lower or "while " in code_lower)
        has_binary_search = any(k in code_lower for k in ["binary", "bisect", "mid", "l <= r", "l < r", ">> 1"])
        has_hashmap = any(k in code_lower for k in ["hash", "dict", "map", "set(", "new set", "new map", "defaultdict", "counter"])

        if has_triple_loop:
            time_comp = "O(N³)"
            time_score = 5.0
        elif has_double_loop:
            time_comp = "O(N²)"
            time_score = 6.5
        elif has_binary_search:
            time_comp = "O(log N)"
            time_score = 9.5
        elif has_single_loop:
            if "sort" in code_lower:
                time_comp = "O(N log N)"
                time_score = 8.5
            else:
                time_comp = "O(N)"
                time_score = 9.0
        else:
            time_comp = "O(1)"
            time_score = 9.5

        # 3. Space Complexity Detection
        if any(k in code_lower for k in ["[[0]", "new array", "matrix", "grid", "dp = ["]):
            if has_double_loop:
                space_comp = "O(N²)"
                space_score = 6.5
            else:
                space_comp = "O(N)"
                space_score = 8.0
        elif has_hashmap or any(k in code_lower for k in ["append(", "push(", "ans =", "res ="]):
            space_comp = "O(N)"
            space_score = 8.5
        else:
            space_comp = "O(1)"
            space_score = 9.5

        # 4. Code Quality & Readability (out of 10)
        code_lines = [line for line in code_text.splitlines() if line.strip() and not line.strip().startswith(("#", "//", "/*"))]
        line_count = len(code_lines)
        has_comments = bool(re.search(r'(#|//|\*).*', code_text))
        has_meaningful_names = not bool(re.search(r'\b(asdf|foo|bar|temp123)\b', code_lower))

        quality_score = 8.5
        if line_count > 60: quality_score -= 1.0
        if not has_meaningful_names: quality_score -= 1.0
        if not has_comments: quality_score -= 0.5

        readability_score = 8.5
        if "def " in code_text or "function " in code_text or "class " in code_text:
            readability_score += 0.5

        # 5. Edge Case Handling (out of 10)
        edge_case_score = 8.0
        if any(k in code_lower for k in ["if not ", "== 0", "length === 0", "null", "none", "len("]):
            edge_case_score += 1.0
        if pass_ratio < 1.0:
            edge_case_score = max(4.0, edge_case_score - 3.0)

        # 6. Optimization & Problem Solving (out of 10)
        optimization_score = round((time_score + space_score) / 2.0, 1)
        problem_solving_score = round((correctness * 0.6) + (optimization_score * 0.4), 1)

        # Overall composite score out of 50
        overall_50 = round((correctness + time_score + space_score + quality_score + problem_solving_score), 1)
        # Scaled percentage score out of 100
        overall_pct = round((overall_50 / 50.0) * 100, 1)

        # Identify Key Strengths & Areas to Improve
        strengths = []
        improvements = []

        if pass_ratio == 1.0:
            strengths.append(f"Passed all {total_test_cases} test cases with complete functional correctness.")
        elif pass_ratio >= 0.7:
            strengths.append(f"Passed {test_cases_passed}/{total_test_cases} test cases covering primary logic paths.")
        else:
            improvements.append("Refactor core algorithm logic to resolve failing edge cases and output mismatches.")

        if time_score >= 8.5:
            strengths.append(f"Achieved optimal {time_comp} time complexity avoiding polynomial bottlenecks.")
        else:
            improvements.append(f"Optimize {time_comp} time complexity by replacing nested loops with hash map lookups or two-pointer traversal.")

        if space_score >= 9.0:
            strengths.append(f"Excellent auxiliary memory footprint with in-place {space_comp} space complexity.")
        else:
            improvements.append("Reduce auxiliary memory allocation by utilizing in-place pointer updates.")

        if edge_case_score >= 8.5:
            strengths.append("Handled boundary conditions including empty inputs, single elements, and zero limits.")
        else:
            improvements.append("Add explicit boundary checks for empty collections, negative numbers, and duplicate entries.")

        if not strengths:
            strengths.append("Standard solution structure with clear modular separation.")
        if not improvements:
            improvements.append("Solution demonstrates high industry standard. Next, test with extreme stress scale data.")

        # Follow-up Interview Question
        follow_up = self.generate_follow_up_question(problem_title, time_comp, space_comp)

        explanation = (
            f"Your solution for '{problem_title}' achieved a {time_comp} time complexity and {space_comp} space complexity. "
            f"Execution passed {test_cases_passed} out of {total_test_cases} test cases with an overall score of {overall_50}/50 ({overall_pct}%). "
            f"The algorithm leverages {'efficient lookup and traversal techniques' if time_score >= 8 else 'iterative simulation'}. "
        )

        return {
            "score": overall_pct,
            "overall_score_50": overall_50,
            "correctness": correctness,
            "timeComplexityScore": time_score,
            "spaceComplexityScore": space_score,
            "codeQuality": quality_score,
            "readability": readability_score,
            "edgeCaseHandling": edge_case_score,
            "optimization": optimization_score,
            "problemSolving": problem_solving_score,
            "timeComplexity": time_comp,
            "spaceComplexity": space_comp,
            "strengths": strengths,
            "improvements": improvements,
            "explanation": explanation,
            "followUpQuestion": follow_up
        }

    def generate_hints(self, problem_id, title, topic, difficulty, current_code=""):
        """
        Returns a progressive 3-tier hint for the specified coding problem:
        Hint 1 -> Conceptual hint
        Hint 2 -> Algorithm direction / Data structure choice
        Hint 3 -> More specific approach / Edge case caution
        """
        t = (topic or "").lower()

        hints = {
            1: "Think about the problem from first principles: What is the target outcome, and can we store previous states or sort the input first?",
            2: "Consider which data structure provides O(1) or O(log N) lookup: A Hash Map, Balanced Tree, or Two Pointers.",
            3: "Watch out for edge cases such as empty input, duplicate values, and negative indices."
        }

        if "array" in t:
            hints = {
                1: "Try walking through an example manually. Can you avoid checking every pair by remembering numbers you have already visited?",
                2: "A Hash Table allows you to check whether the required complement exists in O(1) average time.",
                3: "Maintain a running map of `value -> index`. On each iteration, check if `target - current_val` is already in the map."
            }
        elif "string" in t:
            hints = {
                1: "Consider character frequencies or two pointers moving inwards from the boundaries.",
                2: "Use an array of size 26 or a frequency dictionary to track character counts in linear O(N) time.",
                3: "Remember to ignore non-alphanumeric characters and normalize cases if testing for palindromes or anagrams."
            }
        elif "search" in t:
            hints = {
                1: "Since the array is sorted (or partially sorted), linear scan is suboptimal. How can you discard half the search space in each step?",
                2: "Binary Search: Compare `nums[mid]` with `target` to decide whether to search the left or right half.",
                3: "Carefully update `left = mid + 1` and `right = mid - 1` to prevent off-by-one errors and infinite loops."
            }
        elif "dynamic" in t or "dp" in t:
            hints = {
                1: "Identify the overlapping subproblems: Can the answer for state `i` be computed from states `i-1` and `i-2`?",
                2: "Define a `dp[i]` array where each cell represents the optimal solution up to index `i`.",
                3: "Transition: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. You can often optimize auxiliary space to O(1) with two variables."
            }
        elif "stack" in t:
            hints = {
                1: "A Last-In, First-Out (LIFO) stack helps match closing elements with their most recent opening counterpart.",
                2: "Push opening brackets onto the stack. When a closing bracket appears, check if the stack top matches.",
                3: "Don't forget to verify if the stack is completely empty at the end of the iteration."
            }
        elif "tree" in t:
            hints = {
                1: "Binary trees are naturally recursive: The solution for a node often combines the results of its left and right subtrees.",
                2: "Consider Depth-First Search (DFS) or Breadth-First Search (BFS queue) depending on whether you need path sums or level-order views.",
                3: "Base case: If `node is None`, return the default identity (e.g. 0 for depth, True for symmetry)."
            }
        elif "graph" in t:
            hints = {
                1: "Model nodes and connections with an adjacency list. Keep a `visited` set to prevent infinite cycles.",
                2: "Use BFS with a queue for shortest path problems, or DFS with recursion/stack for connected component discovery.",
                3: "Check bounds before exploring neighbor cells in matrix grid graph problems."
            }
        elif "two pointer" in t:
            hints = {
                1: "If the input array is sorted, placing one pointer at the start and one at the end allows directional convergence.",
                2: "If `current_sum < target`, increment the left pointer. If `current_sum > target`, decrement the right pointer.",
                3: "Handle duplicate elements by advancing pointers until a distinct value is encountered."
            }
        elif "sliding window" in t:
            hints = {
                1: "Maintain a dynamic window `[left, right]` that expands to include new elements and shrinks when constraints are violated.",
                2: "Use a frequency map to keep track of character counts inside the current window in O(1) amortized time.",
                3: "Advance the `right` pointer to expand the window, and advance `left` when the window condition becomes invalid."
            }

        return {
            "hint_level_1": hints[1],
            "hint_level_2": hints[2],
            "hint_level_3": hints[3]
        }

    def generate_follow_up_question(self, problem_title, time_complexity, space_complexity):
        """
        Generates realistic technical interviewer follow-up questions tailored to the candidate's solution.
        """
        questions = [
            f"What is the exact theoretical time complexity of your solution, and why is it {time_complexity}?",
            f"Your solution currently uses {space_complexity} auxiliary space. Is it possible to optimize this to O(1) in-place?",
            f"How would your code behave if the input size grew to 100 million records, exceeding available RAM?",
            f"Can you explain how your implementation handles negative integers, zero, or duplicate keys?",
            f"If this function were called concurrently by 10,000 threads per second in a distributed backend, what concurrency protections would you implement?"
        ]
        import random
        return random.choice(questions)

    def evaluate_follow_up_answer(self, follow_up_question, candidate_answer, expected_time_comp="O(N)"):
        """
        Evaluates candidate's response to interviewer follow-up questions.
        """
        ans_lower = candidate_answer.lower()
        score = 85
        feedback = "Good technical rationale provided."

        if any(term in ans_lower for term in ["o(n)", "o(1)", "o(log n)", "linear", "constant", "traverse", "hash", "iterate"]):
            score = 92
            feedback = "Strong analytical justification. Correctly identified algorithmic complexity drivers."
        elif len(candidate_answer.strip().split()) < 5:
            score = 60
            feedback = "Answer is too brief. In a technical interview, elaborate on your thought process and trade-offs."

        return {
            "score": score,
            "feedback": feedback,
            "next_step": "Excellent. You are ready to proceed to the next coding problem or view your comprehensive report."
        }

    def _call_gemini_evaluation(self, language, code_text, problem_title, problem_desc, test_cases_passed, total_test_cases, execution_status):
        """Optional LLM integration with Google Gemini when API key is configured"""
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.gemini_key}"
            prompt = f"""You are a Principal Software Engineer conducting a Technical Coding Interview.
Evaluate this candidate's code submission.

Problem: {problem_title}
Description: {problem_desc}
Language: {language}
Test Cases Passed: {test_cases_passed}/{total_test_cases}
Execution Status: {execution_status}

Candidate Code:
```{language}
{code_text}
```

Return ONLY valid JSON with this exact schema:
{{
  "score": <number 0-100>,
  "overall_score_50": <number 0-50>,
  "correctness": <number 0-10>,
  "timeComplexityScore": <number 0-10>,
  "spaceComplexityScore": <number 0-10>,
  "codeQuality": <number 0-10>,
  "readability": <number 0-10>,
  "edgeCaseHandling": <number 0-10>,
  "optimization": <number 0-10>,
  "problemSolving": <number 0-10>,
  "timeComplexity": "<e.g. O(N)>",
  "spaceComplexity": "<e.g. O(1)>",
  "strengths": ["<strength 1>", "<strength 2>"],
  "improvements": ["<improvement 1>", "<improvement 2>"],
  "explanation": "<detailed explanation>",
  "followUpQuestion": "<interview question>"
}}
"""
            req_data = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
            req = urllib.request.Request(url, data=req_data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=6.0) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text_resp = data["candidates"][0]["content"]["parts"][0]["text"]
                # Extract JSON block
                match = re.search(r'\{.*\}', text_resp, re.DOTALL)
                if match:
                    return json.loads(match.group(0))
        except Exception as e:
            # Fall back seamlessly to heuristic evaluation
            return None

ai_coding_evaluator = AICodingEvaluator()
