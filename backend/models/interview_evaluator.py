import re
import random
from backend.models.dataset_loader import dataset_loader
from backend.models.deep_answer_evaluator import deep_answer_evaluator

# Curated High-Yield Skill-Specific Question Library for Resume Deep-Dives
SKILL_QUESTION_BANK = {
    "python": {
        "Easy": [
            {
                "question": "Your resume highlights Python. Can you explain the difference between mutable and immutable data types in Python, and how memory references behave when passing them into functions?",
                "target_keywords": ["mutable", "immutable", "list", "tuple", "memory", "reference", "id", "shallow copy"],
                "category": "Python Fundamentals: Memory & Types"
            },
            {
                "question": "You listed Python on your resume. How do list comprehensions differ from generator expressions in terms of syntax, execution, and memory consumption?",
                "target_keywords": ["generator", "list comprehension", "yield", "memory", "lazy evaluation", "iteration"],
                "category": "Python Fundamentals: Generators & Iterators"
            }
        ],
        "Medium": [
            {
                "question": "Based on your Python experience on your resume, how do Python decorators work under the hood, and how have you used them for logging, authentication, or timing in your projects?",
                "target_keywords": ["decorator", "wrapper", "closure", "higher order function", "functools", "args", "kwargs"],
                "category": "Python Deep-Dive: Decorators & Closures"
            },
            {
                "question": "In your Python projects, how do you handle asynchronous programming with asyncio versus threading and multiprocessing? In what scenarios is each approach preferred?",
                "target_keywords": ["asyncio", "threading", "multiprocessing", "event loop", "coroutine", "cpu bound", "i/o bound"],
                "category": "Python Concurrency: Async & Multiprocessing"
            }
        ],
        "Hard": [
            {
                "question": "Your resume shows Python expertise. Can you discuss the Python Global Interpreter Lock (GIL)? How does it affect multithreaded CPU-bound tasks, and how do you bypass it using multiprocessing or C-extensions?",
                "target_keywords": ["gil", "global interpreter lock", "multiprocessing", "thread safety", "cpu bound", "cpython", "bytecode"],
                "category": "Python Core Architecture: GIL & Execution Engine"
            },
            {
                "question": "How does Python's memory management and garbage collection mechanism handle cyclic object references, and what tools do you use to diagnose memory leaks in long-running Python services?",
                "target_keywords": ["reference counting", "garbage collection", "cyclic references", "gc module", "tracemalloc", "objgraph"],
                "category": "Python Internals: Memory Management & Profiling"
            }
        ]
    },
    "javascript": {
        "Easy": [
            {
                "question": "Your resume includes JavaScript. Can you explain the difference between `var`, `let`, and `const`, and how variable hoisting and block scoping work in ES6+?",
                "target_keywords": ["scope", "hoisting", "temporal dead zone", "let", "const", "var", "block scope"],
                "category": "JavaScript Fundamentals: Scope & Hoisting"
            },
            {
                "question": "You list JavaScript in your technical stack. How do JavaScript Promises work, and how does `async/await` syntax improve error handling compared to traditional callback patterns?",
                "target_keywords": ["promise", "async", "await", "callback", "try catch", "resolve", "reject", "chaining"],
                "category": "JavaScript Fundamentals: Asynchronous Patterns"
            }
        ],
        "Medium": [
            {
                "question": "Based on your JavaScript background on your resume, explain how the JavaScript Event Loop coordinates the Call Stack, Microtask Queue (Promises), and Macrotask Queue (setTimeout/I/O).",
                "target_keywords": ["event loop", "call stack", "microtask", "macrotask", "queue", "promise", "execution"],
                "category": "JavaScript Runtime: Event Loop & Concurrency"
            },
            {
                "question": "How do JavaScript closures and lexical scoping function, and how have you used closures to implement data encapsulation or function memoization in your projects?",
                "target_keywords": ["closure", "lexical scope", "encapsulation", "memoization", "private variables", "state"],
                "category": "JavaScript Core: Closures & Scope Chain"
            }
        ],
        "Hard": [
            {
                "question": "Your resume highlights JavaScript. How does Prototypal Inheritance work in JavaScript engines (V8), and how do Hidden Classes and Inline Caching optimize property lookups at runtime?",
                "target_keywords": ["prototype", "inheritance", "v8", "hidden classes", "inline cache", "optimization", "prototype chain"],
                "category": "JavaScript Engine: V8 Optimization & Prototypes"
            }
        ]
    },
    "react": {
        "Easy": [
            {
                "question": "Your resume features React. Can you walk me through the lifecycle of a functional component using hooks like `useState` and `useEffect`, including dependency arrays and cleanup functions?",
                "target_keywords": ["useeffect", "usestate", "lifecycle", "cleanup", "dependencies", "mounting", "unmounting"],
                "category": "React Fundamentals: Component Lifecycle & Hooks"
            },
            {
                "question": "You mentioned React on your resume. What is the Virtual DOM, and why is React's synthetic event system used instead of native DOM events?",
                "target_keywords": ["virtual dom", "diffing", "reconciliation", "synthetic events", "performance", "batching"],
                "category": "React Architecture: Virtual DOM & Events"
            }
        ],
        "Medium": [
            {
                "question": "Based on the React experience on your resume, how do you diagnose and prevent unnecessary component re-renders using `React.memo`, `useMemo`, and `useCallback`?",
                "target_keywords": ["usememo", "usecallback", "react.memo", "re-render", "referential equality", "profiler", "optimization"],
                "category": "React Performance: Render Optimization"
            },
            {
                "question": "In your React projects, how do you handle state management across deeply nested components? When do you choose React Context versus external libraries like Redux Toolkit or Zustand?",
                "target_keywords": ["state management", "context api", "redux", "zustand", "prop drilling", "actions", "selectors"],
                "category": "React State Architecture: Context vs Redux"
            }
        ],
        "Hard": [
            {
                "question": "Your resume shows advanced React proficiency. Explain React 18 Concurrent Rendering, Suspense, and how transitions (`useTransition`, `useDeferredValue`) keep UI responsive during heavy updates.",
                "target_keywords": ["concurrent rendering", "suspense", "usetransition", "usedeferredvalue", "fiber", "interruption", "priority"],
                "category": "React Advanced: Concurrent Architecture & Fiber"
            }
        ]
    },
    "node.js": {
        "Easy": [
            {
                "question": "Your resume highlights Node.js. How does Node.js achieve high concurrency with a single-threaded JavaScript runtime using non-blocking asynchronous I/O?",
                "target_keywords": ["non-blocking", "event loop", "single thread", "libuv", "concurrency", "asynchronous", "i/o"],
                "category": "Node.js Fundamentals: Architecture & I/O"
            },
            {
                "question": "You list Node.js in your stack. How does Express middleware work, and how do you implement centralized error handling and request validation?",
                "target_keywords": ["middleware", "next", "error handling", "request", "response", "express", "pipeline"],
                "category": "Node.js & Express: Middleware Pipeline"
            }
        ],
        "Medium": [
            {
                "question": "Based on your Node.js experience, how do Node.js Streams and Buffers prevent memory overflows when handling large file uploads or video streaming?",
                "target_keywords": ["streams", "buffer", "pipe", "backpressure", "readable", "writable", "chunk", "memory"],
                "category": "Node.js Deep-Dive: Streams & Memory Management"
            },
            {
                "question": "In your Node.js applications, how do you manage secure authentication and session authorization using JWTs, bcrypt password hashing, and HTTP-only cookies?",
                "target_keywords": ["jwt", "bcrypt", "cookies", "tokens", "authentication", "authorization", "security"],
                "category": "Node.js Security: Authentication & JWTs"
            }
        ],
        "Hard": [
            {
                "question": "Your resume includes Node.js backend development. How do you scale Node.js applications across multiple CPU cores using the Cluster module or PM2, and how do you manage shared state and graceful shutdown?",
                "target_keywords": ["cluster", "pm2", "multi-core", "fork", "worker", "graceful shutdown", "ipc", "load balance"],
                "category": "Node.js Scalability: Clustering & Microservices"
            }
        ]
    },
    "sql": {
        "Easy": [
            {
                "question": "Your resume shows SQL expertise. Can you explain the difference between `INNER JOIN`, `LEFT JOIN`, and `FULL OUTER JOIN`, and when you would use `GROUP BY` with a `HAVING` clause?",
                "target_keywords": ["inner join", "left join", "group by", "having", "aggregate", "where", "table"],
                "category": "SQL Fundamentals: Joins & Aggregations"
            }
        ],
        "Medium": [
            {
                "question": "Based on your SQL experience on your resume, how do B-Tree indexes accelerate queries, and why can excessive indexing degrade write performance in OLTP systems?",
                "target_keywords": ["index", "b-tree", "query plan", "explain analyze", "write penalty", "table scan", "composite index"],
                "category": "SQL Optimization: Indexing & Query Plans"
            },
            {
                "question": "You list relational databases on your resume. Explain the ACID properties and how database transaction isolation levels prevent dirty reads, non-repeatable reads, and phantom reads.",
                "target_keywords": ["acid", "atomicity", "consistency", "isolation", "durability", "phantom read", "dirty read", "transactions"],
                "category": "SQL Database Design: ACID & Concurrency"
            }
        ],
        "Hard": [
            {
                "question": "In your database architecture experience, how do you handle database scaling through horizontal sharding, read replicas, connection pooling, and optimistic vs pessimistic locking?",
                "target_keywords": ["sharding", "read replica", "connection pool", "locking", "deadlock", "replication", "partitioning"],
                "category": "Database Architecture: Sharding & Replication"
            }
        ]
    },
    "mongodb": {
        "Easy": [
            {
                "question": "Your resume includes MongoDB. How does a document-oriented NoSQL database like MongoDB differ from a relational SQL database in schema design and data modeling?",
                "target_keywords": ["document", "json", "bson", "schema", "flexible", "collection", "nosql"],
                "category": "MongoDB Fundamentals: Document Data Modeling"
            }
        ],
        "Medium": [
            {
                "question": "Based on your MongoDB skills on your resume, how do you decide between embedding subdocuments versus referencing normalized documents with ObjectIDs, and how does the 16MB document limit factor in?",
                "target_keywords": ["embedding", "referencing", "objectid", "normalization", "16mb", "cardinality", "subdocument"],
                "category": "MongoDB Architecture: Embedding vs Referencing"
            },
            {
                "question": "In your MongoDB projects, walk me through how you build efficient Aggregation Pipelines using `$match`, `$group`, `$project`, and `$lookup`, ensuring proper index utilization.",
                "target_keywords": ["aggregation", "pipeline", "$match", "$group", "$lookup", "indexing", "performance"],
                "category": "MongoDB Deep-Dive: Aggregation Pipelines"
            }
        ],
        "Hard": [
            {
                "question": "Your resume shows MongoDB experience. How does MongoDB handle high availability and write consistency across replica sets using write concerns (`w: 'majority'`), journal commits, and raft election consensus?",
                "target_keywords": ["replica set", "write concern", "majority", "journaling", "election", "sharded cluster", "consistency"],
                "category": "MongoDB Distributed Systems: Replica Sets & Consensus"
            }
        ]
    },
    "machine learning": {
        "Easy": [
            {
                "question": "Your resume features Machine Learning. Can you explain the difference between Supervised, Unsupervised, and Reinforcement Learning, and how you evaluate a classification model using a Confusion Matrix?",
                "target_keywords": ["supervised", "unsupervised", "classification", "confusion matrix", "accuracy", "labels"],
                "category": "Machine Learning Fundamentals: Paradigms & Metrics"
            }
        ],
        "Medium": [
            {
                "question": "Based on the Machine Learning background on your resume, how do you detect and mitigate overfitting and underfitting using cross-validation, regularization (L1/L2), and feature selection?",
                "target_keywords": ["overfitting", "underfitting", "bias-variance", "regularization", "l1", "l2", "cross-validation"],
                "category": "Machine Learning Theory: Bias-Variance & Regularization"
            },
            {
                "question": "You list predictive modeling on your resume. How do you evaluate model performance on imbalanced datasets using Precision, Recall, F1-Score, and ROC-AUC curves rather than simple accuracy?",
                "target_keywords": ["precision", "recall", "f1-score", "roc-auc", "imbalance", "smote", "threshold"],
                "category": "Machine Learning Evaluation: Imbalanced Data"
            }
        ],
        "Hard": [
            {
                "question": "Your resume highlights ML engineering. How do you design an end-to-end MLOps pipeline for model training, hyperparameter tuning, model registry versioning, and real-time inference latency optimization?",
                "target_keywords": ["mlops", "model registry", "pipeline", "drift", "inference", "monitoring", "latency", "docker"],
                "category": "MLOps & System Architecture: Production Deployment"
            }
        ]
    },
    "nlp": {
        "Easy": [
            {
                "question": "Your resume mentions Natural Language Processing (NLP). Walk me through standard text preprocessing techniques such as tokenization, stop-word removal, lemmatization, and TF-IDF vectorization.",
                "target_keywords": ["tokenization", "lemmatization", "stemming", "stop words", "tf-idf", "preprocessing", "corpus"],
                "category": "NLP Fundamentals: Text Preprocessing & Vectorization"
            }
        ],
        "Medium": [
            {
                "question": "Based on your NLP experience on your resume, how do word embeddings (Word2Vec, GloVe) and contextual embeddings (BERT, RoBERTa) capture semantic relationships compared to bag-of-words?",
                "target_keywords": ["embeddings", "word2vec", "bert", "semantic", "cosine similarity", "dense vector", "context"],
                "category": "NLP Deep-Dive: Embeddings & Semantic Representation"
            },
            {
                "question": "You listed NLP on your resume. Explain the Self-Attention mechanism in Transformer architectures and why it outperforms traditional Recurrent Neural Networks (RNNs/LSTMs) for long sequences.",
                "target_keywords": ["self-attention", "transformer", "query key value", "rnn", "lstm", "vanishing gradient", "parallelization"],
                "category": "NLP Architecture: Transformers & Attention Mechanism"
            }
        ],
        "Hard": [
            {
                "question": "In your NLP work, how would you design a scalable Retrieval-Augmented Generation (RAG) system with dense vector indexing (FAISS/Pinecone), chunking strategies, and re-ranking models for enterprise documents?",
                "target_keywords": ["rag", "vector database", "chunking", "re-ranking", "retrieval", "embeddings", "hallucination", "llm"],
                "category": "Advanced NLP: RAG Architecture & Vector Search"
            }
        ]
    },
    "aws": {
        "Easy": [
            {
                "question": "Your resume includes AWS. Can you explain the roles of core services like EC2, S3, and IAM, and how IAM policies ensure least-privilege security?",
                "target_keywords": ["ec2", "s3", "iam", "least privilege", "roles", "policies", "bucket", "cloud"],
                "category": "AWS Fundamentals: Core Services & Security"
            }
        ],
        "Medium": [
            {
                "question": "Based on the AWS background on your resume, how would you architect a serverless backend using AWS Lambda, API Gateway, and DynamoDB or RDS, ensuring cold-start mitigation and cost efficiency?",
                "target_keywords": ["lambda", "api gateway", "serverless", "cold start", "dynamodb", "vpc", "scaling"],
                "category": "AWS Architecture: Serverless & API Gateway"
            },
            {
                "question": "In your cloud projects, how do you configure VPC networking, public vs private subnets, NAT Gateways, and Security Groups to protect database instances from public exposure?",
                "target_keywords": ["vpc", "subnet", "nat gateway", "security group", "cidr", "routing table", "private subnet"],
                "category": "AWS Networking: VPC & Cloud Security"
            }
        ],
        "Hard": [
            {
                "question": "Your resume showcases AWS cloud engineering. How do you design high-availability, multi-region architectures with Route 53 latency routing, Auto-Scaling Groups, Application Load Balancers, and automated disaster recovery?",
                "target_keywords": ["multi-region", "route 53", "auto-scaling", "alb", "disaster recovery", "rpo", "rto", "failover"],
                "category": "AWS Advanced Architecture: High Availability & DR"
            }
        ]
    },
    "docker": {
        "Easy": [
            {
                "question": "Your resume highlights Docker. What is the difference between a Docker Image and a Docker Container, and how does containerization differ from traditional virtual machines?",
                "target_keywords": ["container", "image", "dockerfile", "virtual machine", "kernel", "isolation", "portability"],
                "category": "DevOps Fundamentals: Docker Containers"
            }
        ],
        "Medium": [
            {
                "question": "Based on your Docker skills on your resume, how do you optimize Dockerfiles using multi-stage builds and layer caching to minimize production image size and build times?",
                "target_keywords": ["multi-stage", "layer caching", "dockerfile", "image size", "alpine", "build optimization"],
                "category": "Docker Deep-Dive: Multi-Stage Builds"
            }
        ],
        "Hard": [
            {
                "question": "In your containerized applications, how do you manage container networking, volume persistence, secrets injection, and transition from Docker Compose to Kubernetes Pods and Services?",
                "target_keywords": ["kubernetes", "docker-compose", "volumes", "secrets", "networking", "pods", "services", "ingress"],
                "category": "Container Orchestration: Docker to Kubernetes"
            }
        ]
    },
    "java": {
        "Easy": [
            {
                "question": "Your resume highlights Java. Can you explain the four pillars of Object-Oriented Programming (OOP) and how the Java Virtual Machine (JVM) executes bytecode?",
                "target_keywords": ["encapsulation", "inheritance", "polymorphism", "abstraction", "jvm", "bytecode", "jdk", "jre"],
                "category": "Java Fundamentals: OOP & JVM Execution"
            }
        ],
        "Medium": [
            {
                "question": "Based on your Java experience on your resume, how does Java memory management divide between Stack and Heap, and how does Garbage Collection (G1GC/ZGC) reclaim unreferenced objects?",
                "target_keywords": ["heap", "stack", "garbage collection", "g1gc", "memory", "metaspace", "references"],
                "category": "Java Memory Management: Heap, Stack & GC"
            },
            {
                "question": "You list Java and enterprise backends. How does Spring Boot handle Dependency Injection and Inversion of Control (IoC), and what are the scopes of Spring Beans?",
                "target_keywords": ["spring boot", "dependency injection", "ioc", "beans", "singleton", "prototype", "autowired"],
                "category": "Java Frameworks: Spring Boot & IoC"
            }
        ],
        "Hard": [
            {
                "question": "Your resume includes Java engineering. How do you handle multithreaded concurrency in Java using `java.util.concurrent`, synchronized blocks, volatile keywords, and preventing thread deadlocks?",
                "target_keywords": ["concurrency", "thread", "synchronized", "volatile", "deadlock", "executorservice", "atomic"],
                "category": "Java Concurrency: Thread Safety & Synchronization"
            }
        ]
    },
    "ui/ux": {
        "Easy": [
            {
                "question": "Your resume highlights UI/UX design. Can you explain the difference between wireframing, mockups, and interactive prototypes, and how user empathy drives design decisions?",
                "target_keywords": ["wireframe", "mockup", "prototype", "figma", "user research", "usability", "empathy"],
                "category": "UI/UX Fundamentals: Design Process & Prototyping"
            }
        ],
        "Medium": [
            {
                "question": "Based on your UI/UX and frontend skills, how do you establish a unified Design System (color tokens, typography, component variants) that bridges design in Figma to code in React/CSS?",
                "target_keywords": ["design system", "tokens", "figma", "components", "consistency", "responsive", "variants"],
                "category": "UI/UX & Frontend: Design Systems & Tokens"
            },
            {
                "question": "You listed UI/UX on your resume. How do you design for Accessibility (WCAG 2.1 AA), ensuring adequate color contrast, screen reader compatibility, and full keyboard navigation?",
                "target_keywords": ["accessibility", "wcag", "aria", "contrast", "keyboard navigation", "screen reader", "inclusive"],
                "category": "UI/UX Best Practices: Accessibility & Inclusivity"
            }
        ],
        "Hard": [
            {
                "question": "In your product design experience, how do you conduct heuristic evaluations, A/B usability testing, and analyze conversion drop-offs to iteratively refine product user journeys?",
                "target_keywords": ["heuristics", "a/b testing", "conversion", "user journey", "analytics", "usability testing", "ux metrics"],
                "category": "UI/UX Strategy: Usability Testing & Conversion"
            }
        ]
    }
}

