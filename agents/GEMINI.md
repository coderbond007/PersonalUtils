# Anti-Hallucination Prompting & Keywords

Coding hallucinations—where an AI confidently makes up non-existent functions,
outdated syntax, or phantom libraries—can be mitigated by using specific
structural phrases and keywords in your prompts. This acts as a guardrail,
forcing the agent to prioritize accuracy over simply generating a
plausible-sounding response.

### 1. The "Permission to Fail" Keywords

By default, AI models would rather invent an answer than admit they can't help.
You have to explicitly give them permission to stop.

*   **"If you are unsure, say 'I don't know'."** (This is arguably the single
    most effective phrase you can use).
*   **"Do not fabricate APIs or libraries."**
*   **"Only use standard, built-in functions unless explicitly instructed
    otherwise."**
*   **"If a specific package is required but not mentioned, flag it before
    writing the code."**

### 2. The Chain-of-Thought (CoT) Keywords

Forcing an AI to explain its reasoning *before* it writes the code drastically
reduces logic gaps and prevents it from going down a hallucinatory rabbit hole.

*   **"Think step-by-step."**
*   **"Explain your logic before writing the code."**
*   **"Outline the architecture before providing the implementation."**
*   **"First, list the exact API endpoints and methods you intend to use."**

### 3. The Grounding Keywords

Hallucinations often happen when the AI relies on the vast, blurry edges of its
training data. You want to tether it to verifiable facts.

*   **"According to the official [Language/Framework] documentation..."**
*   **"Based strictly on [Version X.X]..."** (e.g., "Based strictly on Python
    3.11"). This prevents it from using deprecated code or hallucinating
    features from future releases.
*   **"Using ONLY the provided context/snippet..."** (If you are pasting in your
    own code or documentation).
*   **"Provide citations for the documentation you are referencing."**

### 4. The Self-Correction & Verification Keywords

You can build a "maker-checker" system directly into your prompt, forcing the AI
to evaluate its own output.

*   **"Review this code for edge cases and potential runtime errors."**
*   **"Are there any deprecated methods in your proposed solution?"**
*   **"Verify that all imported modules actually exist in the standard
    library."**

### Pro-Tip: The "Research Mode" Prompt

If you are starting a complex task, combine these into a single system
constraint at the beginning of your prompt:

> *"Act as an expert developer. Think step-by-step and outline your logic before
> writing any code. Strictly adhere to the official documentation for
> [Framework/Language]. Do not fabricate or hallucinate APIs; if you are unsure
> of a function's existence, explicitly state 'I do not know' and ask me for
> clarification."*