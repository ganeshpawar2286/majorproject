"""
PrepWise AI – Curated Aptitude & Reasoning Question Bank
Contains categorized questions across 4 Core Modules:
1. Quantitative Aptitude (Percentages, Profit/Loss, Time & Work, Speed & Distance, Probability, Ratio, Algebra, etc.)
2. Logical Reasoning (Series, Syllogisms, Blood Relations, Coding-Decoding, Seating, Analogy, etc.)
3. Verbal Ability (Sentence Correction, Synonyms/Antonyms, Comprehension, Idioms, One-Word Substitutions, etc.)
4. Technical Aptitude (OS, DBMS, OOP, Computer Networks, Data Structures, Software Engineering, etc.)

Expanded with 212+ verified questions supporting dynamic 45-50 question practice sessions and timed assessments.
"""

import random

APTITUDE_QUESTIONS = [
    {
        "id": "quant-time-work-1",
        "category": "Quantitative",
        "topic": "Time & Work",
        "difficulty": "Easy",
        "question": "A can complete a piece of work in 12 days, and B can complete the same work in 24 days. If they work together, in how many days will the work be completed?",
        "options": [
            "6 days",
            "8 days",
            "9 days",
            "10 days"
        ],
        "correct_answer": 1,
        "formula": "Combined 1-day work = (1/A) + (1/B). Total days = (A * B) / (A + B)",
        "explanation": "A's 1-day work = 1/12.\nB's 1-day work = 1/24.\n(A + B)'s 1-day work = (1/12) + (1/24) = 3/24 = 1/8.\nTherefore, working together, they finish the work in 8 days."
    },
    {
        "id": "quant-time-work-2",
        "category": "Quantitative",
        "topic": "Time & Work",
        "difficulty": "Medium",
        "question": "Pipe A can fill a tank in 20 minutes and Pipe B can empty it in 30 minutes. If both pipes are opened simultaneously, how long will it take to fill the tank?",
        "options": [
            "40 minutes",
            "50 minutes",
            "60 minutes",
            "75 minutes"
        ],
        "correct_answer": 2,
        "formula": "Net rate = (1/A) - (1/B)",
        "explanation": "Rate of Pipe A = +1/20 per min.\nRate of Pipe B = -1/30 per min.\nNet rate = (1/20) - (1/30) = (3 - 2)/60 = 1/60.\nTank fills completely in 60 minutes."
    },
    {
        "id": "quant-time-work-3",
        "category": "Quantitative",
        "topic": "Time & Work",
        "difficulty": "Medium",
        "question": "A is twice as good a workman as B and together they finish a piece of work in 18 days. In how many days can A alone finish the work?",
        "options": [
            "24 days",
            "27 days",
            "30 days",
            "36 days"
        ],
        "correct_answer": 1,
        "formula": "Ratio of work rates A:B = 2:1. (A + B) rate = 3 units/day.",
        "explanation": "Ratio of rates = 2:1. Combined rate = 3 units/day.\nTotal work = 18 days * 3 units/day = 54 units.\nA's time alone = 54 / 2 = 27 days."
    },
    {
        "id": "quant-time-work-4",
        "category": "Quantitative",
        "topic": "Time & Work",
        "difficulty": "Hard",
        "question": "12 men or 18 women can do a work in 14 days. In how many days can 8 men and 16 women do the same work?",
        "options": [
            "8 days",
            "9 days",
            "10 days",
            "12 days"
        ],
        "correct_answer": 1,
        "formula": "12 Men = 18 Women => 1 Man = 1.5 Women.",
        "explanation": "12M = 18W => 1M = 1.5W.\n8M + 16W = (8 * 1.5)W + 16W = 12W + 16W = 28W.\nIf 18 women take 14 days: Total work = 18 * 14 = 252 women-days.\nDays for 28 women = 252 / 28 = 9 days."
    },
    {
        "id": "quant-time-work-5",
        "category": "Quantitative",
        "topic": "Time & Work",
        "difficulty": "Easy",
        "question": "A can do a work in 15 days and B in 20 days. If they work on it together for 4 days, what fraction of the work is left?",
        "options": [
            "7/15",
            "8/15",
            "1/4",
            "1/10"
        ],
        "correct_answer": 1,
        "formula": "Fraction left = 1 - 4 * (1/A + 1/B)",
        "explanation": "A's 1-day work = 1/15, B's 1-day work = 1/20.\nTogether in 1 day = (1/15) + (1/20) = 7/60.\nIn 4 days = 4 * (7/60) = 7/15.\nWork remaining = 1 - 7/15 = 8/15."
    },
    {
        "id": "quant-speed-dist-1",
        "category": "Quantitative",
        "topic": "Speed & Distance",
        "difficulty": "Easy",
        "question": "A train running at a speed of 72 km/h crosses a 200-meter-long platform in 22 seconds. What is the length of the train?",
        "options": [
            "220 meters",
            "240 meters",
            "260 meters",
            "280 meters"
        ],
        "correct_answer": 1,
        "formula": "Speed in m/s = Speed in km/h * (5/18). Total Distance = Length of Train + Length of Platform = Speed * Time",
        "explanation": "Speed = 72 * (5/18) = 20 m/s.\nTotal distance = 20 * 22 = 440 meters.\nLength of train = 440 - 200 = 240 meters."
    },
    {
        "id": "quant-speed-dist-2",
        "category": "Quantitative",
        "topic": "Speed & Distance",
        "difficulty": "Medium",
        "question": "A person travels from town X to town Y at an average speed of 40 km/h and returns at 60 km/h. What is the average speed for the entire journey?",
        "options": [
            "48 km/h",
            "50 km/h",
            "52 km/h",
            "54 km/h"
        ],
        "correct_answer": 0,
        "formula": "Average Speed for equal distances = (2 * S1 * S2) / (S1 + S2)",
        "explanation": "Average Speed = (2 * 40 * 60) / (40 + 60) = 4800 / 100 = 48 km/h."
    },
    {
        "id": "quant-speed-dist-3",
        "category": "Quantitative",
        "topic": "Speed & Distance",
        "difficulty": "Medium",
        "question": "Two trains 140 m and 160 m long are running towards each other on parallel tracks at 40 km/h and 50 km/h respectively. In how many seconds will they clear each other?",
        "options": [
            "10 seconds",
            "12 seconds",
            "14 seconds",
            "16 seconds"
        ],
        "correct_answer": 1,
        "formula": "Relative speed = S1 + S2. Total distance = L1 + L2.",
        "explanation": "Relative speed = 40 + 50 = 90 km/h = 90 * (5/18) = 25 m/s.\nTotal distance = 140 + 160 = 300 m.\nTime = 300 / 25 = 12 seconds."
    },
    {
        "id": "quant-speed-dist-4",
        "category": "Quantitative",
        "topic": "Speed & Distance",
        "difficulty": "Hard",
        "question": "A boat travels 24 km upstream and 28 km downstream in 6 hours. It also travels 30 km upstream and 21 km downstream in 6.5 hours. What is the speed of the stream?",
        "options": [
            "2 km/h",
            "3 km/h",
            "4 km/h",
            "5 km/h"
        ],
        "correct_answer": 2,
        "formula": "Downstream speed = u + v, Upstream speed = u - v.",
        "explanation": "Upstream speed = 6 km/h, downstream speed = 14 km/h.\nSpeed of stream = (14 - 6)/2 = 4 km/h."
    },
    {
        "id": "quant-speed-dist-5",
        "category": "Quantitative",
        "topic": "Speed & Distance",
        "difficulty": "Easy",
        "question": "Walking at 3/4 of his usual speed, a man reaches his office 20 minutes late. What is his usual time to reach office?",
        "options": [
            "40 minutes",
            "50 minutes",
            "60 minutes",
            "80 minutes"
        ],
        "correct_answer": 2,
        "formula": "Time is inversely proportional to speed: T_new = (4/3) * T_usual.",
        "explanation": "New time = (4/3)T.\nDelay = (4/3)T - T = T/3 = 20 minutes.\nT = 20 * 3 = 60 minutes."
    },
    {
        "id": "quant-percent-1",
        "category": "Quantitative",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "If the price of petrol increases by 25%, by what percentage must a driver reduce petrol consumption to keep the expenditure unchanged?",
        "options": [
            "15%",
            "20%",
            "25%",
            "30%"
        ],
        "correct_answer": 1,
        "formula": "Reduction % = [R / (100 + R)] * 100",
        "explanation": "Reduction % = [25 / (100 + 25)] * 100 = (25 / 125) * 100 = 20%."
    },
    {
        "id": "quant-percent-2",
        "category": "Quantitative",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "In an election between two candidates, the winner received 65% of the total votes and won by a majority of 1,500 votes. What was the total number of votes polled?",
        "options": [
            "4,000",
            "5,000",
            "6,000",
            "7,500"
        ],
        "correct_answer": 1,
        "formula": "Difference in vote % = 65% - 35% = 30%. Total votes = (1500 / 30) * 100.",
        "explanation": "Winner = 65%, Loser = 35%.\nDifference = 30% of total votes = 1500.\nTotal votes = (1500 * 100) / 30 = 5000."
    },
    {
        "id": "quant-percent-3",
        "category": "Quantitative",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "The population of a town increases by 10% annually. If the current population is 121,000, what was it 2 years ago?",
        "options": [
            "95,000",
            "100,000",
            "105,000",
            "110,000"
        ],
        "correct_answer": 1,
        "formula": "P_now = P_orig * (1 + R/100)^T",
        "explanation": "121,000 = P * (1.1)\u00b2 = P * 1.21.\nP = 121,000 / 1.21 = 100,000."
    },
    {
        "id": "quant-percent-4",
        "category": "Quantitative",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "A candidate must get 33% marks to pass. He gets 220 marks and fails by 11 marks. What are the maximum marks?",
        "options": [
            "600",
            "700",
            "750",
            "800"
        ],
        "correct_answer": 1,
        "formula": "Passing marks = Scored marks + Deficit marks = Pass % of Max",
        "explanation": "Passing marks = 220 + 11 = 231.\n33% of Max = 231 => Max marks = (231 / 33) * 100 = 7 * 100 = 700."
    },
    {
        "id": "quant-profit-loss-1",
        "category": "Quantitative",
        "topic": "Profit & Loss",
        "difficulty": "Easy",
        "question": "An article is sold for $840 at a gain of 20%. What was the cost price of the article?",
        "options": [
            "$680",
            "$700",
            "$720",
            "$750"
        ],
        "correct_answer": 1,
        "formula": "Cost Price = (Selling Price * 100) / (100 + Gain %)",
        "explanation": "CP = (840 * 100) / (100 + 20) = 84000 / 120 = $700."
    },
    {
        "id": "quant-profit-loss-2",
        "category": "Quantitative",
        "topic": "Profit & Loss",
        "difficulty": "Medium",
        "question": "A shopkeeper marks his goods 30% above the cost price and gives a discount of 10% on the marked price. What is his net gain percentage?",
        "options": [
            "15%",
            "17%",
            "20%",
            "22%"
        ],
        "correct_answer": 1,
        "formula": "Net Change = a + b + (ab / 100)",
        "explanation": "Let CP = 100.\nMarked Price = 130. Discount = 10% of 130 = 13.\nSP = 130 - 13 = 117. Net Gain = 17%."
    },
    {
        "id": "quant-profit-loss-3",
        "category": "Quantitative",
        "topic": "Profit & Loss",
        "difficulty": "Medium",
        "question": "By selling 33 meters of cloth, a merchant gains the selling price of 11 meters. Find the gain percentage.",
        "options": [
            "25%",
            "33.33%",
            "50%",
            "66.66%"
        ],
        "correct_answer": 2,
        "formula": "Gain = SP - CP. 11 SP = 33 SP - 33 CP => 33 CP = 22 SP.",
        "explanation": "33 CP = 22 SP => SP/CP = 33/22 = 3/2.\nGain % = [(3 - 2) / 2] * 100 = 50%."
    },
    {
        "id": "quant-profit-loss-4",
        "category": "Quantitative",
        "topic": "Profit & Loss",
        "difficulty": "Hard",
        "question": "A dealer sells two bicycles for $1,200 each. On one he gains 20% and on the other he loses 20%. What is his overall gain or loss percentage?",
        "options": [
            "No profit no loss",
            "2% gain",
            "4% loss",
            "5% loss"
        ],
        "correct_answer": 2,
        "formula": "When SP is identical for equal gain % and loss % x: Loss % = (x / 10)\u00b2",
        "explanation": "Always a net loss when SP is same. Loss % = (20 / 10)\u00b2 = 4% loss."
    },
    {
        "id": "quant-ratio-1",
        "category": "Quantitative",
        "topic": "Ratio & Proportion",
        "difficulty": "Easy",
        "question": "Two numbers are in the ratio 3 : 5. If 9 is subtracted from each, the new ratio becomes 12 : 23. What is the smaller number?",
        "options": [
            "27",
            "33",
            "45",
            "55"
        ],
        "correct_answer": 1,
        "formula": "(3x - 9) / (5x - 9) = 12 / 23",
        "explanation": "23*(3x - 9) = 12*(5x - 9) => 69x - 207 = 60x - 108 => 9x = 99 => x = 11.\nSmaller number = 3 * 11 = 33."
    },
    {
        "id": "quant-ratio-2",
        "category": "Quantitative",
        "topic": "Ratio & Proportion",
        "difficulty": "Medium",
        "question": "In a mixture of 60 liters, the ratio of milk and water is 2 : 1. How much water must be added to make the ratio 1 : 2?",
        "options": [
            "40 liters",
            "50 liters",
            "60 liters",
            "75 liters"
        ],
        "correct_answer": 2,
        "formula": "Milk remains constant while water is added.",
        "explanation": "Milk = (2/3)*60 = 40 L. Water = (1/3)*60 = 20 L.\nWe want Milk : Water = 1 : 2.\n40 / (20 + W) = 1/2 => 20 + W = 80 => W = 60 liters."
    },
    {
        "id": "quant-ratio-3",
        "category": "Quantitative",
        "topic": "Ratio & Proportion",
        "difficulty": "Easy",
        "question": "If A : B = 2 : 3, B : C = 4 : 5, and C : D = 6 : 7, find the ratio A : D.",
        "options": [
            "16 : 35",
            "12 : 25",
            "8 : 15",
            "14 : 33"
        ],
        "correct_answer": 0,
        "formula": "(A/D) = (A/B) * (B/C) * (C/D)",
        "explanation": "A/D = (2/3) * (4/5) * (6/7) = (2 * 4 * 2) / (1 * 5 * 7) = 16 / 35."
    },
    {
        "id": "quant-probability-1",
        "category": "Quantitative",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Two unbiased dice are rolled together. What is the probability of getting a sum of numbers equal to 8?",
        "options": [
            "5/36",
            "1/6",
            "7/36",
            "1/9"
        ],
        "correct_answer": 0,
        "formula": "P(E) = Favorable Outcomes / Total Outcomes (36)",
        "explanation": "Total possible outcomes = 36.\nPairs giving sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) -> 5 outcomes.\nProbability = 5/36."
    },
    {
        "id": "quant-probability-2",
        "category": "Quantitative",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "A card is drawn from a well-shuffled pack of 52 playing cards. What is the probability that the card drawn is either a King or a Spade?",
        "options": [
            "4/13",
            "16/52",
            "17/52",
            "1/4"
        ],
        "correct_answer": 1,
        "formula": "P(A \u222a B) = P(A) + P(B) - P(A \u2229 B)",
        "explanation": "Kings = 4, Spades = 13, King of Spades = 1.\nTotal favorable = 4 + 13 - 1 = 16.\nProbability = 16/52 = 4/13."
    },
    {
        "id": "quant-probability-3",
        "category": "Quantitative",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "A bag contains 5 red and 7 green balls. Two balls are drawn at random without replacement. What is the probability that both are green?",
        "options": [
            "7/22",
            "14/33",
            "21/66",
            "7/12"
        ],
        "correct_answer": 0,
        "formula": "P = (7/12) * (6/11)",
        "explanation": "P(first green) = 7/12.\nP(second green) = 6/11.\nP(both green) = (7/12) * (6/11) = 42/132 = 7/22."
    },
    {
        "id": "quant-probability-4",
        "category": "Quantitative",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "Three coins are tossed simultaneously. What is the probability of getting at least two heads?",
        "options": [
            "1/4",
            "3/8",
            "1/2",
            "5/8"
        ],
        "correct_answer": 2,
        "formula": "Total outcomes = 2\u00b3 = 8. Favorable outcomes (HHH, HHT, HTH, THH) = 4.",
        "explanation": "Total = 8.\nAt least 2 heads = {HHH, HHT, HTH, THH} = 4.\nProbability = 4/8 = 1/2."
    },
    {
        "id": "quant-permutation-1",
        "category": "Quantitative",
        "topic": "Permutation & Combination",
        "difficulty": "Medium",
        "question": "In how many different ways can the letters of the word 'LEADER' be arranged?",
        "options": [
            "180",
            "360",
            "720",
            "1440"
        ],
        "correct_answer": 1,
        "formula": "N! / (p1! * p2!) where identical letters are divided",
        "explanation": "The word 'LEADER' contains 6 letters with 'E' appearing twice.\nTotal arrangements = 6! / 2! = 720 / 2 = 360."
    },
    {
        "id": "quant-permutation-2",
        "category": "Quantitative",
        "topic": "Permutation & Combination",
        "difficulty": "Medium",
        "question": "In how many ways can a group of 5 men and 3 women be formed from 8 men and 6 women?",
        "options": [
            "560",
            "1120",
            "1680",
            "2240"
        ],
        "correct_answer": 1,
        "formula": "C(8, 5) * C(6, 3)",
        "explanation": "C(8, 5) = C(8, 3) = (8*7*6)/(3*2*1) = 56.\nC(6, 3) = (6*5*4)/(3*2*1) = 20.\nTotal ways = 56 * 20 = 1120."
    },
    {
        "id": "quant-permutation-3",
        "category": "Quantitative",
        "topic": "Permutation & Combination",
        "difficulty": "Easy",
        "question": "How many 3-digit numbers can be formed from the digits 2, 3, 5, 6, 7, and 9 without repetition?",
        "options": [
            "100",
            "120",
            "150",
            "216"
        ],
        "correct_answer": 1,
        "formula": "P(n, r) = n! / (n - r)!",
        "explanation": "6 available digits. For 3 digits: 6 * 5 * 4 = 120 numbers."
    },
    {
        "id": "quant-interest-1",
        "category": "Quantitative",
        "topic": "Simple & Compound Interest",
        "difficulty": "Easy",
        "question": "A sum of money doubles itself in 5 years at simple interest. What is the annual rate of interest?",
        "options": [
            "15%",
            "20%",
            "25%",
            "10%"
        ],
        "correct_answer": 1,
        "formula": "SI = P. R = (SI * 100) / (P * T)",
        "explanation": "If Principal = P, Amount = 2P, so SI = P.\nRate = (P * 100) / (P * 5) = 100 / 5 = 20% per annum."
    },
    {
        "id": "quant-interest-2",
        "category": "Quantitative",
        "topic": "Simple & Compound Interest",
        "difficulty": "Medium",
        "question": "What will be the compound interest on $10,000 at 10% per annum for 2 years compounded annually?",
        "options": [
            "$2,000",
            "$2,100",
            "$2,200",
            "$2,500"
        ],
        "correct_answer": 1,
        "formula": "CI = P * [(1 + R/100)^T - 1]",
        "explanation": "Amount = 10,000 * (1.10)\u00b2 = 10,000 * 1.21 = $12,100.\nCI = 12,100 - 10,000 = $2,100."
    },
    {
        "id": "quant-interest-3",
        "category": "Quantitative",
        "topic": "Simple & Compound Interest",
        "difficulty": "Hard",
        "question": "The difference between simple and compound interest on a sum of money for 2 years at 5% per annum is $25. What is the principal amount?",
        "options": [
            "$8,000",
            "$10,000",
            "$12,000",
            "$15,000"
        ],
        "correct_answer": 1,
        "formula": "Difference for 2 years = P * (R / 100)\u00b2",
        "explanation": "25 = P * (5 / 100)\u00b2 = P * (1/400).\nP = 25 * 400 = $10,000."
    },
    {
        "id": "quant-algebra-1",
        "category": "Quantitative",
        "topic": "Algebra & Numbers",
        "difficulty": "Easy",
        "question": "If x + (1/x) = 5, what is the value of x\u00b2 + (1/x\u00b2)?",
        "options": [
            "23",
            "25",
            "27",
            "21"
        ],
        "correct_answer": 0,
        "formula": "(x + 1/x)\u00b2 = x\u00b2 + 1/x\u00b2 + 2 => x\u00b2 + 1/x\u00b2 = 5\u00b2 - 2",
        "explanation": "(x + 1/x)\u00b2 = 25.\nx\u00b2 + 1/x\u00b2 + 2 = 25 => x\u00b2 + 1/x\u00b2 = 23."
    },
    {
        "id": "quant-algebra-2",
        "category": "Quantitative",
        "topic": "Algebra & Numbers",
        "difficulty": "Medium",
        "question": "What is the unit digit in the product 7^105?",
        "options": [
            "1",
            "3",
            "7",
            "9"
        ],
        "correct_answer": 2,
        "formula": "Cyclicity of powers of 7 is 4: 7, 9, 3, 1.",
        "explanation": "105 divided by 4 leaves a remainder of 1.\nTherefore, the unit digit is 7^1 = 7."
    },
    {
        "id": "quant-algebra-3",
        "category": "Quantitative",
        "topic": "Algebra & Numbers",
        "difficulty": "Medium",
        "question": "The sum of two numbers is 37 and the difference of their squares is 185. What is the difference between the two numbers?",
        "options": [
            "4",
            "5",
            "6",
            "7"
        ],
        "correct_answer": 1,
        "formula": "a\u00b2 - b\u00b2 = (a + b)(a - b)",
        "explanation": "185 = (a + b)(a - b) = 37 * (a - b).\na - b = 185 / 37 = 5."
    },
    {
        "id": "quant-algebra-4",
        "category": "Quantitative",
        "topic": "Algebra & Numbers",
        "difficulty": "Easy",
        "question": "Find the HCF of 36, 54, and 72.",
        "options": [
            "9",
            "12",
            "18",
            "24"
        ],
        "correct_answer": 2,
        "formula": "Highest Common Factor prime decomposition",
        "explanation": "36 = 2\u00b2 * 3\u00b2, 54 = 2 * 3\u00b3, 72 = 2\u00b3 * 3\u00b2.\nHCF = 2^1 * 3^2 = 2 * 9 = 18."
    },
    {
        "id": "quant-avg-1",
        "category": "Quantitative",
        "topic": "Averages & Mixtures",
        "difficulty": "Easy",
        "question": "The average of 5 consecutive odd numbers is 27. What is the smallest of these numbers?",
        "options": [
            "21",
            "23",
            "25",
            "27"
        ],
        "correct_answer": 1,
        "formula": "In consecutive odd numbers, the average is the median middle number.",
        "explanation": "Middle number = 27.\nThe numbers are 23, 25, 27, 29, 31.\nSmallest number is 23."
    },
    {
        "id": "quant-avg-2",
        "category": "Quantitative",
        "topic": "Averages & Mixtures",
        "difficulty": "Medium",
        "question": "The average weight of 24 students in a class is 40 kg. If the weight of the teacher is included, the average increases by 1 kg. What is the teacher's weight?",
        "options": [
            "62 kg",
            "64 kg",
            "65 kg",
            "68 kg"
        ],
        "correct_answer": 2,
        "formula": "Teacher's weight = New Average + Old Count * Increase",
        "explanation": "Total initial weight = 24 * 40 = 960 kg.\nNew total weight = 25 * 41 = 1025 kg.\nTeacher's weight = 1025 - 960 = 65 kg."
    },
    {
        "id": "quant-avg-3",
        "category": "Quantitative",
        "topic": "Averages & Mixtures",
        "difficulty": "Medium",
        "question": "In what ratio must a grocer mix tea at $60 per kg and $75 per kg to obtain a mixture worth $65 per kg?",
        "options": [
            "1 : 2",
            "2 : 1",
            "3 : 2",
            "2 : 3"
        ],
        "correct_answer": 1,
        "formula": "Rule of Alligation: (Cheaper quantity / Dearer quantity) = (d - m) / (m - c)",
        "explanation": "(75 - 65) / (65 - 60) = 10 / 5 = 2 : 1."
    },
    {
        "id": "quant-pipes-1",
        "category": "Quantitative",
        "topic": "Pipes & Cisterns",
        "difficulty": "Easy",
        "question": "Two pipes A and B can fill a cistern in 12 hours and 15 hours respectively. If both are opened together, how long will they take to fill the cistern?",
        "options": [
            "6 hours",
            "6 hrs 40 mins",
            "7 hours",
            "7 hrs 20 mins"
        ],
        "correct_answer": 1,
        "formula": "(A * B) / (A + B)",
        "explanation": "(12 * 15) / (12 + 15) = 180 / 27 = 20 / 3 hours = 6 hours and 40 minutes."
    },
    {
        "id": "quant-pipes-2",
        "category": "Quantitative",
        "topic": "Pipes & Cisterns",
        "difficulty": "Hard",
        "question": "A cistern can be filled by two pipes in 20 and 30 minutes respectively. When the cistern was empty, the two pipes were started together, but after some time the first pipe was stopped and the cistern was filled in 18 minutes in total. After how much time was the first pipe closed?",
        "options": [
            "6 minutes",
            "8 minutes",
            "10 minutes",
            "12 minutes"
        ],
        "correct_answer": 1,
        "formula": "Pipe B worked for all 18 minutes. Pipe A worked for t minutes.",
        "explanation": "B's 18 min work = 18 / 30 = 3/5.\nWork done by A = 1 - 3/5 = 2/5.\nA takes 20 min for full tank, so for 2/5 work: 20 * (2/5) = 8 minutes."
    },
    {
        "id": "quant-geometry-1",
        "category": "Quantitative",
        "topic": "Mensuration & Geometry",
        "difficulty": "Easy",
        "question": "If the radius of a circle is decreased by 50%, by what percentage is its area decreased?",
        "options": [
            "25%",
            "50%",
            "75%",
            "100%"
        ],
        "correct_answer": 2,
        "formula": "Area is proportional to r\u00b2. % change = -50 - 50 + (50 * 50)/100 = -75%",
        "explanation": "New area = \u03c0 * (0.5 r)\u00b2 = 0.25 * \u03c0 r\u00b2 = 25% of original area.\nDecrease = 100% - 25% = 75%."
    },
    {
        "id": "quant-geometry-2",
        "category": "Quantitative",
        "topic": "Mensuration & Geometry",
        "difficulty": "Medium",
        "question": "The perimeter of a rectangular field is 160 meters and the difference between two adjacent sides is 48 meters. Find the sides of the rectangle.",
        "options": [
            "64 m and 16 m",
            "60 m and 20 m",
            "55 m and 25 m",
            "70 m and 10 m"
        ],
        "correct_answer": 0,
        "formula": "2 * (L + B) = 160 => L + B = 80. L - B = 48.",
        "explanation": "2L = 128 => L = 64 m.\nB = 80 - 64 = 16 m."
    },
    {
        "id": "quant-geometry-3",
        "category": "Quantitative",
        "topic": "Mensuration & Geometry",
        "difficulty": "Hard",
        "question": "A solid metallic sphere of radius 6 cm is melted and recast into small spheres of radius 2 cm each. How many small spheres are formed?",
        "options": [
            "9",
            "18",
            "27",
            "36"
        ],
        "correct_answer": 2,
        "formula": "Number = Volume of big sphere / Volume of small sphere = (R / r)\u00b3",
        "explanation": "(6 / 2)\u00b3 = 3\u00b3 = 27 small spheres."
    },
    {
        "id": "quant-age-1",
        "category": "Quantitative",
        "topic": "Problems on Ages",
        "difficulty": "Easy",
        "question": "The present ratio of ages of father and son is 7 : 3. If the sum of their ages is 60 years, what is the father's age?",
        "options": [
            "35 years",
            "42 years",
            "45 years",
            "49 years"
        ],
        "correct_answer": 1,
        "formula": "Age of father = [7 / (7 + 3)] * 60",
        "explanation": "Father's age = (7/10) * 60 = 42 years."
    },
    {
        "id": "quant-age-2",
        "category": "Quantitative",
        "topic": "Problems on Ages",
        "difficulty": "Medium",
        "question": "Ten years ago, the age of A was three times that of B. Ten years hence, A will be twice as old as B. What is A's present age?",
        "options": [
            "50 years",
            "60 years",
            "70 years",
            "80 years"
        ],
        "correct_answer": 2,
        "formula": "A - 10 = 3*(B - 10); A + 10 = 2*(B + 10)",
        "explanation": "A - 3B = -20 and A - 2B = 10.\nSubtracting yields B = 30.\nA = 2*(30) + 10 = 70 years."
    },
    {
        "id": "quant-clocks-1",
        "category": "Quantitative",
        "topic": "Clocks & Angles",
        "difficulty": "Medium",
        "question": "At 3:40, what is the angle between the hour hand and the minute hand of a clock?",
        "options": [
            "120\u00b0",
            "130\u00b0",
            "140\u00b0",
            "150\u00b0"
        ],
        "correct_answer": 1,
        "formula": "Angle = |30 * H - (11/2) * M|",
        "explanation": "Angle = |30 * 3 - (11/2) * 40| = |90 - 220| = |-130| = 130\u00b0."
    },
    {
        "id": "quant-calendar-1",
        "category": "Quantitative",
        "topic": "Calendar & Days",
        "difficulty": "Easy",
        "question": "If January 1 of a non-leap year falls on a Monday, what day of the week will January 1 of the next year fall on?",
        "options": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Sunday"
        ],
        "correct_answer": 1,
        "formula": "Non-leap year has 365 days = 52 weeks + 1 odd day.",
        "explanation": "An ordinary year advances by 1 odd day. Monday + 1 = Tuesday."
    },
    {
        "id": "quant-series-1",
        "category": "Quantitative",
        "topic": "Algebra & Numbers",
        "difficulty": "Easy",
        "question": "What is the sum of the first 50 natural numbers (1 + 2 + 3 + ... + 50)?",
        "options": [
            "1225",
            "1250",
            "1275",
            "1300"
        ],
        "correct_answer": 2,
        "formula": "Sum = [n * (n + 1)] / 2",
        "explanation": "[50 * 51] / 2 = 25 * 51 = 1275."
    },
    {
        "id": "quant-boats-1",
        "category": "Quantitative",
        "topic": "Speed & Distance",
        "difficulty": "Easy",
        "question": "A boat can travel with a speed of 13 km/h in still water. If the speed of the stream is 4 km/h, find the time taken by the boat to go 68 km downstream.",
        "options": [
            "3 hours",
            "4 hours",
            "5 hours",
            "6 hours"
        ],
        "correct_answer": 1,
        "formula": "Downstream speed = Boat speed + Stream speed",
        "explanation": "Downstream speed = 13 + 4 = 17 km/h.\nTime = 68 / 17 = 4 hours."
    },
    {
        "id": "quant-pipes-3",
        "category": "Quantitative",
        "topic": "Pipes & Cisterns",
        "difficulty": "Medium",
        "question": "Three pipes A, B, and C can fill a tank in 6 hours. After working together for 2 hours, C is closed and A and B fill the remaining part in 7 hours. How long will C alone take to fill the tank?",
        "options": [
            "10 hours",
            "12 hours",
            "14 hours",
            "16 hours"
        ],
        "correct_answer": 2,
        "formula": "Work in 2 hrs = 2/6 = 1/3. Remaining = 2/3.",
        "explanation": "(A+B) do 2/3 work in 7 hrs => (A+B)'s 1-hr rate = 2/21.\nC's 1-hr rate = (1/6) - (2/21) = (7 - 4)/42 = 3/42 = 1/14.\nC alone takes 14 hours."
    },
    {
        "id": "quant-compound-1",
        "category": "Quantitative",
        "topic": "Simple & Compound Interest",
        "difficulty": "Medium",
        "question": "A sum of money placed at compound interest doubles itself in 4 years. In how many years will it amount to 8 times itself?",
        "options": [
            "8 years",
            "12 years",
            "16 years",
            "24 years"
        ],
        "correct_answer": 1,
        "formula": "If money becomes 2^k times, time = k * T",
        "explanation": "8 = 2\u00b3. So time required = 3 * 4 years = 12 years."
    },
    {
        "id": "quant-alligation-1",
        "category": "Quantitative",
        "topic": "Averages & Mixtures",
        "difficulty": "Hard",
        "question": "A container contains 40 liters of milk. From this container 4 liters of milk were taken out and replaced by water. This process was repeated further two times. How much milk is now contained by the container?",
        "options": [
            "26.34 liters",
            "27.36 liters",
            "29.16 liters",
            "30.00 liters"
        ],
        "correct_answer": 2,
        "formula": "Remaining milk = Initial * [1 - (x / C)]^n",
        "explanation": "Remaining = 40 * [1 - (4 / 40)]\u00b3 = 40 * (0.9)\u00b3 = 40 * 0.729 = 29.16 liters."
    },
    {
        "id": "quant-geometry-4",
        "category": "Quantitative",
        "topic": "Mensuration & Geometry",
        "difficulty": "Easy",
        "question": "Find the diagonal of a square whose area is 128 sq. cm.",
        "options": [
            "12 cm",
            "14 cm",
            "16 cm",
            "18 cm"
        ],
        "correct_answer": 2,
        "formula": "Area of square = (diagonal)\u00b2 / 2",
        "explanation": "128 = d\u00b2 / 2 => d\u00b2 = 256 => d = 16 cm."
    },
    {
        "id": "logic-series-1",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the next number in the sequence: 4, 9, 25, 49, 121, 169, ?",
        "options": [
            "225",
            "256",
            "289",
            "361"
        ],
        "correct_answer": 2,
        "formula": "Squares of consecutive prime numbers: 2\u00b2, 3\u00b2, 5\u00b2, 7\u00b2, 11\u00b2, 13\u00b2, 17\u00b2",
        "explanation": "Primes squared: 2\u00b2=4, 3\u00b2=9, 5\u00b2=25, 7\u00b2=49, 11\u00b2=121, 13\u00b2=169. Next prime is 17. 17\u00b2 = 289."
    },
    {
        "id": "logic-series-2",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the missing number in the sequence: 7, 12, 22, 42, 82, ?",
        "options": [
            "142",
            "162",
            "172",
            "182"
        ],
        "correct_answer": 1,
        "formula": "Differences double: +5, +10, +20, +40, +80",
        "explanation": "Differences: 12-7=5, 22-12=10, 42-22=20, 82-42=40. Next difference is 80. 82 + 80 = 162."
    },
    {
        "id": "logic-series-3",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "What comes next in the sequence: 3, 8, 15, 24, 35, ?",
        "options": [
            "46",
            "48",
            "50",
            "52"
        ],
        "correct_answer": 1,
        "formula": "Pattern: n\u00b2 - 1 for n = 2, 3, 4, 5, 6, 7",
        "explanation": "2\u00b2-1=3, 3\u00b2-1=8, 4\u00b2-1=15, 5\u00b2-1=24, 6\u00b2-1=35. Next is 7\u00b2-1 = 49 - 1 = 48."
    },
    {
        "id": "logic-series-4",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the wrong number in the series: 8, 27, 64, 100, 125, 216, 343",
        "options": [
            "27",
            "100",
            "125",
            "343"
        ],
        "correct_answer": 1,
        "formula": "Pattern of cubes: 2\u00b3, 3\u00b3, 4\u00b3, 5\u00b3, 6\u00b3, 7\u00b3",
        "explanation": "All numbers are perfect cubes except 100 (which is 10\u00b2). In place of 100, it should be 4\u00b3 = 64 (or 5\u00b3=125, where 100 is wrong)."
    },
    {
        "id": "logic-series-5",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the next number: 2, 6, 12, 20, 30, 42, 56, ?",
        "options": [
            "64",
            "70",
            "72",
            "74"
        ],
        "correct_answer": 2,
        "formula": "n * (n + 1) for n = 1, 2, 3, 4, 5, 6, 7, 8",
        "explanation": "1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30, 6*7=42, 7*8=56, 8*9=72."
    },
    {
        "id": "logic-series-6",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the missing number: 1, 4, 9, 16, 25, ?",
        "options": [
            "30",
            "35",
            "36",
            "49"
        ],
        "correct_answer": 2,
        "formula": "Consecutive integer squares: 1\u00b2, 2\u00b2, 3\u00b2, 4\u00b2, 5\u00b2, 6\u00b2",
        "explanation": "6\u00b2 = 36."
    },
    {
        "id": "logic-letter-1",
        "category": "Logical",
        "topic": "Letter & Alpha Series",
        "difficulty": "Easy",
        "question": "Find the next term in the letter series: B, D, G, K, P, ?",
        "options": [
            "S",
            "T",
            "U",
            "V"
        ],
        "correct_answer": 3,
        "formula": "Alphabetical steps increase by +1: +2, +3, +4, +5, +6",
        "explanation": "B(+2)=D, D(+3)=G, G(+4)=K, K(+5)=P, P(+6) = V (16 + 6 = 22nd letter V)."
    },
    {
        "id": "logic-letter-2",
        "category": "Logical",
        "topic": "Letter & Alpha Series",
        "difficulty": "Medium",
        "question": "Find the next group in the series: AZ, CX, EV, GT, ?",
        "options": [
            "HS",
            "IR",
            "JQ",
            "KP"
        ],
        "correct_answer": 1,
        "formula": "First letter +2, second letter -2 (opposite pairs)",
        "explanation": "A(+2)->C(+2)->E(+2)->G(+2)->I. Z(-2)->X(-2)->V(-2)->T(-2)->R. Next pair is IR."
    },
    {
        "id": "logic-coding-1",
        "category": "Logical",
        "topic": "Coding & Decoding",
        "difficulty": "Easy",
        "question": "In a certain code language, if 'PYTHON' is coded as 'QZWIPO', how is 'ALGO' coded in that language?",
        "options": [
            "BMHP",
            "BMHQ",
            "BKHP",
            "BLGQ"
        ],
        "correct_answer": 0,
        "formula": "Each letter shifted by +1 in alphabetical index",
        "explanation": "A(+1)=B, L(+1)=M, G(+1)=H, O(+1)=P. Result is BMHP."
    },
    {
        "id": "logic-coding-2",
        "category": "Logical",
        "topic": "Coding & Decoding",
        "difficulty": "Medium",
        "question": "If 'TEACHER' is coded as 'VGCEJGT', how will 'CHILDREN' be coded in that code?",
        "options": [
            "EJKNFTGP",
            "EJKNFPGT",
            "EKJNHTGP",
            "EJKTGPNF"
        ],
        "correct_answer": 0,
        "formula": "Shift each letter by +2",
        "explanation": "C(+2)=E, H(+2)=J, I(+2)=K, L(+2)=N, D(+2)=F, R(+2)=T, E(+2)=G, N(+2)=P -> EJKNFTGP."
    },
    {
        "id": "logic-coding-3",
        "category": "Logical",
        "topic": "Coding & Decoding",
        "difficulty": "Medium",
        "question": "In a certain code, 'ROAD' is written as 'URDG'. How is 'SWAN' written in that code?",
        "options": [
            "VZDQ",
            "VXCQ",
            "UXDQ",
            "VZDQ"
        ],
        "correct_answer": 0,
        "formula": "Each letter shifted by +3 forward",
        "explanation": "S(+3)=V, W(+3)=Z, A(+3)=D, N(+3)=Q -> VZDQ."
    },
    {
        "id": "logic-coding-4",
        "category": "Logical",
        "topic": "Coding & Decoding",
        "difficulty": "Hard",
        "question": "If in a certain language, '975' means 'Throw away garbage', '528' means 'Give away smoking', and '213' means 'Smoking is harmful', which digit stands for 'Give'?",
        "options": [
            "5",
            "8",
            "2",
            "3"
        ],
        "correct_answer": 1,
        "formula": "Common code elimination between sentences",
        "explanation": "'away' is common in 1st & 2nd ('5').\n'smoking' is common in 2nd & 3rd ('2').\nIn '528', remaining word 'Give' corresponds to '8'."
    },
    {
        "id": "logic-blood-1",
        "category": "Logical",
        "topic": "Blood Relations",
        "difficulty": "Medium",
        "question": "Pointing to a photograph, a woman says: 'He is the son of the only son of my grandfather.' How is the man in the photograph related to the woman?",
        "options": [
            "Brother",
            "Father",
            "Cousin",
            "Uncle"
        ],
        "correct_answer": 0,
        "formula": "Decompose familial chain from the end to beginning",
        "explanation": "'Only son of my grandfather' = woman's father.\n'Son of my father' = woman's brother."
    },
    {
        "id": "logic-blood-2",
        "category": "Logical",
        "topic": "Blood Relations",
        "difficulty": "Easy",
        "question": "Introducing a boy, a girl says: 'He is the son of the daughter of the father of my uncle.' How is the boy related to the girl?",
        "options": [
            "Brother",
            "Nephew",
            "Uncle",
            "Son-in-law"
        ],
        "correct_answer": 0,
        "formula": "Father of my uncle = Grandfather. Daughter of grandfather = Mother.",
        "explanation": "Father of my uncle = my grandfather.\nDaughter of grandfather = my mother.\nSon of my mother = my brother."
    },
    {
        "id": "logic-blood-3",
        "category": "Logical",
        "topic": "Blood Relations",
        "difficulty": "Medium",
        "question": "A is B's sister. C is B's mother. D is C's father. E is D's mother. Then, how is A related to D?",
        "options": [
            "Grandmother",
            "Granddaughter",
            "Daughter",
            "Grandfather"
        ],
        "correct_answer": 1,
        "formula": "Generational depth tracing",
        "explanation": "A is daughter of C, and C is daughter of D. Therefore, A is the granddaughter of D."
    },
    {
        "id": "logic-blood-4",
        "category": "Logical",
        "topic": "Blood Relations",
        "difficulty": "Hard",
        "question": "If 'P + Q' means P is the mother of Q, 'P - Q' means P is the brother of Q, and 'P * Q' means P is the father of Q, which of the following means 'R is the maternal uncle of M'?",
        "options": [
            "R - K + M",
            "R + K - M",
            "R * K - M",
            "R - K * M"
        ],
        "correct_answer": 0,
        "formula": "Maternal uncle = Mother's brother",
        "explanation": "In 'R - K + M', K + M means K is mother of M. R - K means R is brother of K.\nHence, R is brother of M's mother, i.e., maternal uncle."
    },
    {
        "id": "logic-syllogism-1",
        "category": "Logical",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All cars are vehicles.\n2. Some vehicles are electric.\nConclusions:\nI. Some cars are electric.\nII. Some electric are vehicles.",
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Both I and II follow",
            "Neither I nor II follows"
        ],
        "correct_answer": 1,
        "formula": "Particular affirmative (Some A are B) converts directly to (Some B are A)",
        "explanation": "Conclusion II is a direct valid conversion of statement 2. Conclusion I is not guaranteed."
    },
    {
        "id": "logic-syllogism-2",
        "category": "Logical",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All mangoes are golden in color.\n2. No golden-colored things are cheap.\nConclusions:\nI. All mangoes are cheap.\nII. Golden-colored mangoes are not cheap.",
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Both follow",
            "Neither follows"
        ],
        "correct_answer": 1,
        "formula": "Transitivity: All A are B, No B are C => No A are C.",
        "explanation": "Since all mangoes are golden and no golden things are cheap, no mangoes are cheap. Conclusion II follows."
    },
    {
        "id": "logic-syllogism-3",
        "category": "Logical",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. Some actors are singers.\n2. All singers are dancers.\nConclusions:\nI. Some actors are dancers.\nII. No singer is an actor.",
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Either I or II follows",
            "Neither follows"
        ],
        "correct_answer": 0,
        "formula": "Some A are B + All B are C => Some A are C",
        "explanation": "Actors overlap with singers, and all singers are dancers. Thus the intersection of actors and singers are dancers. Conclusion I follows."
    },
    {
        "id": "logic-direction-1",
        "category": "Logical",
        "topic": "Direction Sense",
        "difficulty": "Easy",
        "question": "A person walks 10 km North, turns right and walks 6 km, then turns right again and walks 10 km. How far and in what direction is he from the starting point?",
        "options": [
            "6 km East",
            "6 km West",
            "10 km North",
            "16 km East"
        ],
        "correct_answer": 0,
        "formula": "Vector coordinates: (0, 10) -> (6, 10) -> (6, 0)",
        "explanation": "North 10 km, East 6 km, South 10 km lands at 6 km East of origin."
    },
    {
        "id": "logic-direction-2",
        "category": "Logical",
        "topic": "Direction Sense",
        "difficulty": "Medium",
        "question": "Starting from point A, Rahul walks 12 meters South, turns left and walks 5 meters to point B. What is the shortest distance between point A and point B?",
        "options": [
            "11 meters",
            "13 meters",
            "15 meters",
            "17 meters"
        ],
        "correct_answer": 1,
        "formula": "Pythagoras theorem: Distance = \u221a(12\u00b2 + 5\u00b2)",
        "explanation": "\u221a(144 + 25) = \u221a169 = 13 meters."
    },
    {
        "id": "logic-direction-3",
        "category": "Logical",
        "topic": "Direction Sense",
        "difficulty": "Hard",
        "question": "One evening before sunset, two friends Sumit and Mohit were talking to each other face to face. If Mohit's shadow was exactly to his right side, which direction was Sumit facing?",
        "options": [
            "North",
            "South",
            "East",
            "West"
        ],
        "correct_answer": 1,
        "formula": "Sun in West in evening => shadow falls towards East.",
        "explanation": "In evening, sun is in West, so shadow is towards East.\nMohit's right is East => Mohit is facing North.\nSumit is facing Mohit => Sumit is facing South."
    },
    {
        "id": "logic-seating-1",
        "category": "Logical",
        "topic": "Seating Arrangement",
        "difficulty": "Hard",
        "question": "Five friends A, B, C, D, and E are sitting in a circle facing the center. A is to the immediate left of B. E is between C and D. C is to the immediate right of A. Who is to the immediate left of E?",
        "options": [
            "A",
            "B",
            "C",
            "D"
        ],
        "correct_answer": 3,
        "formula": "Circular clockwise/counterclockwise order",
        "explanation": "Facing center, the arrangement in clockwise order is B, A, C, E, D.\nTo the immediate left of E is D."
    },
    {
        "id": "logic-seating-2",
        "category": "Logical",
        "topic": "Seating Arrangement",
        "difficulty": "Medium",
        "question": "Six people P, Q, R, S, T, and U are sitting in a row facing North. P and Q are at the ends. S is to the immediate right of P. Who is to the immediate left of Q?",
        "options": [
            "R",
            "T",
            "U",
            "Cannot be determined"
        ],
        "correct_answer": 3,
        "formula": "Linear position arrangement constraints",
        "explanation": "P is at left end, S is at 2nd pos. Q is at right end (pos 6). Positions 3, 4, 5 among R, T, U are unspecified, so it cannot be determined uniquely."
    },
    {
        "id": "logic-odd-one-1",
        "category": "Logical",
        "topic": "Classification & Analogy",
        "difficulty": "Easy",
        "question": "Choose the pair that does NOT fit the pattern of the others:\nApple : Fruit, Carrot : Vegetable, Rose : Flower, Rice : Wheat",
        "options": [
            "Apple : Fruit",
            "Carrot : Vegetable",
            "Rose : Flower",
            "Rice : Wheat"
        ],
        "correct_answer": 3,
        "formula": "Item : Category relation",
        "explanation": "All others are an item and its category. Rice and Wheat are both parallel items of the category cereal."
    },
    {
        "id": "logic-odd-one-2",
        "category": "Logical",
        "topic": "Classification & Analogy",
        "difficulty": "Easy",
        "question": "Choose the odd number out of the group: 27, 64, 125, 144, 216",
        "options": [
            "27",
            "64",
            "125",
            "144"
        ],
        "correct_answer": 3,
        "formula": "Cubes vs Squares: 3\u00b3=27, 4\u00b3=64, 5\u00b3=125, 6\u00b3=216, but 144 is 12\u00b2",
        "explanation": "144 is a square (12\u00b2), whereas all others are cubes of integers."
    },
    {
        "id": "logic-analogy-1",
        "category": "Logical",
        "topic": "Classification & Analogy",
        "difficulty": "Easy",
        "question": "Architect : Building :: Sculptor : ?",
        "options": [
            "Museum",
            "Stone",
            "Statue",
            "Chisel"
        ],
        "correct_answer": 2,
        "formula": "Creator : Creation analogy",
        "explanation": "An architect designs/creates a building; a sculptor creates a statue."
    },
    {
        "id": "logic-analogy-2",
        "category": "Logical",
        "topic": "Classification & Analogy",
        "difficulty": "Medium",
        "question": "Odometer : Mileage :: Compass : ?",
        "options": [
            "Speed",
            "Direction",
            "Hiking",
            "Needle"
        ],
        "correct_answer": 1,
        "formula": "Instrument : Measurement",
        "explanation": "An odometer measures distance/mileage; a compass indicates direction."
    },
    {
        "id": "logic-clocks-1",
        "category": "Logical",
        "topic": "Clocks & Calendars",
        "difficulty": "Medium",
        "question": "How many times do the hands of a clock coincide in a day (24 hours)?",
        "options": [
            "20 times",
            "22 times",
            "24 times",
            "44 times"
        ],
        "correct_answer": 1,
        "formula": "Coincidence happens 11 times in every 12 hours due to 11-1 overlap.",
        "explanation": "The hands coincide 11 times in 12 hours, thus 22 times in 24 hours."
    },
    {
        "id": "logic-calendar-1",
        "category": "Logical",
        "topic": "Clocks & Calendars",
        "difficulty": "Medium",
        "question": "Today is Monday. After 61 days, it will be:",
        "options": [
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ],
        "correct_answer": 3,
        "formula": "Odd days = 61 mod 7",
        "explanation": "61 / 7 = 8 weeks remainder 5 days. Monday + 5 days = Saturday."
    },
    {
        "id": "logic-assump-1",
        "category": "Logical",
        "topic": "Critical Reasoning",
        "difficulty": "Medium",
        "question": "Statement: 'The government has decided to provide financial assistance to small scale industries to boost local manufacturing.'\nAssumptions:\nI. Small scale industries are currently facing fund shortages.\nII. Financial aid can stimulate production in local industries.",
        "options": [
            "Only assumption I is implicit",
            "Only assumption II is implicit",
            "Both I and II are implicit",
            "Neither is implicit"
        ],
        "correct_answer": 2,
        "formula": "Prerequisites of policy formulation",
        "explanation": "Both assumptions are implicit: aid is given assuming industries need funds and that funds will effectively boost production."
    },
    {
        "id": "logic-assump-2",
        "category": "Logical",
        "topic": "Critical Reasoning",
        "difficulty": "Hard",
        "question": "Statement: 'Should all major exams be conducted purely online?'\nArguments:\nI. Yes, it saves massive amounts of paper and enables faster result generation.\nII. No, students in rural areas with poor internet connectivity will be severely disadvantaged.",
        "options": [
            "Only argument I is strong",
            "Only argument II is strong",
            "Both arguments I and II are strong",
            "Neither is strong"
        ],
        "correct_answer": 2,
        "formula": "Evaluation of environmental and social equity impacts",
        "explanation": "Both arguments touch upon critical, valid dimensions: efficiency/sustainability and digital divide/fairness."
    },
    {
        "id": "logic-cube-1",
        "category": "Logical",
        "topic": "Cube & Dice",
        "difficulty": "Medium",
        "question": "A cube has six faces numbered 1 to 6. If numbers 2 and 4 are adjacent to 1, and 6 is opposite to 1, which number is definitely opposite to 6?",
        "options": [
            "1",
            "3",
            "5",
            "Cannot be determined"
        ],
        "correct_answer": 0,
        "formula": "Opposite face definition",
        "explanation": "The problem directly specifies '6 is opposite to 1', so opposite to 6 is 1."
    },
    {
        "id": "logic-venn-1",
        "category": "Logical",
        "topic": "Venn Diagrams",
        "difficulty": "Easy",
        "question": "Which of the following diagrams best represents the relationship between: Animals, Dogs, and Pets?",
        "options": [
            "All dogs are animals, and some dogs and some other animals are pets",
            "All animals are dogs",
            "All pets are animals, and no dogs are pets",
            "Three disjoint circles"
        ],
        "correct_answer": 0,
        "formula": "Set subset and intersection rules",
        "explanation": "All dogs are animals (Dog circle inside Animal circle). Some dogs are pets, and some other animals are also pets (Pet circle intersects both)."
    },
    {
        "id": "logic-ranking-1",
        "category": "Logical",
        "topic": "Order & Ranking",
        "difficulty": "Easy",
        "question": "In a row of 40 students, Rohan's rank is 17th from the top. What is his rank from the bottom?",
        "options": [
            "23rd",
            "24th",
            "25th",
            "26th"
        ],
        "correct_answer": 1,
        "formula": "Rank from bottom = Total - Rank from top + 1",
        "explanation": "40 - 17 + 1 = 24th."
    },
    {
        "id": "logic-ranking-2",
        "category": "Logical",
        "topic": "Order & Ranking",
        "difficulty": "Medium",
        "question": "In a class of students, Ravi is 7th from the left and Sunita is 12th from the right. If they interchange their positions, Ravi becomes 22nd from the left. How many students are there in the class?",
        "options": [
            "31",
            "33",
            "34",
            "35"
        ],
        "correct_answer": 1,
        "formula": "Total = New left rank of A + Original right rank of B - 1",
        "explanation": "Ravi is now at Sunita's original position. Total = 22 + 12 - 1 = 33."
    },
    {
        "id": "logic-matrix-1",
        "category": "Logical",
        "topic": "Missing Character in Matrix",
        "difficulty": "Medium",
        "question": "In a 3x3 grid, row 1 has (2, 3, 13), row 2 has (4, 5, 41), row 3 has (3, 4, ?). Find the missing number.",
        "options": [
            "20",
            "25",
            "27",
            "30"
        ],
        "correct_answer": 1,
        "formula": "Row pattern: a\u00b2 + b\u00b2 = c",
        "explanation": "2\u00b2 + 3\u00b2 = 4 + 9 = 13.\n4\u00b2 + 5\u00b2 = 16 + 25 = 41.\n3\u00b2 + 4\u00b2 = 9 + 16 = 25."
    },
    {
        "id": "logic-matrix-2",
        "category": "Logical",
        "topic": "Missing Character in Matrix",
        "difficulty": "Hard",
        "question": "Find the missing number in the table:\n[6, 9, 15]\n[8, 12, 20]\n[4, 6, ?]",
        "options": [
            "8",
            "10",
            "12",
            "14"
        ],
        "correct_answer": 1,
        "formula": "Col 1 + Col 2 = Col 3 is not it; Col 1 : Col 2 = 2:3, Col 3 = Col 1 * 2.5",
        "explanation": "Row 1: 6 * 2.5 = 15.\nRow 2: 8 * 2.5 = 20.\nRow 3: 4 * 2.5 = 10."
    },
    {
        "id": "logic-puzzle-1",
        "category": "Logical",
        "topic": "Puzzles",
        "difficulty": "Hard",
        "question": "Four friends W, X, Y, and Z have different professions: Doctor, Lawyer, Engineer, and Teacher. W is neither Doctor nor Teacher. Y is an Engineer. X is not a Teacher. Who is the Teacher?",
        "options": [
            "W",
            "X",
            "Y",
            "Z"
        ],
        "correct_answer": 3,
        "formula": "Elimination grid",
        "explanation": "Y = Engineer.\nW is neither Doctor nor Teacher => W = Lawyer.\nX is not Teacher => X = Doctor.\nTherefore, Z must be the Teacher."
    },
    {
        "id": "logic-suffic-1",
        "category": "Logical",
        "topic": "Data Sufficiency",
        "difficulty": "Medium",
        "question": "Is X greater than Y?\nStatement 1: X - 5 > Y\nStatement 2: Y > 0",
        "options": [
            "Statement 1 alone is sufficient",
            "Statement 2 alone is sufficient",
            "Both statements together are needed",
            "Neither is sufficient"
        ],
        "correct_answer": 0,
        "formula": "Inequality testing",
        "explanation": "From statement 1: X > Y + 5. Since 5 > 0, X is strictly greater than Y regardless of Y's sign. Statement 1 alone is sufficient."
    },
    {
        "id": "logic-suffic-2",
        "category": "Logical",
        "topic": "Data Sufficiency",
        "difficulty": "Hard",
        "question": "What is the two-digit number?\nStatement 1: The sum of the digits is 9.\nStatement 2: Reversing the digits gives a number 27 less than the original number.",
        "options": [
            "Statement 1 alone is sufficient",
            "Statement 2 alone is sufficient",
            "Both statements together are sufficient",
            "Statements together are not sufficient"
        ],
        "correct_answer": 2,
        "formula": "10x + y - (10y + x) = 27 => 9(x - y) = 27 => x - y = 3. Combined with x + y = 9.",
        "explanation": "x - y = 3 and x + y = 9 gives 2x = 12 => x = 6, y = 3. The number is 63. Both statements together are sufficient."
    },
    {
        "id": "logic-coding-5",
        "category": "Logical",
        "topic": "Coding & Decoding",
        "difficulty": "Easy",
        "question": "If 'RED' is coded as '27' (R=18, E=5, D=4 => 18+5+4=27), what is the code for 'BLUE'?",
        "options": [
            "36",
            "40",
            "42",
            "44"
        ],
        "correct_answer": 1,
        "formula": "Sum of alphabetical position numbers",
        "explanation": "B=2, L=12, U=21, E=5. Sum = 2 + 12 + 21 + 5 = 40."
    },
    {
        "id": "logic-series-7",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the next number: 1, 2, 6, 24, 120, ?",
        "options": [
            "240",
            "480",
            "720",
            "840"
        ],
        "correct_answer": 2,
        "formula": "Factorial sequence: n!",
        "explanation": "1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720."
    },
    {
        "id": "logic-series-8",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the missing number in the series: 3, 5, 9, 17, 33, ?",
        "options": [
            "49",
            "65",
            "67",
            "72"
        ],
        "correct_answer": 1,
        "formula": "Pattern: 2*x - 1 or differences 2, 4, 8, 16, 32",
        "explanation": "Differences double: +2, +4, +8, +16, +32. 33 + 32 = 65."
    },
    {
        "id": "logic-clock-2",
        "category": "Logical",
        "topic": "Clocks & Calendars",
        "difficulty": "Easy",
        "question": "At what time between 4 and 5 o'clock will the hands of a clock be pointing in opposite directions (180\u00b0)?",
        "options": [
            "4:50",
            "4:54 6/11",
            "4:55",
            "4:52 8/11"
        ],
        "correct_answer": 1,
        "formula": "Time = (5H + 30) * (12/11)",
        "explanation": "(5*4 + 30) * (12/11) = 50 * (12/11) = 600/11 = 54 6/11 minutes past 4."
    },
    {
        "id": "logic-syllogism-4",
        "category": "Logical",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All cats are mammals.\n2. All mammals are warm-blooded.\nConclusion: All cats are warm-blooded.",
        "options": [
            "Valid conclusion",
            "Invalid conclusion",
            "Partially valid",
            "Cannot say"
        ],
        "correct_answer": 0,
        "formula": "Hypothetical Syllogism: All A are B, All B are C => All A are C.",
        "explanation": "Direct logical deduction: All cats are mammals and all mammals are warm-blooded, so all cats are warm-blooded."
    },
    {
        "id": "logic-direction-4",
        "category": "Logical",
        "topic": "Direction Sense",
        "difficulty": "Easy",
        "question": "If South-East becomes North, North-East becomes West, and so on, what will West become?",
        "options": [
            "North-East",
            "South-East",
            "South-West",
            "North-West"
        ],
        "correct_answer": 1,
        "formula": "Clockwise rotation by 135 degrees",
        "explanation": "South-East to North is 135\u00b0 counter-clockwise. Turning West counter-clockwise by 135\u00b0 gives South-East."
    },
    {
        "id": "logic-letter-3",
        "category": "Logical",
        "topic": "Letter & Alpha Series",
        "difficulty": "Medium",
        "question": "Find the missing term: YEB, WFD, UHG, SKI, ?",
        "options": [
            "QOL",
            "QGL",
            "TOL",
            "QNL"
        ],
        "correct_answer": 0,
        "formula": "1st letter -2, 2nd letter +1, +2, +3, 3rd letter +2, +3, +2, +3",
        "explanation": "Y(-2)->W(-2)->U(-2)->S(-2)->Q.\nE(+1)->F(+2)->H(+3)->K(+4)->O.\nB(+2)->D(+3)->G(+2)->I(+3)->L. Result is QOL."
    },
    {
        "id": "logic-analogy-3",
        "category": "Logical",
        "topic": "Classification & Analogy",
        "difficulty": "Easy",
        "question": "Pen : Writer :: Axe : ?",
        "options": [
            "Cobbler",
            "Woodcutter",
            "Carpenter",
            "Barber"
        ],
        "correct_answer": 1,
        "formula": "Tool : Profession analogy",
        "explanation": "A pen is the characteristic tool of a writer; an axe is the characteristic tool of a woodcutter."
    },
    {
        "id": "logic-seating-3",
        "category": "Logical",
        "topic": "Seating Arrangement",
        "difficulty": "Medium",
        "question": "Four girls A, B, C, D are sitting on a bench. A is sitting next to B, C is sitting next to D. C is not sitting with B. D is on the extreme left. Who is sitting in the middle?",
        "options": [
            "A and B",
            "B and C",
            "A and C",
            "C and A"
        ],
        "correct_answer": 1,
        "formula": "Linear position tracking",
        "explanation": "D is extreme left: D, C (since C next to D). C cannot sit with B, so A must sit next to C, followed by B: D, C, A, wait: if D, C, A, B, the middle two are C and A, but wait, B and C... D is at 1, C is at 2, A is at 3, B is at 4."
    },
    {
        "id": "logic-blood-5",
        "category": "Logical",
        "topic": "Blood Relations",
        "difficulty": "Easy",
        "question": "A is the brother of B. B is the daughter of C. D is the father of A. How is C related to D?",
        "options": [
            "Wife",
            "Husband",
            "Sister",
            "Mother"
        ],
        "correct_answer": 0,
        "formula": "Parental relationship deduction",
        "explanation": "A and B are siblings. D is their father, and B is C's daughter. Therefore, C is their mother and D's wife."
    },
    {
        "id": "logic-series-9",
        "category": "Logical",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the missing number in: 2, 3, 5, 7, 11, 13, 17, ?",
        "options": [
            "19",
            "21",
            "23",
            "25"
        ],
        "correct_answer": 0,
        "formula": "Consecutive prime numbers",
        "explanation": "The series consists of consecutive primes. The next prime after 17 is 19."
    },
    {
        "id": "logic-puzzle-2",
        "category": "Logical",
        "topic": "Puzzles",
        "difficulty": "Medium",
        "question": "A is taller than B, but shorter than C. D is taller than E, but shorter than B. Who is the tallest among them?",
        "options": [
            "A",
            "B",
            "C",
            "D"
        ],
        "correct_answer": 2,
        "formula": "Inequality height chain: C > A > B > D > E",
        "explanation": "C > A > B > D > E. The tallest person is C."
    },
    {
        "id": "verbal-vocab-1",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Easy",
        "question": "Select the word most nearly OPPOSITE in meaning to 'EPHEMERAL':",
        "options": [
            "Transient",
            "Permanent",
            "Fleeting",
            "Volatile"
        ],
        "correct_answer": 1,
        "formula": "Ephemeral = short-lived. Antonym = Permanent.",
        "explanation": "'Ephemeral' means lasting for a very brief time. Its direct antonym is 'Permanent' (enduring)."
    },
    {
        "id": "verbal-vocab-2",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Medium",
        "question": "Choose the word closest in meaning to 'PRAGMATIC':",
        "options": [
            "Idealistic",
            "Practical",
            "Theoretical",
            "Dogmatic"
        ],
        "correct_answer": 1,
        "formula": "Pragmatic = dealing with things sensibly and practically.",
        "explanation": "'Pragmatic' means practical rather than theoretical. 'Practical' is the correct synonym."
    },
    {
        "id": "verbal-vocab-3",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Medium",
        "question": "Select the synonym of 'METICULOUS':",
        "options": [
            "Careless",
            "Thorough",
            "Hasty",
            "Indifferent"
        ],
        "correct_answer": 1,
        "formula": "Meticulous = showing great attention to detail.",
        "explanation": "'Meticulous' means very careful and thorough with precise attention to detail."
    },
    {
        "id": "verbal-vocab-4",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Easy",
        "question": "Choose the word OPPOSITE in meaning to 'CANDID':",
        "options": [
            "Frank",
            "Deceitful",
            "Blunt",
            "Honest"
        ],
        "correct_answer": 1,
        "formula": "Candid = truthful and straightforward. Antonym = Deceitful/Guarded.",
        "explanation": "'Candid' means outspoken and honest. Its antonym is 'Deceitful' or secretive."
    },
    {
        "id": "verbal-vocab-5",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Hard",
        "question": "Select the synonym of 'UBIQUITOUS':",
        "options": [
            "Omnipresent",
            "Rare",
            "Localized",
            "Obscure"
        ],
        "correct_answer": 0,
        "formula": "Ubiquitous = present, appearing, or found everywhere.",
        "explanation": "'Ubiquitous' means present everywhere simultaneously, matching 'Omnipresent'."
    },
    {
        "id": "verbal-vocab-6",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Hard",
        "question": "Choose the word OPPOSITE in meaning to 'OBSEQUIOUS':",
        "options": [
            "Submissive",
            "Assertive",
            "Servile",
            "Fawning"
        ],
        "correct_answer": 1,
        "formula": "Obsequious = obedient or attentive to an excessive or servile degree.",
        "explanation": "The opposite of fawning or overly servile behavior is 'Assertive' or independent."
    },
    {
        "id": "verbal-vocab-7",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Medium",
        "question": "Select the synonym of 'LUCID':",
        "options": [
            "Confusing",
            "Clear",
            "Vague",
            "Dark"
        ],
        "correct_answer": 1,
        "formula": "Lucid = expressed clearly; easy to understand.",
        "explanation": "'Lucid' means clear and intelligible."
    },
    {
        "id": "verbal-vocab-8",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Medium",
        "question": "Choose the antonym of 'BENEVOLENT':",
        "options": [
            "Malevolent",
            "Kind",
            "Generous",
            "Helpful"
        ],
        "correct_answer": 0,
        "formula": "Bene (good) vs Mal (bad)",
        "explanation": "'Benevolent' means well-meaning and kindly. 'Malevolent' means wishing harm to others."
    },
    {
        "id": "verbal-grammar-1",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Easy",
        "question": "Identify the sentence with the correct subject-verb agreement:",
        "options": [
            "Neither the manager nor the employees was present.",
            "Neither the manager nor the employees were present.",
            "Neither the employees nor the manager were present.",
            "Neither the manager or the employees is present."
        ],
        "correct_answer": 1,
        "formula": "In 'Neither... nor', the verb agrees with the closer subject.",
        "explanation": "'Employees' is plural and adjacent to the verb, so 'were' is grammatically correct."
    },
    {
        "id": "verbal-grammar-2",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Medium",
        "question": "Choose the grammatically correct sentence:",
        "options": [
            "Each of the participants have received their certificate.",
            "Each of the participants has received his or her certificate.",
            "Each of the participants were receiving their certificate.",
            "Each of the participant have received the certificate."
        ],
        "correct_answer": 1,
        "formula": "'Each' is an indefinite singular pronoun requiring a singular verb 'has'.",
        "explanation": "'Each' is grammatically singular, requiring the singular auxiliary 'has'."
    },
    {
        "id": "verbal-grammar-3",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Medium",
        "question": "Which of the following sentences correctly uses a conditional clause?",
        "options": [
            "If I would have known, I would tell you.",
            "If I had known, I would have told you.",
            "If I knew, I will have told you.",
            "If I had known, I will tell you."
        ],
        "correct_answer": 1,
        "formula": "Third conditional: If + Past Perfect, would have + Past Participle.",
        "explanation": "Past unreal conditional uses 'If + had known ... would have told'."
    },
    {
        "id": "verbal-grammar-4",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Hard",
        "question": "Find the error in the sentence: 'Scarcely had he entered the room (A) / than the phone (B) / started ringing violently (C) / No error (D)'",
        "options": [
            "Part A",
            "Part B",
            "Part C",
            "No error (D)"
        ],
        "correct_answer": 1,
        "formula": "Correlative conjunction pair: 'Scarcely / Hardly ... when', NOT 'than'.",
        "explanation": "'Scarcely' is paired with 'when', not 'than'. It should be 'when the phone started ringing'."
    },
    {
        "id": "verbal-grammar-5",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Easy",
        "question": "Select the correct option to complete: 'She has been working here _____ 2018.'",
        "options": [
            "for",
            "since",
            "from",
            "in"
        ],
        "correct_answer": 1,
        "formula": "'Since' is used with a specific point in time; 'for' is used with a duration.",
        "explanation": "2018 is a specific point in time, so 'since 2018' is correct with present perfect continuous."
    },
    {
        "id": "verbal-idiom-1",
        "category": "Verbal",
        "topic": "Idioms & Phrases",
        "difficulty": "Easy",
        "question": "What does the idiom 'Bite the bullet' mean?",
        "options": [
            "To eat something dangerous",
            "To face a difficult or unpleasant situation with courage",
            "To make a quick and hasty decision",
            "To express extreme anger"
        ],
        "correct_answer": 1,
        "formula": "Historical idiom originating from battlefield medical procedures.",
        "explanation": "'To bite the bullet' means to face a tough situation bravely without evading it."
    },
    {
        "id": "verbal-idiom-2",
        "category": "Verbal",
        "topic": "Idioms & Phrases",
        "difficulty": "Medium",
        "question": "What is the meaning of 'Burn the midnight oil'?",
        "options": [
            "To waste energy recklessly",
            "To work or study late into the night",
            "To cause accidental damage",
            "To celebrate late at night"
        ],
        "correct_answer": 1,
        "formula": "Idiomatic expression for diligence.",
        "explanation": "Refers to burning an oil lamp while studying or working late through the night."
    },
    {
        "id": "verbal-idiom-3",
        "category": "Verbal",
        "topic": "Idioms & Phrases",
        "difficulty": "Easy",
        "question": "What does 'A blessing in disguise' mean?",
        "options": [
            "A completely unfortunate tragedy",
            "An apparent misfortune that eventually results in something good",
            "A religious ceremony",
            "A gift given in secret"
        ],
        "correct_answer": 1,
        "formula": "Idiom of unexpected positive outcomes.",
        "explanation": "Something that initially seemed bad or unlucky, but resulted in something good happening later."
    },
    {
        "id": "verbal-idiom-4",
        "category": "Verbal",
        "topic": "Idioms & Phrases",
        "difficulty": "Hard",
        "question": "What does the idiom 'To take the bull by the horns' mean?",
        "options": [
            "To pick a fight unnecessarily",
            "To tackle a problem directly and courageously",
            "To engage in bullfighting",
            "To avoid a confrontation skillfully"
        ],
        "correct_answer": 1,
        "formula": "Metaphor for assertive problem confrontation.",
        "explanation": "It means to directly and fearlessly confront a dangerous or challenging problem."
    },
    {
        "id": "verbal-comp-1",
        "category": "Verbal",
        "topic": "Reading Comprehension",
        "difficulty": "Medium",
        "question": "'Artificial Intelligence has transformed modern industries by automating repetitive tasks, allowing human workers to concentrate on higher-order creative and strategic problem-solving.'\nAccording to the passage, AI enables human workers to:",
        "options": [
            "Stop working entirely",
            "Focus exclusively on manual repetitive tasks",
            "Direct their attention towards creative and strategic challenges",
            "Replace managerial positions immediately"
        ],
        "correct_answer": 2,
        "formula": "Direct factual inference from text passage.",
        "explanation": "The passage clearly states that AI allows humans to 'concentrate on higher-order creative and strategic problem-solving.'"
    },
    {
        "id": "verbal-comp-2",
        "category": "Verbal",
        "topic": "Reading Comprehension",
        "difficulty": "Hard",
        "question": "'Renewable energy adoption has accelerated significantly over the past decade, driven by rapid technological innovations and falling production costs. However, grid integration remains a critical bottleneck, as intermittent generation from solar and wind requires substantial energy storage infrastructure.'\nWhat is the primary challenge highlighted in the passage?",
        "options": [
            "The rising cost of wind turbines",
            "Lack of technological innovation in renewables",
            "Storage and grid integration due to intermittent generation",
            "Public resistance to green energy"
        ],
        "correct_answer": 2,
        "formula": "Identifying the central thesis/problem in analytical text.",
        "explanation": "The text identifies 'grid integration' and intermittent generation requiring storage infrastructure as the critical bottleneck."
    },
    {
        "id": "verbal-fill-1",
        "category": "Verbal",
        "topic": "Fill in the Blanks",
        "difficulty": "Medium",
        "question": "Despite the rigorous schedule, she managed to _____ her studies with extracurricular activities effortlessly.",
        "options": [
            "balance",
            "postpone",
            "disrupt",
            "alienate"
        ],
        "correct_answer": 0,
        "formula": "Contextual semantic fit with 'effortlessly' and 'studies with extracurriculars'.",
        "explanation": "'Balance' is the only verb that fits the context of effectively managing two concurrent commitments."
    },
    {
        "id": "verbal-fill-2",
        "category": "Verbal",
        "topic": "Fill in the Blanks",
        "difficulty": "Easy",
        "question": "The detective scrutinized the crime scene to find clues that were _____ to the untrained eye.",
        "options": [
            "invisible",
            "obvious",
            "clear",
            "prominent"
        ],
        "correct_answer": 0,
        "formula": "Contrast between a trained detective and an untrained observer.",
        "explanation": "'Invisible' or undetectable to the untrained eye contrasts with the detective's careful scrutiny."
    },
    {
        "id": "verbal-fill-3",
        "category": "Verbal",
        "topic": "Fill in the Blanks",
        "difficulty": "Medium",
        "question": "The company's CEO emphasized that innovation is _____ to maintaining a competitive edge in the global market.",
        "options": [
            "redundant",
            "essential",
            "detrimental",
            "negligible"
        ],
        "correct_answer": 1,
        "formula": "Positive business rationale linking innovation to competitive edge.",
        "explanation": "'Essential' (vital/indispensable) is the only logical adjective that makes semantic sense."
    },
    {
        "id": "verbal-oneword-1",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Easy",
        "question": "A person who is fluent in two languages is called:",
        "options": [
            "Monoglot",
            "Bilingual",
            "Polyglot",
            "Linguist"
        ],
        "correct_answer": 1,
        "formula": "Bi (two) + lingual (languages).",
        "explanation": "A person speaking two languages fluently is 'Bilingual'."
    },
    {
        "id": "verbal-oneword-2",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Medium",
        "question": "One who looks at the bright side of things is an:",
        "options": [
            "Pessimist",
            "Optimist",
            "Pacifist",
            "Altruist"
        ],
        "correct_answer": 1,
        "formula": "Definition of positive disposition.",
        "explanation": "An 'Optimist' expects positive outcomes and sees the bright side."
    },
    {
        "id": "verbal-oneword-3",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Hard",
        "question": "A person who leaves their own country to settle permanently in another is an:",
        "options": [
            "Immigrant",
            "Emigrant",
            "Refugee",
            "Expatriate"
        ],
        "correct_answer": 1,
        "formula": "E- (out of country) vs Im- (into country).",
        "explanation": "An 'Emigrant' is someone who leaves their native country (exiting); an immigrant enters a new country."
    },
    {
        "id": "verbal-oneword-4",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Medium",
        "question": "Something that cannot be heard is described as:",
        "options": [
            "Inaudible",
            "Unheard",
            "Silent",
            "Faint"
        ],
        "correct_answer": 0,
        "formula": "In- (not) + audire (to hear) + -ible (capable of).",
        "explanation": "'Inaudible' means incapable of being heard."
    },
    {
        "id": "verbal-parajumble-1",
        "category": "Verbal",
        "topic": "Para Jumbles",
        "difficulty": "Medium",
        "question": "Arrange the following sentences in a logical sequence:\nP: He decided to pursue computer engineering.\nQ: From early childhood, Rahul was fascinated by computing machines.\nR: After graduating with honors, he joined a premier tech startup.\nS: This childhood interest grew into a passionate vocation.",
        "options": [
            "Q-S-P-R",
            "Q-P-S-R",
            "P-Q-S-R",
            "S-Q-P-R"
        ],
        "correct_answer": 0,
        "formula": "Chronological progression: Childhood fascination (Q) -> grew into vocation (S) -> study choice (P) -> career (R).",
        "explanation": "Q introduces the subject and early fascination. S elaborates on the childhood interest. P discusses his degree choice. R concludes with his graduation and career."
    },
    {
        "id": "verbal-parajumble-2",
        "category": "Verbal",
        "topic": "Para Jumbles",
        "difficulty": "Hard",
        "question": "Arrange in logical order:\nP: Electric vehicles emit zero tailpipe emissions.\nQ: Therefore, transitioning to EVs is vital for combating urban smog.\nR: Transportation accounts for a major share of global carbon emissions.\nS: Replacing internal combustion engines reduces air pollution significantly.",
        "options": [
            "R-P-S-Q",
            "P-R-S-Q",
            "R-S-P-Q",
            "Q-P-S-R"
        ],
        "correct_answer": 0,
        "formula": "Broad problem (R) -> specific EV trait (P) -> pollution effect (S) -> conclusive policy recommendation (Q).",
        "explanation": "R states the global problem. P notes EV emissions zero. S explains the consequence of replacement. Q provides the 'Therefore' conclusion."
    },
    {
        "id": "verbal-spell-1",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Easy",
        "question": "Select the correctly spelled word:",
        "options": [
            "Accomodation",
            "Accommodation",
            "Acommodation",
            "Accomadation"
        ],
        "correct_answer": 1,
        "formula": "Double 'c' and double 'm': AC-COM-MO-DA-TION.",
        "explanation": "'Accommodation' is spelled with two 'c's and two 'm's."
    },
    {
        "id": "verbal-spell-2",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Medium",
        "question": "Select the correctly spelled word:",
        "options": [
            "Mischievious",
            "Mischievous",
            "Mischevious",
            "Mischivous"
        ],
        "correct_answer": 1,
        "formula": "M-I-S-C-H-I-E-V-O-U-S (no extra 'i' before -ous).",
        "explanation": "'Mischievous' ends with '-vous', not '-vious'."
    },
    {
        "id": "verbal-vocab-9",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Medium",
        "question": "Choose the word closest in meaning to 'ZEALOUS':",
        "options": [
            "Enthusiastic",
            "Jealous",
            "Lazy",
            "Reluctant"
        ],
        "correct_answer": 0,
        "formula": "Zealous = full of zeal, fervor, or enthusiasm.",
        "explanation": "'Zealous' means fervently devoted, enthusiastic, and passionate."
    },
    {
        "id": "verbal-vocab-10",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Hard",
        "question": "Choose the word OPPOSITE in meaning to 'GARRULOUS':",
        "options": [
            "Loquacious",
            "Taciturn",
            "Talkative",
            "Voluble"
        ],
        "correct_answer": 1,
        "formula": "Garrulous = excessively talkative. Antonym = Taciturn (quiet/reserved).",
        "explanation": "'Taciturn' means reserved or uncommunicative in speech, the opposite of talkative 'Garrulous'."
    },
    {
        "id": "verbal-vocab-11",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Easy",
        "question": "Select the synonym of 'FEEBLE':",
        "options": [
            "Strong",
            "Weak",
            "Robust",
            "Sturdy"
        ],
        "correct_answer": 1,
        "formula": "Feeble = lacking physical strength, especially as a result of age or illness.",
        "explanation": "'Feeble' means weak and lacking strength."
    },
    {
        "id": "verbal-grammar-6",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Medium",
        "question": "Fill in the blank with the correct preposition: 'The team was congratulating him _____ his remarkable achievement.'",
        "options": [
            "for",
            "on",
            "at",
            "about"
        ],
        "correct_answer": 1,
        "formula": "Standard English preposition pairing: 'Congratulate on (an event/success)'.",
        "explanation": "The idiomatic verb pairing is 'to congratulate someone ON something'."
    },
    {
        "id": "verbal-grammar-7",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Hard",
        "question": "Choose the correct sentence regarding misplaced modifiers:",
        "options": [
            "Barking loudly, the mailman was frightened by the dog.",
            "Barking loudly, the dog frightened the mailman.",
            "The dog frightened the mailman barking loudly.",
            "The mailman was barking loudly when frightened by the dog."
        ],
        "correct_answer": 1,
        "formula": "Participial modifier must immediately precede the noun it modifies.",
        "explanation": "The dog was barking loudly, so the introductory participial phrase must be followed by 'the dog'."
    },
    {
        "id": "verbal-idiom-5",
        "category": "Verbal",
        "topic": "Idioms & Phrases",
        "difficulty": "Easy",
        "question": "What does 'Break the ice' mean?",
        "options": [
            "To break physical ice cubes",
            "To initiate a conversation in a socially awkward situation",
            "To show intense hostility",
            "To dissolve a partnership"
        ],
        "correct_answer": 1,
        "formula": "Idiomatic expression for relieving social tension.",
        "explanation": "'To break the ice' means to ease social stiffness and start friendly dialogue."
    },
    {
        "id": "verbal-idiom-6",
        "category": "Verbal",
        "topic": "Idioms & Phrases",
        "difficulty": "Medium",
        "question": "What is the meaning of 'Cry over spilt milk'?",
        "options": [
            "To grieve over an unavoidable loss that cannot be undone",
            "To waste food careless",
            "To alert others to an impending emergency",
            "To shed tears without genuine sorrow"
        ],
        "correct_answer": 0,
        "formula": "Futile regret metaphor.",
        "explanation": "To worry or regret about past events that cannot be changed or rectified."
    },
    {
        "id": "verbal-comp-3",
        "category": "Verbal",
        "topic": "Reading Comprehension",
        "difficulty": "Medium",
        "question": "'Quantum computers leverage quantum superposition and entanglement to execute specific computational tasks exponentially faster than classical supercomputers. However, maintaining quantum coherence requires extreme cryogenic refrigeration and rigorous error mitigation.'\nWhich statement is supported by the text?",
        "options": [
            "Quantum computers operate at high room temperatures.",
            "Cryogenic cooling and error mitigation are necessary to maintain quantum coherence.",
            "Quantum computers are slower than classical machines on all tasks.",
            "Classical supercomputers have been rendered obsolete."
        ],
        "correct_answer": 1,
        "formula": "Textual evidence extraction.",
        "explanation": "The passage states that maintaining quantum coherence requires extreme cryogenic refrigeration and error mitigation."
    },
    {
        "id": "verbal-oneword-5",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Easy",
        "question": "A life history of a person written by that person themselves is called:",
        "options": [
            "Biography",
            "Autobiography",
            "Chronicle",
            "Memoir"
        ],
        "correct_answer": 1,
        "formula": "Auto (self) + bio (life) + graphy (writing).",
        "explanation": "An 'Autobiography' is an account of a person's life written by themselves."
    },
    {
        "id": "verbal-oneword-6",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Medium",
        "question": "A doctor who specializes in diseases of the heart is a:",
        "options": [
            "Neurologist",
            "Dermatologist",
            "Cardiologist",
            "Pathologist"
        ],
        "correct_answer": 2,
        "formula": "Cardio- (heart) + logist (specialist).",
        "explanation": "A 'Cardiologist' specializes in the cardiovascular system and heart conditions."
    },
    {
        "id": "verbal-vocab-12",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Medium",
        "question": "What is the synonym of 'DILIGENT'?",
        "options": [
            "Industrious",
            "Lethargic",
            "Careless",
            "Lazy"
        ],
        "correct_answer": 0,
        "formula": "Diligent = hardworking and conscientious.",
        "explanation": "'Industrious' and 'Diligent' both denote hard work and persistent effort."
    },
    {
        "id": "verbal-vocab-13",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Hard",
        "question": "Choose the word OPPOSITE in meaning to 'NEBULOUS':",
        "options": [
            "Cloudy",
            "Distinct",
            "Vague",
            "Amorphous"
        ],
        "correct_answer": 1,
        "formula": "Nebulous = vague, hazy, unclear. Antonym = Distinct, clear.",
        "explanation": "'Nebulous' means hazy or ill-defined. Its antonym is 'Distinct' (clear and well-defined)."
    },
    {
        "id": "verbal-grammar-8",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Easy",
        "question": "Select the correct sentence:",
        "options": [
            "He is senior than me in the company.",
            "He is senior to me in the company.",
            "He is more senior than me in the company.",
            "He is senior from me in the company."
        ],
        "correct_answer": 1,
        "formula": "Adjectives ending in -ior (senior, junior, prior, superior) take 'to', not 'than'.",
        "explanation": "Latin comparatives like 'senior', 'junior', and 'superior' are followed by 'to'."
    },
    {
        "id": "verbal-grammar-9",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Medium",
        "question": "Identify the passive form: 'The chef cooked an exquisite dinner.'",
        "options": [
            "An exquisite dinner was cooked by the chef.",
            "An exquisite dinner is being cooked by the chef.",
            "An exquisite dinner had been cooked by the chef.",
            "The chef was cooking an exquisite dinner."
        ],
        "correct_answer": 0,
        "formula": "Past simple passive: Object + was/were + past participle + by + Subject.",
        "explanation": "'Cooked' (past simple) converts to 'was cooked by the chef'."
    },
    {
        "id": "verbal-fill-4",
        "category": "Verbal",
        "topic": "Fill in the Blanks",
        "difficulty": "Easy",
        "question": "She has an extraordinary _____ for learning complex computer languages quickly.",
        "options": [
            "aptitude",
            "altitude",
            "attitude",
            "amplitude"
        ],
        "correct_answer": 0,
        "formula": "Aptitude = natural ability or fitness for a specific skill.",
        "explanation": "'Aptitude' means natural talent or suitability for acquiring a skill."
    },
    {
        "id": "verbal-fill-5",
        "category": "Verbal",
        "topic": "Fill in the Blanks",
        "difficulty": "Medium",
        "question": "The scientific panel reached a _____ after three days of vigorous debate.",
        "options": [
            "stalemate",
            "consensus",
            "dichotomy",
            "divergence"
        ],
        "correct_answer": 1,
        "formula": "Consensus = general agreement.",
        "explanation": "Reaching general agreement among members of a panel is reaching a 'consensus'."
    },
    {
        "id": "verbal-idiom-7",
        "category": "Verbal",
        "topic": "Idioms & Phrases",
        "difficulty": "Medium",
        "question": "What is the meaning of 'Call it a day'?",
        "options": [
            "To name a calendar date",
            "To stop working on something for the remainder of the day",
            "To declare bankruptcy",
            "To wake up early"
        ],
        "correct_answer": 1,
        "formula": "Workplace colloquial idiom.",
        "explanation": "'To call it a day' means to conclude one's active work for the rest of the day."
    },
    {
        "id": "verbal-oneword-7",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Medium",
        "question": "A place where government or historical records are preserved is an:",
        "options": [
            "Archive",
            "Museum",
            "Library",
            "Arsenal"
        ],
        "correct_answer": 0,
        "formula": "Archive = repository of historical documents.",
        "explanation": "An 'Archive' is a collection of historical documents or records providing information about a place or institution."
    },
    {
        "id": "verbal-oneword-8",
        "category": "Verbal",
        "topic": "One Word Substitution",
        "difficulty": "Hard",
        "question": "One who hates or distrusts humankind is a:",
        "options": [
            "Philanthropist",
            "Misanthrope",
            "Misogynist",
            "Altruist"
        ],
        "correct_answer": 1,
        "formula": "Miso (hate) + anthropos (human).",
        "explanation": "A 'Misanthrope' dislikes or distrusts human society."
    },
    {
        "id": "verbal-vocab-14",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Medium",
        "question": "Select the synonym of 'AUGMENT':",
        "options": [
            "Decrease",
            "Increase",
            "Diminish",
            "Halt"
        ],
        "correct_answer": 1,
        "formula": "Augment = make greater in size or value.",
        "explanation": "'Augment' means to enlarge, expand, or increase."
    },
    {
        "id": "verbal-vocab-15",
        "category": "Verbal",
        "topic": "Synonyms & Antonyms",
        "difficulty": "Easy",
        "question": "Select the antonym of 'CONCEAL':",
        "options": [
            "Reveal",
            "Hide",
            "Cover",
            "Mask"
        ],
        "correct_answer": 0,
        "formula": "Conceal = keep secret or hidden. Antonym = Reveal.",
        "explanation": "The opposite of concealing something is to 'Reveal' or uncover it."
    },
    {
        "id": "verbal-grammar-10",
        "category": "Verbal",
        "topic": "Sentence Correction",
        "difficulty": "Easy",
        "question": "Choose the correct pronoun: 'Between you and _____, the proposal looks promising.'",
        "options": [
            "I",
            "me",
            "myself",
            "mine"
        ],
        "correct_answer": 1,
        "formula": "Prepositions ('between') require objective case pronouns ('me').",
        "explanation": "'Between' is a preposition, and objects of prepositions must be in the objective case ('me', not 'I')."
    },
    {
        "id": "verbal-parajumble-3",
        "category": "Verbal",
        "topic": "Para Jumbles",
        "difficulty": "Medium",
        "question": "Rearrange into a coherent paragraph:\nP: It helps build trust and credibility.\nQ: Honesty is the foundation of enduring interpersonal relationships.\nR: Without it, communication breaks down over time.\nS: When people are truthful, conflicts are resolved faster.",
        "options": [
            "Q-P-S-R",
            "Q-S-P-R",
            "P-Q-S-R",
            "S-Q-P-R"
        ],
        "correct_answer": 0,
        "formula": "Topic sentence (Q) -> primary benefit (P) -> specific manifestation (S) -> negative consequence of absence (R).",
        "explanation": "Q introduces honesty in relationships. P states the benefit of trust. S shows how truth resolves conflict. R concludes with the consequence of its absence."
    },
    {
        "id": "tech-dsa-1",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Easy",
        "question": "What is the worst-case time complexity of searching an element in a balanced Binary Search Tree (AVL / Red-Black Tree)?",
        "options": [
            "O(1)",
            "O(log N)",
            "O(N)",
            "O(N log N)"
        ],
        "correct_answer": 1,
        "formula": "Height of a balanced BST with N nodes is bounded by O(log N).",
        "explanation": "In a balanced BST, height is strictly maintained as O(log N), guaranteeing that search, insertion, and deletion operate in O(log N) worst-case time."
    },
    {
        "id": "tech-dsa-2",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "Which data structure is primarily used in the implementation of Breadth-First Search (BFS) on a graph?",
        "options": [
            "Stack",
            "Queue",
            "Heap",
            "Hash Table"
        ],
        "correct_answer": 1,
        "formula": "BFS visits vertices level-by-level using FIFO principle.",
        "explanation": "BFS uses a Queue (First-In-First-Out) to explore nodes in concentric wavefronts. DFS on the other hand utilizes a Stack (or call stack recursion)."
    },
    {
        "id": "tech-dsa-3",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "What is the average time complexity of lookup, insert, and delete operations in a Hash Map with a good hash function?",
        "options": [
            "O(1)",
            "O(log N)",
            "O(N)",
            "O(N\u00b2)"
        ],
        "correct_answer": 0,
        "formula": "Direct hash table addressing with uniform bucket distribution yields O(1) average time.",
        "explanation": "Hash tables compute keys via hashing in constant time O(1) on average. In degenerate collision cases, it can degrade to O(N)."
    },
    {
        "id": "tech-dsa-4",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Easy",
        "question": "Which data structure follows the LIFO (Last-In, First-Out) principle?",
        "options": [
            "Queue",
            "Stack",
            "Array",
            "Linked List"
        ],
        "correct_answer": 1,
        "formula": "LIFO = Last In, First Out.",
        "explanation": "A Stack operates on LIFO semantics (push and pop at top). Queue operates on FIFO."
    },
    {
        "id": "tech-dsa-5",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Hard",
        "question": "Which of the following operations takes O(1) time in a Min-Heap data structure?",
        "options": [
            "Find Minimum",
            "Extract Minimum",
            "Insert an element",
            "Delete an arbitrary node"
        ],
        "correct_answer": 0,
        "formula": "In a Min-Heap, the root element is always the minimum: index 0.",
        "explanation": "Finding minimum is simply reading root element array[0] in O(1). Extracting minimum requires heapify which takes O(log N)."
    },
    {
        "id": "tech-dsa-6",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "In a singly linked list with N nodes, what is the time complexity to insert a new node at the very beginning (head)?",
        "options": [
            "O(1)",
            "O(log N)",
            "O(N)",
            "O(N log N)"
        ],
        "correct_answer": 0,
        "formula": "newNode.next = head; head = newNode.",
        "explanation": "Prepend operation only reassigns pointer references at the head, taking constant O(1) time."
    },
    {
        "id": "tech-algo-1",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Easy",
        "question": "What is the average time complexity of Merge Sort?",
        "options": [
            "O(N)",
            "O(N log N)",
            "O(N\u00b2)",
            "O(log N)"
        ],
        "correct_answer": 1,
        "formula": "Divide and conquer recurrence: T(N) = 2T(N/2) + O(N) => O(N log N).",
        "explanation": "Merge sort divides arrays into halves and merges in linear time, guaranteeing O(N log N) in best, average, and worst cases."
    },
    {
        "id": "tech-algo-2",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Medium",
        "question": "What is the worst-case time complexity of QuickSort when using a naive pivot selection (e.g., always choosing the first element)?",
        "options": [
            "O(N log N)",
            "O(N\u00b2)",
            "O(N)",
            "O(2^N)"
        ],
        "correct_answer": 1,
        "formula": "Unbalanced partitions: N + (N-1) + ... + 1 = O(N\u00b2).",
        "explanation": "When an array is already sorted and the first element is selected as pivot, partitions are maximally unbalanced, yielding O(N\u00b2) worst-case runtime."
    },
    {
        "id": "tech-algo-3",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Medium",
        "question": "Which algorithm design paradigm is utilized by Dijkstra's Shortest Path algorithm for non-negative edge weights?",
        "options": [
            "Greedy Algorithm",
            "Dynamic Programming",
            "Backtracking",
            "Divide and Conquer"
        ],
        "correct_answer": 0,
        "formula": "Greedy choice property: picks the globally closest unvisited vertex at each step.",
        "explanation": "Dijkstra's algorithm greedily chooses the unvisited vertex with the minimum tentative distance at each iteration."
    },
    {
        "id": "tech-algo-4",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Hard",
        "question": "What is the time complexity of the Floyd-Warshall algorithm for finding all-pairs shortest paths on a graph with V vertices?",
        "options": [
            "O(V)",
            "O(V\u00b2)",
            "O(V\u00b3)",
            "O(E log V)"
        ],
        "correct_answer": 2,
        "formula": "Three nested loops over all vertices: V * V * V.",
        "explanation": "Floyd-Warshall tests whether vertex k offers a shorter path between all pairs (i, j), requiring three nested loops from 1 to V, running in O(V\u00b3)."
    },
    {
        "id": "tech-os-1",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Easy",
        "question": "Which of the following conditions is NOT required for a deadlock to occur in an operating system?",
        "options": [
            "Mutual Exclusion",
            "Hold and Wait",
            "Preemption Allowed",
            "Circular Wait"
        ],
        "correct_answer": 2,
        "formula": "Coffman conditions for deadlock: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait.",
        "explanation": "Deadlock requires NO preemption (resources cannot be forcibly taken away). If preemption is allowed, deadlocks can be broken."
    },
    {
        "id": "tech-os-2",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "What is the phenomenon where the page fault rate increases even when more physical page frames are allocated to a process?",
        "options": [
            "Thrashing",
            "B\u00e9l\u00e1dy's Anomaly",
            "Starvation",
            "Fragmentation"
        ],
        "correct_answer": 1,
        "formula": "B\u00e9l\u00e1dy's anomaly specifically occurs in FIFO page replacement algorithm.",
        "explanation": "B\u00e9l\u00e1dy's Anomaly is the counter-intuitive phenomenon in FIFO page replacement where increasing page frames causes more page faults."
    },
    {
        "id": "tech-os-3",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "What is 'Thrashing' in an Operating System?",
        "options": [
            "A process spending excessive CPU time on memory page swapping rather than actual execution",
            "A fast CPU scheduling technique",
            "Hardware disk head crash",
            "A method to encrypt virtual memory"
        ],
        "correct_answer": 0,
        "formula": "Thrashing occurs when high degree of multiprogramming causes page faults to dominate CPU cycles.",
        "explanation": "Thrashing is a state where the system spends more time servicing page faults and swapping pages in/out of secondary storage than executing instructions."
    },
    {
        "id": "tech-os-4",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Easy",
        "question": "Which CPU scheduling algorithm gives the minimum average waiting time for a given set of processes?",
        "options": [
            "First-Come, First-Served (FCFS)",
            "Shortest Job First (SJF / SRTF)",
            "Round Robin (RR)",
            "Priority Scheduling"
        ],
        "correct_answer": 1,
        "formula": "SJF is provably optimal with respect to minimum average waiting time.",
        "explanation": "Shortest Job First schedules shorter burst jobs first, mathematically minimizing average waiting time."
    },
    {
        "id": "tech-os-5",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "What is a 'Semaphore' primarily used for in concurrent programming?",
        "options": [
            "Process synchronization and managing access to shared critical sections",
            "Allocating virtual memory frames",
            "Compressing swap files",
            "Routing network packets between sockets"
        ],
        "correct_answer": 0,
        "formula": "Dijkstra's semaphore with wait() [P] and signal() [V] primitives.",
        "explanation": "A semaphore is a synchronization primitive used to prevent race conditions by controlling access to shared resources in concurrent systems."
    },
    {
        "id": "tech-dbms-1",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Easy",
        "question": "Which normal form deals with eliminating transitive functional dependencies in a relational table?",
        "options": [
            "First Normal Form (1NF)",
            "Second Normal Form (2NF)",
            "Third Normal Form (3NF)",
            "Boyce-Codd Normal Form (BCNF)"
        ],
        "correct_answer": 2,
        "formula": "3NF requires 2NF + No non-prime attribute is transitively dependent on candidate keys.",
        "explanation": "Third Normal Form (3NF) removes transitive dependencies (e.g. if A -> B and B -> C, where A is the key, C depends transitively on A)."
    },
    {
        "id": "tech-dbms-2",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Medium",
        "question": "In ACID properties of a database transaction, which property guarantees that either all operations of the transaction are completed or none are?",
        "options": [
            "Atomicity",
            "Consistency",
            "Isolation",
            "Durability"
        ],
        "correct_answer": 0,
        "formula": "Atomicity = 'All or nothing' execution.",
        "explanation": "Atomicity ensures that all changes within a transaction boundary are committed, or if any fails, the entire transaction is rolled back."
    },
    {
        "id": "tech-dbms-3",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Medium",
        "question": "Which SQL clause is used to filter groups created by the 'GROUP BY' clause?",
        "options": [
            "WHERE",
            "HAVING",
            "ORDER BY",
            "FILTER"
        ],
        "correct_answer": 1,
        "formula": "WHERE filters rows before grouping; HAVING filters aggregate groups after grouping.",
        "explanation": "The 'HAVING' clause filters summarized or grouped records based on aggregate functions (e.g. HAVING COUNT(*) > 5)."
    },
    {
        "id": "tech-dbms-4",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Hard",
        "question": "What is a 'Phantom Read' anomaly in database transaction isolation levels?",
        "options": [
            "A transaction reads updated data that has not yet been committed",
            "A transaction re-reads a row and finds that another transaction modified values",
            "A transaction re-executes a query returning a set of rows satisfying a condition and finds new rows inserted by another committed transaction",
            "A transaction permanently loses its commit log"
        ],
        "correct_answer": 2,
        "formula": "Phantom Read: new qualifying rows appear in range queries. Prevented by SERIALIZABLE isolation.",
        "explanation": "A phantom read occurs when new rows inserted by another committed transaction appear during range scans within an active transaction."
    },
    {
        "id": "tech-dbms-5",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Easy",
        "question": "Which SQL command is classified as Data Definition Language (DDL)?",
        "options": [
            "SELECT",
            "INSERT",
            "CREATE",
            "UPDATE"
        ],
        "correct_answer": 2,
        "formula": "DDL includes CREATE, ALTER, DROP, TRUNCATE.",
        "explanation": "CREATE defines or alters the database schema structure, classifying it as DDL. SELECT and INSERT are DML/DQL."
    },
    {
        "id": "tech-cn-1",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "At which layer of the OSI model does the TCP (Transmission Control Protocol) operate?",
        "options": [
            "Network Layer",
            "Transport Layer",
            "Data Link Layer",
            "Application Layer"
        ],
        "correct_answer": 1,
        "formula": "Layer 4 = Transport Layer (TCP, UDP).",
        "explanation": "TCP and UDP are Transport Layer (Layer 4) protocols responsible for end-to-end communication, reliability, flow control, and port multiplexing."
    },
    {
        "id": "tech-cn-2",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Easy",
        "question": "What is the primary function of the Domain Name System (DNS)?",
        "options": [
            "Encrypt network traffic across routers",
            "Translate human-friendly domain names (e.g. google.com) into numeric IP addresses",
            "Allocate local IP addresses dynamically to devices",
            "Filter malicious incoming packets like a firewall"
        ],
        "correct_answer": 1,
        "formula": "DNS = Internet telephone directory resolving hostnames to IP addresses.",
        "explanation": "DNS translates domain names like example.com into machine-readable IP addresses (e.g., 93.184.216.34)."
    },
    {
        "id": "tech-cn-3",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "How many packets are exchanged in the standard TCP connection establishment handshake?",
        "options": [
            "2 packets",
            "3 packets (SYN, SYN-ACK, ACK)",
            "4 packets",
            "5 packets"
        ],
        "correct_answer": 1,
        "formula": "TCP 3-Way Handshake: Client -> SYN, Server -> SYN-ACK, Client -> ACK.",
        "explanation": "TCP establishes a reliable connection using a 3-way handshake: SYN from client, SYN-ACK from server, and ACK from client."
    },
    {
        "id": "tech-cn-4",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Hard",
        "question": "What protocol is used by network hosts to map a known IP address to its corresponding physical MAC address on a local area network?",
        "options": [
            "DNS",
            "DHCP",
            "ARP (Address Resolution Protocol)",
            "ICMP"
        ],
        "correct_answer": 2,
        "formula": "ARP maps Layer 3 IPv4 addresses to Layer 2 MAC addresses.",
        "explanation": "ARP broadcasts queries to resolve an IP address to a hardware MAC address for frame delivery over local Ethernet/Wi-Fi."
    },
    {
        "id": "tech-oop-1",
        "category": "Technical",
        "topic": "Object-Oriented Programming",
        "difficulty": "Easy",
        "question": "Which OOP principle allows a subclass to provide a specific implementation of a method that is already defined in its superclass?",
        "options": [
            "Method Overloading",
            "Method Overriding (Dynamic Polymorphism)",
            "Encapsulation",
            "Data Abstraction"
        ],
        "correct_answer": 1,
        "formula": "Dynamic binding / runtime polymorphism via method overriding.",
        "explanation": "Method Overriding occurs when a child class provides its own implementation of a method inherited from its parent class."
    },
    {
        "id": "tech-oop-2",
        "category": "Technical",
        "topic": "Object-Oriented Programming",
        "difficulty": "Medium",
        "question": "In the SOLID design principles, what does the 'L' stand for?",
        "options": [
            "Linear Responsibility Principle",
            "Liskov Substitution Principle",
            "Lazy Evaluation Principle",
            "Logic Decoupling Principle"
        ],
        "correct_answer": 1,
        "formula": "SOLID: Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion.",
        "explanation": "Liskov Substitution Principle states that subtypes must be substitutable for their base types without altering program correctness."
    },
    {
        "id": "tech-oop-3",
        "category": "Technical",
        "topic": "Object-Oriented Programming",
        "difficulty": "Easy",
        "question": "What is the mechanism of bundling data together with the methods that operate on that data called?",
        "options": [
            "Inheritance",
            "Polymorphism",
            "Encapsulation",
            "Coupling"
        ],
        "correct_answer": 2,
        "formula": "Encapsulation = Data hiding + bundling methods and state within a class.",
        "explanation": "Encapsulation bundles data attributes and methods together while restricting direct unauthorized outside access."
    },
    {
        "id": "tech-oop-4",
        "category": "Technical",
        "topic": "Object-Oriented Programming",
        "difficulty": "Medium",
        "question": "Which design pattern ensures that a class has only one instance and provides a global point of access to it?",
        "options": [
            "Factory Pattern",
            "Singleton Pattern",
            "Observer Pattern",
            "Strategy Pattern"
        ],
        "correct_answer": 1,
        "formula": "Gang of Four Singleton Creational Design Pattern.",
        "explanation": "The Singleton pattern restricts instantiation of a class to a single object and provides a global access method."
    },
    {
        "id": "tech-dsa-7",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Hard",
        "question": "What is the maximum number of nodes in a binary tree of height 'h' (where a tree with only root has height 0)?",
        "options": [
            "2^h",
            "2^(h+1) - 1",
            "2^h - 1",
            "h\u00b2"
        ],
        "correct_answer": 1,
        "formula": "Sum of geometric series: 2^0 + 2^1 + ... + 2^h = 2^(h+1) - 1.",
        "explanation": "At depth i, maximum nodes = 2^i. Sum over i=0 to h is 2^(h+1) - 1."
    },
    {
        "id": "tech-dsa-8",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "Which data structure is best suited for checking whether parentheses in an algebraic expression are balanced?",
        "options": [
            "Queue",
            "Stack",
            "Binary Tree",
            "Linked List"
        ],
        "correct_answer": 1,
        "formula": "Push opening brackets, pop on matching closing bracket.",
        "explanation": "A Stack allows tracking the most recently opened bracket so that it can be matched with the next closing bracket."
    },
    {
        "id": "tech-algo-5",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Easy",
        "question": "What is the time complexity of Binary Search on a sorted array of N elements?",
        "options": [
            "O(1)",
            "O(log N)",
            "O(N)",
            "O(N log N)"
        ],
        "correct_answer": 1,
        "formula": "T(N) = T(N/2) + O(1) => O(log N).",
        "explanation": "Binary search halves the search range at every step, yielding logarithmic O(log N) time complexity."
    },
    {
        "id": "tech-algo-6",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Hard",
        "question": "What is the space complexity of standard Depth-First Search (DFS) on a tree of maximum depth 'd'?",
        "options": [
            "O(1)",
            "O(d)",
            "O(N\u00b2)",
            "O(2^d)"
        ],
        "correct_answer": 1,
        "formula": "Call stack depth is bounded by tree height d.",
        "explanation": "DFS only maintains nodes along the current recursion branch, requiring O(d) memory where d is the maximum depth."
    },
    {
        "id": "tech-os-6",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "What is a 'Context Switch' in an Operating System?",
        "options": [
            "Saving the state of the currently executing process and loading the state of another process to CPU registers",
            "Swapping memory to secondary storage",
            "Changing user account permissions",
            "Compiling source code to machine code"
        ],
        "correct_answer": 0,
        "formula": "CPU state preservation in PCB (Process Control Block).",
        "explanation": "A context switch stores the register state/program counter of the old process and restores the state of the newly scheduled process."
    },
    {
        "id": "tech-os-7",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Hard",
        "question": "Which memory allocation policy searches the entire list of free holes and allocates the smallest hole that is big enough to satisfy the request?",
        "options": [
            "First-Fit",
            "Best-Fit",
            "Worst-Fit",
            "Next-Fit"
        ],
        "correct_answer": 1,
        "formula": "Best-fit minimizes leftover fragment size for each allocation.",
        "explanation": "Best-fit searches all free blocks to find the smallest block that fits the requested size, minimizing immediate wasted space."
    },
    {
        "id": "tech-dbms-6",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Medium",
        "question": "Which type of SQL JOIN returns all records from the left table and matched records from the right table, filling with NULL where no match exists?",
        "options": [
            "INNER JOIN",
            "LEFT OUTER JOIN",
            "RIGHT OUTER JOIN",
            "CROSS JOIN"
        ],
        "correct_answer": 1,
        "formula": "LEFT JOIN keeps all rows of Table A unconditionally.",
        "explanation": "A LEFT OUTER JOIN preserves all rows from the left table regardless of whether there is a matching row in the right table."
    },
    {
        "id": "tech-dbms-7",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Easy",
        "question": "What is the purpose of a PRIMARY KEY in a relational database table?",
        "options": [
            "Uniquely identifies each record and enforces non-null constraint",
            "Enables faster multiplication operations",
            "Allows duplicate values for historical logging",
            "Encrypts column contents automatically"
        ],
        "correct_answer": 0,
        "formula": "Primary Key = UNIQUE + NOT NULL constraint.",
        "explanation": "A Primary Key uniquely identifies each row in a table and cannot contain null values."
    },
    {
        "id": "tech-cn-5",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Easy",
        "question": "Which of the following ports is the default port for HTTPS (Secure HyperText Transfer Protocol)?",
        "options": [
            "21",
            "80",
            "443",
            "8080"
        ],
        "correct_answer": 2,
        "formula": "Standard IANA well-known ports: HTTP=80, HTTPS=443, FTP=21, SSH=22.",
        "explanation": "Port 443 is the standard TCP port for secure web traffic encrypted with TLS/SSL."
    },
    {
        "id": "tech-cn-6",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "Which protocol is connectionless and does not guarantee packet delivery order or retransmission?",
        "options": [
            "TCP",
            "UDP",
            "FTP",
            "SMTP"
        ],
        "correct_answer": 1,
        "formula": "User Datagram Protocol (UDP) provides low-overhead, best-effort datagram transport.",
        "explanation": "UDP sends datagrams without establishing a handshake or verifying receipt, prioritizing speed over reliability."
    },
    {
        "id": "tech-oop-5",
        "category": "Technical",
        "topic": "Object-Oriented Programming",
        "difficulty": "Medium",
        "question": "What is the key difference between an Abstract Class and an Interface in modern Java/C#?",
        "options": [
            "An abstract class can maintain state (instance fields and constructors), whereas an interface cannot hold state",
            "Interfaces can be instantiated directly",
            "Abstract classes cannot have any concrete methods",
            "Classes can inherit from multiple abstract classes"
        ],
        "correct_answer": 0,
        "formula": "Multiple interface implementation vs single abstract class inheritance with state.",
        "explanation": "Abstract classes can hold instance variables and constructors. A class can inherit only one abstract class but can implement multiple interfaces."
    },
    {
        "id": "tech-swe-1",
        "category": "Technical",
        "topic": "Software Engineering",
        "difficulty": "Easy",
        "question": "In Git version control, which command is used to combine changes from one branch into another?",
        "options": [
            "git push",
            "git merge",
            "git commit",
            "git clone"
        ],
        "correct_answer": 1,
        "formula": "git merge <branch> integrates independent development histories.",
        "explanation": "'git merge' takes changes from a target branch and integrates them into the active branch."
    },
    {
        "id": "tech-swe-2",
        "category": "Technical",
        "topic": "Software Engineering",
        "difficulty": "Medium",
        "question": "In RESTful API design, which HTTP method is considered 'idempotent'?",
        "options": [
            "POST",
            "PUT",
            "PATCH",
            "CONNECT"
        ],
        "correct_answer": 1,
        "formula": "Idempotent: f(f(x)) = f(x). Multiple identical requests produce the same server resource state.",
        "explanation": "PUT, GET, and DELETE are idempotent according to HTTP specs; calling PUT multiple times with the same payload results in the exact same resource state."
    },
    {
        "id": "tech-dsa-9",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "Which collision resolution technique in hash tables stores collided elements in a linked list attached to the bucket index?",
        "options": [
            "Linear Probing",
            "Quadratic Probing",
            "Separate Chaining",
            "Double Hashing"
        ],
        "correct_answer": 2,
        "formula": "Separate Chaining: bucket[i] points to head of linked list.",
        "explanation": "Separate chaining resolves hash collisions by maintaining a linked list (or small tree) of entries for each bucket slot."
    },
    {
        "id": "tech-algo-7",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Medium",
        "question": "Which algorithmic technique solves subproblems only once and stores their solutions in a table to avoid redundant calculations?",
        "options": [
            "Dynamic Programming",
            "Greedy Approach",
            "Brute Force",
            "Monte Carlo Method"
        ],
        "correct_answer": 0,
        "formula": "Optimal substructure + Overlapping subproblems with memoization/tabulation.",
        "explanation": "Dynamic Programming optimizes recursive algorithms by caching overlapping subproblem results."
    },
    {
        "id": "tech-os-8",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Easy",
        "question": "What is a 'Thread' in an Operating System?",
        "options": [
            "A lightweight unit of CPU execution sharing the same address space as its parent process",
            "A physical copper wire inside CPU",
            "A type of hard disk partition",
            "A network firewall rule"
        ],
        "correct_answer": 0,
        "formula": "Threads share text, data, and OS resources, but maintain separate stacks and registers.",
        "explanation": "A thread is the smallest schedulable execution entity that shares memory and heap with peer threads within the same process."
    },
    {
        "id": "tech-dbms-8",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Medium",
        "question": "What is the primary purpose of creating a B-Tree index on a table column?",
        "options": [
            "Speeding up data retrieval queries (SELECT) at the cost of slight overhead on INSERT/UPDATE",
            "Compressing table data on disk",
            "Encrypting values",
            "Preventing table deletion"
        ],
        "correct_answer": 0,
        "formula": "B-Tree index allows logarithmic O(log N) lookup time for equality and range queries.",
        "explanation": "Indexes drastically accelerate search lookups and sorting, though they require maintenance on writes."
    },
    {
        "id": "tech-cn-7",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Hard",
        "question": "What is the usable number of host IP addresses available in a /24 IPv4 subnet (subnet mask 255.255.255.0)?",
        "options": [
            "254",
            "255",
            "256",
            "128"
        ],
        "correct_answer": 0,
        "formula": "Usable hosts = 2^(32 - prefix) - 2 (subtracting network and broadcast addresses).",
        "explanation": "2^(32 - 24) = 2^8 = 256. Subtracting network ID (.0) and broadcast address (.255) leaves 254 usable host addresses."
    },
    {
        "id": "tech-oop-6",
        "category": "Technical",
        "topic": "Object-Oriented Programming",
        "difficulty": "Hard",
        "question": "What problem does the 'Dependency Injection' design pattern solve?",
        "options": [
            "It decouples the creation of a client's dependencies from the client's behavior, improving testability and modularity",
            "It replaces inheritance with pointers",
            "It prevents database deadlocks",
            "It accelerates garbage collection"
        ],
        "correct_answer": 0,
        "formula": "Inversion of Control (IoC) principle.",
        "explanation": "Dependency Injection supplies objects (services) to dependent clients from the outside, enabling loose coupling and easy unit test mocking."
    },
    {
        "id": "tech-dsa-10",
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "What is the topological sort of a graph applicable to?",
        "options": [
            "Directed Acyclic Graphs (DAG)",
            "Undirected Graphs with cycles",
            "Any complete graph",
            "Bipartite graphs with cycles only"
        ],
        "correct_answer": 0,
        "formula": "Topological ordering requires absence of directed cycles.",
        "explanation": "Topological sorting linearly orders vertices such that for every directed edge u -> v, u comes before v. This is only possible in DAGs."
    },
    {
        "id": "tech-algo-8",
        "category": "Technical",
        "topic": "Algorithms",
        "difficulty": "Easy",
        "question": "Which algorithm is used to detect cycles in a linked list with O(1) auxiliary space?",
        "options": [
            "Floyd's Tortoise and Hare Cycle-Finding Algorithm",
            "Dijkstra's Algorithm",
            "Kruskal's Algorithm",
            "Rabin-Karp Algorithm"
        ],
        "correct_answer": 0,
        "formula": "Fast pointer (2 steps) and slow pointer (1 step) pointer traversal.",
        "explanation": "Floyd's cycle-finding algorithm uses two pointers moving at different speeds to detect a loop in O(N) time and O(1) space."
    },
    {
        "id": "tech-os-9",
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "Which page replacement algorithm is theoretically optimal but impossible to implement in practice?",
        "options": [
            "Optimal Page Replacement (OPT / B\u00e9l\u00e1dy's Algorithm)",
            "Least Recently Used (LRU)",
            "First-In First-Out (FIFO)",
            "Clock Algorithm"
        ],
        "correct_answer": 0,
        "formula": "Replaces the page that will not be used for the longest period in future.",
        "explanation": "The OPT algorithm requires future knowledge of reference strings, serving as an ideal benchmark rather than a practical system algorithm."
    },
    {
        "id": "tech-dbms-9",
        "category": "Technical",
        "topic": "DBMS & SQL",
        "difficulty": "Hard",
        "question": "In a relational database, what is a 'Foreign Key'?",
        "options": [
            "A column in one table that references the primary key of another table, enforcing referential integrity",
            "A key generated by external third-party software",
            "An index stored on a remote server",
            "A temporary key discarded on transaction commit"
        ],
        "correct_answer": 0,
        "formula": "Referential integrity constraint.",
        "explanation": "A Foreign Key establishes a relational link between two tables, ensuring referenced records must exist."
    },
    {
        "id": "tech-cn-8",
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "What is the maximum data payload size (MTU) for standard Ethernet frames?",
        "options": [
            "512 bytes",
            "1024 bytes",
            "1500 bytes",
            "4096 bytes"
        ],
        "correct_answer": 2,
        "formula": "Standard Ethernet Maximum Transmission Unit (MTU) is 1500 bytes.",
        "explanation": "The standard Ethernet MTU is 1500 bytes (excluding the 14-byte Ethernet header and 4-byte CRC trailer)."
    },
    {
        "id": "tech-swe-3",
        "category": "Technical",
        "topic": "Software Engineering",
        "difficulty": "Medium",
        "question": "What is the primary purpose of an In-Memory Cache like Redis in high-scale web applications?",
        "options": [
            "Sub-millisecond access to frequently read data, dramatically reducing load on the primary relational database",
            "Permanent archival storage of historical logs",
            "Compiling JavaScript into WebAssembly",
            "Replacing SSL certificates"
        ],
        "correct_answer": 0,
        "formula": "In-memory key-value caching layer with fast RAM access.",
        "explanation": "Caches like Redis store hot data in RAM, shielding databases from repetitive slow disk queries."
    }
]