# Category fallback question banks
QUESTION_BANK = {
    "INFORMATION-TECHNOLOGY": {
        "Easy": [
            {
                "question": "Can you walk me through your recent project experience and how you utilized your primary technical stack?",
                "target_keywords": ["project", "architecture", "framework", "database", "testing", "code", "development"],
                "category": "Technical Overview"
            },
            {
                "question": "How do you ensure code quality, readability, and maintainability when working in a team environment?",
                "target_keywords": ["code review", "git", "clean code", "unit testing", "documentation", "refactoring"],
                "category": "Software Engineering Practices"
            }
        ],
        "Medium": [
            {
                "question": "Explain a challenging technical bug or performance bottleneck you encountered. How did you diagnose and resolve it?",
                "target_keywords": ["debugging", "logs", "profiling", "root cause", "optimization", "performance", "resolution"],
                "category": "Problem Solving & Debugging"
            },
            {
                "question": "How do you design scalable RESTful APIs or database schemas to handle high concurrent user traffic?",
                "target_keywords": ["rest api", "schema", "indexing", "caching", "redis", "scalability", "load balancing"],
                "category": "System Design & Architecture"
            }
        ],
        "Hard": [
            {
                "question": "Describe a scenario where you had to make a trade-off between architectural purity and project deadlines. How did you manage technical debt?",
                "target_keywords": ["trade-off", "technical debt", "stakeholders", "refactoring", "milestones", "risk management"],
                "category": "Engineering Leadership & Strategy"
            },
            {
                "question": "Walk me through how you would architect a distributed real-time data streaming pipeline with failover resilience.",
                "target_keywords": ["kafka", "microservices", "replication", "fault tolerance", "event driven", "throughput"],
                "category": "Advanced Systems Architecture"
            }
        ]
    },
    "ENGINEERING": {
        "Easy": [
            {
                "question": "What engineering methodologies and CAD/modeling or simulation tools do you rely on most in your design workflow?",
                "target_keywords": ["design", "cad", "simulation", "modeling", "specs", "standards", "safety"],
                "category": "Engineering Fundamentals"
            }
        ],
        "Medium": [
            {
                "question": "Describe an instance where a prototype failed during initial testing. What steps did you take to re-engineer the component?",
                "target_keywords": ["prototype", "failure analysis", "testing", "tolerances", "stress test", "iteration"],
                "category": "Quality & Testing"
            }
        ],
        "Hard": [
            {
                "question": "How do you approach root-cause failure analysis in complex electromechanical or structural systems under harsh operating environments?",
                "target_keywords": ["root cause", "fea", "materials", "thermal", "compliance", "reliability"],
                "category": "Advanced Engineering Analysis"
            }
        ]
    },
    "FINANCE": {
        "Easy": [
            {
                "question": "How do you ensure accuracy and compliance when preparing financial reports and forecasting models?",
                "target_keywords": ["reconciliation", "compliance", "excel", "gaap", "audit", "forecasting"],
                "category": "Financial Reporting"
            }
        ],
        "Medium": [
            {
                "question": "Walk me through your process for evaluating investment risk and building discounted cash flow (DCF) models.",
                "target_keywords": ["dcf", "valuation", "wacc", "cash flow", "risk assessment", "variance"],
                "category": "Valuation & Analysis"
            }
        ],
        "Hard": [
            {
                "question": "How would you navigate capital allocation strategies during periods of high market volatility and inflation?",
                "target_keywords": ["hedging", "liquidity", "capital allocation", "macroeconomic", "portfolio strategy"],
                "category": "Strategic Finance"
            }
        ]
    },
    "HR": {
        "Easy": [
            {
                "question": "How do you handle conflict resolution between employees while maintaining workplace policy and empathy?",
                "target_keywords": ["communication", "conflict resolution", "policy", "empathy", "mediation", "confidentiality"],
                "category": "Employee Relations"
            }
        ],
        "Medium": [
            {
                "question": "What strategies do you use to attract and retain top talent in highly competitive labor markets?",
                "target_keywords": ["sourcing", "employer brand", "onboarding", "retention", "benefits", "engagement"],
                "category": "Talent Acquisition"
            }
        ],
        "Hard": [
            {
                "question": "Describe how you lead organizational restructuring or change management initiatives with minimal disruption to morale.",
                "target_keywords": ["change management", "culture", "leadership", "stakeholders", "communication plan"],
                "category": "Strategic HR Leadership"
            }
        ]
    }
}

