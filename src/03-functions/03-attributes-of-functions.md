# Attributes of Functions

To single out a function, one needs exactly three questions, with each question splitting the space in half. The disagreement (XOR) between the questions is also a question, so we end up with seven questions in total.

|       | Impression | Identification | Calibration | Opportunity | Insight | Impact | Emotion | Conviction |
|-------|------------|----------------|-------------|-------------|---------|--------|---------|------------|
| A     | 1          | 1              | 1           | 1           | 0       | 0      | 0       | 0          |
| B     | 1          | 1              | 0           | 0           | 1       | 1      | 0       | 0          |
| A^B   | 0          | 0              | 1           | 1           | 1       | 1      | 0       | 0          |
| C     | 1          | 0              | 1           | 0           | 1       | 0      | 1       | 0          |
| A^C   | 0          | 1              | 0           | 1           | 1       | 0      | 1       | 0          |
| B^C   | 0          | 1              | 1           | 0           | 0       | 1      | 1       | 0          |
| A^B^C | 1          | 0              | 0           | 1           | 0       | 1      | 1       | 0          |


These are essentially Hadamard matrices with the first row (all zeros) omitted. Programmatically, these matrices of any necessary size can be constructed recursively from the smallest Hadamard matrix using Sylvester's construction.

As with attributes, none of the questions is strictly primary: if we choose a different first question, the earlier first question will naturally emerge from the XOR with the other questions.

Unlike with attributes, we can't just pick three and use them as a classification basis: XOR terms cancel each other, so if you add A^B to the basis of A and B you end up with a set of questions that cannot pin down a single function. Another invalid set is A^B, A^C, B^C: any two imply the third. To cut it short, there are 28 valid bases and 7 invalid bases.

## Inherited attributes

Recall that we started with the initial pair of conceptual categories: external and internal. These functions are also subject to this distinction, so there are external and internal functions.

How do we tell which function is external or internal? If we look at where a function ends up structurally, relative to the boundary, that's what the function is. We can infer that by looking at the final operation, where the signal ends up: a destination defines whether a function is internal or external. So Identification is external, as its final operation is Sense, an external operation, and Insight is internal, finishing with Know, an internal operation. If you look at the summary table, it makes intuitive sense.

| Internal (A = 0)               | External (A = 1)                 |
|--------------------------------|----------------------------------|
| **Insight**: Sense → Know      | **Impression**: Know → Predict   |
| **Impact**: Sense → Feel       | **Identification**: Know → Sense |
| **Conviction**: Predict → Know | **Calibration**: Feel → Sense    |
| **Emotion**: Predict → Feel    | **Opportunity**: Feel → Predict  |

We also expanded our category powers to include subjective and objective, as well as absolute and relative, distinctions.

The starting point, the origin of the signal, defines whether an idea is objective or subjective. For functions, we can infer that from looking at the initial, starting operation, where the signal starts: the source defines whether a function is objective or subjective. So Opportunity is subjective because Feel is a subjective operation, and Impression is objective because Know is an objective operation.

| Subjective (B = 0)              | Objective (B = 1)                |
|---------------------------------|----------------------------------|
| **Calibration**: Feel → Sense   | **Impression**: Know → Predict   |
| **Opportunity**: Feel → Predict | **Identification**: Know → Sense |
| **Conviction**: Predict → Know  | **Insight**: Sense → Know        |
| **Emotion**: Predict → Feel     | **Impact**: Sense → Feel         |

We can devise a test to determine whether a function is absolute or relative. Still, we could cut to the chase and compute the result as the XOR of the objective/subjective and external/internal attributes.

| Absolute (A^B = 0) | Relative (A^B = 1) |
|--------------------|--------------------|
| **Impression**     | **Calibration**    |
| **Identification** | **Opportunity**    |
| **Conviction**     | **Insight**        |
| **Emotion**        | **Impact**         |

So Impact is a relative function, and Conviction is an absolute function: it makes intuitive sense, as you can't measure the impact of an explosion without comparing it to some measure, a meter, but you can see my conviction to keep spelling these ideas out – it is just there.

|                              | Impression | Identification | Calibration | Opportunity | Insight   | Impact    | Emotion    | Conviction |
|------------------------------|------------|----------------|-------------|-------------|-----------|-----------|------------|------------|
| External/Internal (A/~A)     | External   | External       | External    | External    | Internal  | Internal  | Internal   | Internal   |
| Objective/Subjective (B/~B)  | Objective  | Objective      | Subjective  | Subjective  | Objective | Objective | Subjective | Subjective |
| Relative/Absolute (A^B/~A^B) | Absolute   | Absolute       | Relative    | Relative    | Relative  | Relative  | Absolute   | Absolute   |
| C                            | 1          | 0              | 1           | 0           | 1         | 0         | 1          | 0          |
| A^C                          | 0          | 1              | 0           | 1           | 1         | 0         | 1          | 0          |
| B^C                          | 0          | 1              | 1           | 0           | 0         | 1         | 1          | 0          |
| A^B^C                        | 1          | 0              | 0           | 1           | 0         | 1         | 1          | 0          |

I call these three attributes inherited because they were born at the operation level, or earlier. Think of a surname inherited from parents. By comparison, the yet unknown attributes are emergent attributes: each emergent attribute is a question that a single component of a function cannot explain. Here's another way to put it: emergent attributes are properties of functions that are born from relations between operations, not from operations themselves.

Let's uncover what these emergent attributes mean for functions and how we can build intuition for them.