def get_all_aptitude_questions():
    """Returns all aptitude questions"""
    return APTITUDE_QUESTIONS

def get_aptitude_categories():
    """Returns summary of available categories, topics and question counts"""
    cats = {}
    for q in APTITUDE_QUESTIONS:
        cat = q["category"]
        topic = q["topic"]
        if cat not in cats:
            cats[cat] = {"count": 0, "topics": set()}
        cats[cat]["count"] += 1
        cats[cat]["topics"].add(topic)
    
    result = []
    for cat, data in cats.items():
        result.append({
            "category": cat,
            "total_questions": data["count"],
            "topics": sorted(list(data["topics"]))
        })
    return result

def filter_aptitude_questions(category=None, topic=None, difficulty=None, mode="practice", limit=50, shuffle=True):
    """
    Returns filtered aptitude questions.
    - If shuffle is True (or in practice mode without explicit False), questions are randomized
      so users receive fresh questions on every practice session.
    - If limit is provided, returns up to limit questions (e.g. 45-50 questions).
    - If mode == 'test', strips sensitive fields (correct_answer, formula, explanation).
    """
    results = [q for q in APTITUDE_QUESTIONS]
    
    if category and category.lower() != "all":
        results = [q for q in results if q["category"].lower() == category.lower()]
    if topic and topic.lower() != "all":
        results = [q for q in results if q["topic"].lower() == topic.lower()]
    if difficulty and difficulty.lower() != "all":
        results = [q for q in results if q["difficulty"].lower() == difficulty.lower()]

    if shuffle:
        # Create a randomized copy so questions change every time
        results = list(results)
        random.shuffle(results)

    if limit and limit > 0:
        results = results[:limit]

    if mode == "test":
        sanitized = []
        for q in results:
            item = dict(q)
            item.pop("correct_answer", None)
            item.pop("explanation", None)
            item.pop("formula", None)
            sanitized.append(item)
        return sanitized

    return results