GENERIC_QUESTIONS = {
    "Easy": [
        {
            "question": "Tell me about yourself and highlight key achievements from your background that align with this target role.",
            "target_keywords": ["experience", "achievements", "skills", "growth", "contribute", "background"],
            "category": "Behavioral Introduction"
        }
    ],
    "Medium": [
        {
            "question": "Describe a situation where you had to work under tight deadlines with competing priorities. How did you prioritize your tasks?",
            "target_keywords": ["prioritization", "deadline", "time management", "communication", "deliverables"],
            "category": "Behavioral & Time Management"
        }
    ],
    "Hard": [
        {
            "question": "Give an example of a difficult decision you made that was met with pushback from team members or stakeholders. How did you align the team?",
            "target_keywords": ["decision", "leadership", "negotiation", "alignment", "data driven", "stakeholders"],
            "category": "Leadership & Influence"
        }
    ]
}

class InterviewEvaluator:
    def __init__(self):
        self.question_bank = QUESTION_BANK
        self.skill_question_bank = SKILL_QUESTION_BANK

    def _normalize_skill_key(self, skill_name):
        """Maps diverse skill string representations to our canonical skill bank keys."""
        s = skill_name.strip().lower()
        if "react" in s:
            return "react"
        if "node" in s:
            return "node.js"
        if "python" in s:
            return "python"
        if "javascript" in s or s == "js":
            return "javascript"
        if "typescript" in s or s == "ts":
            return "javascript"
        if "sql" in s or "mysql" in s or "postgres" in s:
            return "sql"
        if "mongo" in s:
            return "mongodb"
        if "machine learning" in s or "ml" in s or "scikit" in s:
            return "machine learning"
        if "nlp" in s or "natural language" in s:
            return "nlp"
        if "aws" in s or "cloud" in s or "ec2" in s or "s3" in s:
            return "aws"
        if "docker" in s or "container" in s:
            return "docker"
        if "java" in s and "script" not in s:
            return "java"
        if "ui" in s or "ux" in s or "figma" in s:
            return "ui/ux"
        return s

    def _generate_dynamic_skill_question(self, skill, difficulty="Medium"):
        """Synthesizes structured, authentic technical interview questions for any skill."""
        diff = difficulty if difficulty in ["Easy", "Medium", "Hard"] else "Medium"
        skill_clean = skill.strip().title()

        templates = {
            "Easy": [
                {
                    "question": f"Your resume highlights proficiency in {skill_clean}. What core concepts, fundamental principles, and design conventions do you rely on when working with {skill_clean}?",
                    "target_keywords": [skill.lower(), "fundamentals", "principles", "best practices", "conventions", "implementation"],
                    "category": f"Resume Core: {skill_clean} Fundamentals"
                },
                {
                    "question": f"Can you walk me through how you first integrated {skill_clean} into your project workflow as listed on your resume, and what key advantages it provided?",
                    "target_keywords": [skill.lower(), "workflow", "advantages", "project", "integration", "tools"],
                    "category": f"Resume Workflow: {skill_clean} Integration"
                }
            ],
            "Medium": [
                {
                    "question": f"Based on your resume background in {skill_clean}, describe a challenging technical bottleneck, bug, or configuration hurdle you diagnosed and resolved when using {skill_clean}.",
                    "target_keywords": [skill.lower(), "debugging", "root cause", "resolution", "performance", "optimization"],
                    "category": f"Resume Troubleshooting: {skill_clean}"
                },
                {
                    "question": f"In your projects featuring {skill_clean}, how do you ensure maintainability, code quality, automated testing, and error handling?",
                    "target_keywords": [skill.lower(), "testing", "maintainability", "error handling", "quality", "clean code"],
                    "category": f"Resume Best Practices: {skill_clean}"
                }
            ],
            "Hard": [
                {
                    "question": f"Given your technical experience with {skill_clean}, how do you architect systems for high throughput, scalability, and security using {skill_clean} under demanding production conditions?",
                    "target_keywords": [skill.lower(), "scalability", "architecture", "security", "throughput", "concurrency", "performance"],
                    "category": f"Resume Architecture: {skill_clean} Scalability"
                },
                {
                    "question": f"If you were tasked with auditing and refactoring a large-scale codebase built with {skill_clean}, what criteria, performance profiling, and design patterns would you prioritize?",
                    "target_keywords": [skill.lower(), "refactoring", "profiling", "patterns", "technical debt", "optimization"],
                    "category": f"Resume Engineering: {skill_clean} Optimization"
                }
            ]
        }
        options = templates.get(diff, templates["Medium"])
        selected = random.choice(options)
        return selected

    def generate_question(
        self,
        category="INFORMATION-TECHNOLOGY",
        target_role="Software Engineer",
        difficulty="Medium",
        asked_ids=None,
        resume_skills=None,
        candidate_name=None,
        resume_text=None,
        experience_years=None
    ):
        """
        Dynamically synthesizes deeply personalized interview questions directly anchored
        in the candidate's uploaded resume skills, project portfolio, and experience level.
        """
        asked_ids = asked_ids or []
        resume_skills = [s.strip() for s in (resume_skills or []) if s.strip()]
        candidate_name = candidate_name or "Candidate"
        asked_count = len(asked_ids)

        # -------------------------------------------------------------
        # RESUME-TAILORED INTERVIEW QUESTION GENERATOR
        # -------------------------------------------------------------
        if resume_skills and len(resume_skills) > 0:
            candidate_pool = []

            # 1. Project Architecture & Cross-Stack Synthesis
            if len(resume_skills) >= 2:
                primary = resume_skills[0]
                secondary = resume_skills[1]
                tertiary = resume_skills[2] if len(resume_skills) > 2 else secondary

                # Architectural Deep-Dives
                candidate_pool.append({
                    "question": f"In your uploaded resume, you highlighted building scalable applications with {primary} and {secondary}. Can you walk me through the high-level architecture of that project, your data flow, and how you handled API and database persistence?",
                    "target_keywords": [primary.lower(), secondary.lower(), "architecture", "data flow", "api", "database", "project"],
                    "category": f"Resume Project Deep-Dive: {primary} & {secondary}",
                    "difficulty": "Medium"
                })

                candidate_pool.append({
                    "question": f"Looking at your experience with {primary} and {secondary}, describe a scenario where you faced a significant performance bottleneck, memory leak, or concurrency issue. How did you diagnose the root cause and optimize it?",
                    "target_keywords": [primary.lower(), secondary.lower(), "debugging", "root cause", "bottleneck", "profiling", "optimization"],
                    "category": f"Resume Debugging: {primary} & {secondary}",
                    "difficulty": "Medium"
                })

                candidate_pool.append({
                    "question": f"On your resume, you listed competencies across {primary}, {secondary}, and {tertiary}. If the system you developed experienced a 10x surge in daily traffic, where would the primary bottlenecks emerge in this stack, and how would you scale it horizontally?",
                    "target_keywords": [primary.lower(), secondary.lower(), tertiary.lower(), "scalability", "load balancing", "caching", "horizontal scaling", "bottleneck"],
                    "category": f"Resume Scalability: {primary} & {secondary}",
                    "difficulty": "Hard"
                })

                candidate_pool.append({
                    "question": f"You highlighted {primary} and {secondary} on your resume. What security vulnerabilities (such as injection, broken authentication, or CORS issues) do you proactively guard against in that architecture, and how do you implement automated testing?",
                    "target_keywords": [primary.lower(), secondary.lower(), "security", "authentication", "testing", "unit test", "validation"],
                    "category": f"Resume Production Readiness: {primary}",
                    "difficulty": "Medium"
                })

                candidate_pool.append({
                    "question": f"As someone with experience in {primary} and {secondary}, tell me about a time you had to make a trade-off between architectural purity and delivering on a tight deadline. How did you manage technical debt?",
                    "target_keywords": [primary.lower(), "trade-off", "technical debt", "prioritization", "deadline", "refactoring"],
                    "category": f"Resume Behavioral: Engineering Trade-offs",
                    "difficulty": "Hard"
                })

            # 2. Skill-Specific Bank Questions for Candidate's Skills
            for skill in resume_skills:
                norm_key = self._normalize_skill_key(skill)
                if norm_key in self.skill_question_bank:
                    bank_for_skill = self.skill_question_bank[norm_key]
                    
                    # Add questions for current difficulty first
                    diff_list = bank_for_skill.get(difficulty, [])
                    for q_item in diff_list:
                        candidate_pool.append({
                            "question": q_item["question"],
                            "target_keywords": q_item["target_keywords"],
                            "category": q_item["category"],
                            "difficulty": difficulty
                        })
                    
                    # Also include adjacent difficulties as backup
                    for d_key, q_list in bank_for_skill.items():
                        if d_key != difficulty:
                            for q_item in q_list:
                                candidate_pool.append({
                                    "question": q_item["question"],
                                    "target_keywords": q_item["target_keywords"],
                                    "category": q_item["category"],
                                    "difficulty": d_key
                                })
                else:
                    # Dynamically generate question for any skill
                    dyn_q = self._generate_dynamic_skill_question(skill, difficulty)
                    candidate_pool.append({
                        "question": dyn_q["question"],
                        "target_keywords": dyn_q["target_keywords"],
                        "category": dyn_q["category"],
                        "difficulty": difficulty
                    })

            # Filter out questions already asked
            unasked = [q for q in candidate_pool if q["question"] not in asked_ids]

            # Thoughtful Progression Ordering:
            # Question 1: Project & Architecture overview
            # Question 2: Primary skill core concepts
            # Question 3: Secondary skill or database/cloud
            # Question 4: Debugging & troubleshooting
            # Question 5: Scalability & security
            # Question 6+: Behavioral leadership & trade-offs
            if unasked:
                # Prefer questions matching current difficulty
                matching_diff = [q for q in unasked if q.get("difficulty") == difficulty]
                pool_to_pick = matching_diff if matching_diff else unasked

                # If question 1 (asked_count == 0), prioritize Project Deep-Dive
                if asked_count == 0:
                    proj_qs = [q for q in pool_to_pick if "Project Deep-Dive" in q.get("category", "")]
                    if proj_qs:
                        selected = proj_qs[0]
                    else:
                        selected = random.choice(pool_to_pick)
                elif asked_count == 1:
                    # Primary skill core
                    norm_first = self._normalize_skill_key(resume_skills[0])
                    primary_qs = [q for q in pool_to_pick if norm_first in q.get("question", "").lower() or norm_first in q.get("category", "").lower()]
                    selected = primary_qs[0] if primary_qs else random.choice(pool_to_pick)
                elif asked_count == 2 and len(resume_skills) > 1:
                    # Secondary skill / database / cloud
                    norm_sec = self._normalize_skill_key(resume_skills[1])
                    sec_qs = [q for q in pool_to_pick if norm_sec in q.get("question", "").lower() or norm_sec in q.get("category", "").lower()]
                    selected = sec_qs[0] if sec_qs else random.choice(pool_to_pick)
                elif asked_count == 3:
                    # Debugging or Troubleshooting
                    debug_qs = [q for q in pool_to_pick if "Debugging" in q.get("category", "") or "Troubleshooting" in q.get("category", "")]
                    selected = debug_qs[0] if debug_qs else random.choice(pool_to_pick)
                elif asked_count == 4:
                    # Scalability or Security
                    scale_qs = [q for q in pool_to_pick if "Scalability" in q.get("category", "") or "Architecture" in q.get("category", "")]
                    selected = scale_qs[0] if scale_qs else random.choice(pool_to_pick)
                else:
                    selected = random.choice(pool_to_pick)

                return {
                    "question_id": selected["question"],
                    "question": selected["question"],
                    "difficulty": selected.get("difficulty", difficulty),
                    "category": selected.get("category", "Resume Skill Deep-Dive"),
                    "target_keywords": selected.get("target_keywords", [s.lower() for s in resume_skills[:4]]),
                    "is_resume_tailored": True
                }

            # If all pre-generated questions were exhausted, generate fresh dynamic ones
            skill_choice = random.choice(resume_skills)
            fresh_dyn = self._generate_dynamic_skill_question(skill_choice, difficulty)
            return {
                "question_id": fresh_dyn["question"],
                "question": fresh_dyn["question"],
                "difficulty": difficulty,
                "category": fresh_dyn["category"],
                "target_keywords": fresh_dyn["target_keywords"],
                "is_resume_tailored": True
            }

        # -------------------------------------------------------------
        # FALLBACK: CATEGORY QUESTION BANK (When no resume uploaded)
        # -------------------------------------------------------------
        cat_key = category.upper() if category and category.upper() in self.question_bank else "INFORMATION-TECHNOLOGY"
        diff_questions = self.question_bank.get(cat_key, {}).get(difficulty)
        if not diff_questions:
            diff_questions = GENERIC_QUESTIONS.get(difficulty, GENERIC_QUESTIONS["Medium"])

        available = [q for q in diff_questions if q["question"] not in asked_ids]
        if not available:
            available = diff_questions

        selected = random.choice(available)
        q_text = selected["question"]
        if target_role and target_role != "Professional":
            q_text = q_text.replace("this target role", f"the {target_role} position")

        return {
            "question_id": selected["question"],
            "question": q_text,
            "difficulty": difficulty,
            "category": selected.get("category", "General Professional"),
            "target_keywords": selected.get("target_keywords", []),
            "is_resume_tailored": False
        }

    def evaluate_response(self, question_text, target_keywords, candidate_response, current_difficulty="Medium"):
        """
        Evaluates candidate answers using Deep Semantic Answer Evaluator & Vocal Delivery Metrics.
        """
        return deep_answer_evaluator.evaluate_candidate_answer(
            question=question_text,
            target_keywords=target_keywords,
            user_response=candidate_response,
            current_difficulty=current_difficulty
        )

interview_evaluator = InterviewEvaluator()
