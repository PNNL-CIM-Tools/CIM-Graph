# Coding Rules

## 1. KISS First, Always

**Keep It Simple, Stupid.**

- Prefer straightforward logic over clever tricks or patterns.
- If a junior developer couldn’t explain the code in 2–3 sentences, it’s too complex.
- Avoid unnecessary indirection (e.g., “manager of managers”, nested factories, etc.).

**Agent behavior:**

- Default to the simplest solution that satisfies the requirements.
- Do not introduce abstractions or patterns unless they clearly simplify the codebase.

---

## 2. Be Ruthlessly DRY (But Not Dogmatic)

**Don’t Repeat Yourself**, especially for logic and behavior.

- Extract shared logic into well-named functions or modules.
- Avoid copy-pasting the same behavior across files or components.
- However, don’t create convoluted abstractions just to deduplicate a few similar lines.

**Agent behavior:**

- Look for repeated logic; encapsulate it in reusable functions.
- Prefer small, meaningful helper functions over generic “doEverythingUtil” helpers.
- It’s okay to repeat a tiny bit of code if abstraction would obscure intent.

---

## 3. Avoid Over-Abstraction

Abstractions must **earn their keep**.

- Only abstract when there are **real, repeated patterns** and they are stable.
- Don’t build meta-frameworks, super-generic base classes, or over-generic utilities.
- If an abstraction makes the mental model harder to understand, don’t add it.

**Agent behavior:**

- Prefer concrete, domain-specific functions over hyper-generic helpers.
- Do not introduce complex inheritance trees or deep hierarchies.
- Avoid “just in case” abstraction for hypothetical future use.

---

## 4. Avoid Over-Engineering

Design for **today’s real requirements**, not every hypothetical tomorrow.

- Apply **YAGNI**: You Aren’t Gonna Need It.
- Don’t add features, flags, extension points, or layers until there is a proven need.
- Avoid gold-plating: extra complexity without clear value.

**Agent behavior:**

- Implement only what is explicitly required or what is obviously necessary to make it robust.
- Do not speculate about future requirements or build for imaginary extensibility.

---

## 5. Fail Fast, Don’t “Fallback Forever”

Too many fallbacks signal **low confidence** in the design.

- Each fallback should be **intentional**, **rare**, and **well-understood**.
- Prefer clear failure with good error messages over silently cascading through many fallbacks.
- “Try this, if not then this, then that, then that…” is a smell.

**Agent behavior:**

- Implement at most one or two clear, well-documented fallback paths where truly needed.
- When something is critical, fail fast with a clear error rather than guessing.

---

## 6. No Blanket Try/Catch as a Safety Blanket

Defensive coding is good; paranoia everywhere is not.

- Catch exceptions **only where they can be handled meaningfully**.
- Avoid blanket `catch (Exception)` / `try/except` sprinkled around every function.
- Unhandled exceptions should bubble up with context and be handled at a clear boundary (e.g., top-level handler, API boundary).

**Agent behavior:**

- Place try/catch/try-except blocks around specific risky operations, not whole functions.
- When catching, either:
  - recover in a well-defined way, or
  - log and rethrow / propagate with context.
- Do not hide failures or swallow exceptions silently.

---

## 7. Prefer Functional, Side-Effect-Minimal Code

Predictable code is easier to test and reason about.

- Functions should have clear inputs and outputs.
- Minimize hidden state and unexpected side effects.
- Side-effectful functions should have names that make side effects obvious (e.g., `saveUser`, `sendEmail`, `logEvent`).

**Agent behavior:**

- Decompose complex procedures into small, purpose-focused functions.
- When possible, keep helpers pure (no I/O, no global state changes).
- Make side effects explicit and isolated.

---

## 8. Optimize for Human Readability Over Cleverness

Code is read far more than it’s written.

- Choose clarity over micro-optimizations unless profiling proves a real need.
- Use meaningful names; avoid abbreviations and cryptic naming.
- If the “clever” version needs a long comment to explain it, write the obvious version instead.

**Agent behavior:**

- Prefer explicit loops and conditionals over complex one-liners or deeply nested expressions.
- Add short, focused comments where intent is not obvious from the code itself.
- Respect existing naming and style conventions in the repo.

---

## 9. Keep Modules Small, Cohesive, and Well-Bounded

Good structure reduces complexity.

- Each module/class/component should do **one thing well**.
- Avoid “god objects” and massive utility modules that know about everything.
- Boundaries between modules should be clear and logical.

**Agent behavior:**

- Group related code together; don’t scatter related behavior across many files without reason.
- When adding new functionality, consider whether it fits an existing module or deserves a small new one.
- Don’t introduce cross-cutting dependencies that tangle unrelated parts of the codebase.

---

## 10. Build for Maintainability: Tests, Logs, and Contracts

Confidence comes from **design + verification**, not from piles of fallback logic.

- Add tests around critical and non-obvious logic.
- Validate inputs where appropriate and fail with clear messages.
- Log at meaningful boundaries with actionable, non-noisy messages.

**Agent behavior:**

- When adding complex logic, also add or update tests.
- Prefer simple, focused tests that check behavior over overly clever or brittle tests.
- Use logging thoughtfully: enough to help debug, not so much that it becomes noise.

---

## Summary for Agents

When generating or modifying code in this repository, ask:

1. **Is this the simplest solution that clearly solves the problem?**
2. **Am I repeating logic that should be shared?**
3. **Am I introducing abstractions or fallbacks just to feel “safe” rather than because they’re needed?**
4. **Will a human reading this code later quickly understand what it does and why?**

If the answer to any of these is “no” or “not really”, rewrite until it is.

Agents must prioritize:
**KISS → DRY → Readable → Maintainable**
over cleverness, over-engineering, and defensive complexity.