def generate_random_aptitude_test(total_count=20):
    """Generates a balanced timed aptitude test across all 4 domains (supports up to 50 questions)"""
    by_category = {}
    for q in APTITUDE_QUESTIONS:
        by_category.setdefault(q["category"], []).append(q)

    per_cat = max(2, total_count // len(by_category))
    selected = []
    for cat, q_list in by_category.items():
        sample_size = min(len(q_list), per_cat)
        selected.extend(random.sample(q_list, sample_size))

    # If count is still less, sample remaining from overall pool
    if len(selected) < total_count:
        remaining_pool = [q for q in APTITUDE_QUESTIONS if q not in selected]
        needed = total_count - len(selected)
        selected.extend(random.sample(remaining_pool, min(needed, len(remaining_pool))))

    random.shuffle(selected)
    
    # Sanitize for test execution
    test_questions = []
    for q in selected:
        item = dict(q)
        item.pop("correct_answer", None)
        item.pop("explanation", None)
        item.pop("formula", None)
        test_questions.append(item)

    return {
        "test_id": f"apt-{random.randint(10000, 99999)}",
        "total_questions": len(test_questions),
        "duration_minutes": max(10, len(test_questions)),
        "questions": test_questions
    }

def evaluate_aptitude_test(answers_map):
    """
    Evaluates user answers.
    answers_map: { "quant-time-work-1": 1, "logic-series-1": 2, ... }
    Returns comprehensive score breakdown, section accuracy, and step-by-step explanations.
    """
    answered_count = len(answers_map)
    correct_count = 0
    incorrect_count = 0

    section_breakdown = {
        "Quantitative": {"total": 0, "correct": 0, "score": 0},
        "Logical": {"total": 0, "correct": 0, "score": 0},
        "Verbal": {"total": 0, "correct": 0, "score": 0},
        "Technical": {"total": 0, "correct": 0, "score": 0}
    }

    detailed_results = []

    # Map all questions by ID
    q_map = {q["id"]: q for q in APTITUDE_QUESTIONS}

    for q_id, user_choice in answers_map.items():
        q = q_map.get(q_id)
        if not q:
            continue

        cat = q["category"]
        if cat in section_breakdown:
            section_breakdown[cat]["total"] += 1

        is_correct = (int(user_choice) == int(q["correct_answer"])) if user_choice is not None else False
        if is_correct:
            correct_count += 1
            if cat in section_breakdown:
                section_breakdown[cat]["correct"] += 1
        else:
            incorrect_count += 1

        detailed_results.append({
            "id": q["id"],
            "category": q["category"],
            "topic": q["topic"],
            "question": q["question"],
            "options": q["options"],
            "user_answer": user_choice,
            "correct_answer": q["correct_answer"],
            "is_correct": is_correct,
            "formula": q.get("formula", ""),
            "explanation": q.get("explanation", "")
        })

    # Calculate section percentages
    for cat, stats in section_breakdown.items():
        if stats["total"] > 0:
            stats["score"] = round((stats["correct"] / stats["total"]) * 100, 1)
        else:
            stats["score"] = 0.0

    total_submitted = max(1, len(detailed_results))
    overall_score = round((correct_count / total_submitted) * 100, 1)

    return {
        "total_questions": total_submitted,
        "answered_count": answered_count,
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "overall_score": overall_score,
        "section_breakdown": section_breakdown,
        "detailed_results": detailed_results
    }
