# Defining Emergence

Imagine a single point on a graph. Imagine another point, somewhere off to the side and up. Just as you imagined a second point, a brand new emergent property appeared: a distance between the points. And quite a few more properties, such as whether a point is higher or lower than another on one of the axes.

These emergent properties aren't specific to each point: a point can't have a distance or an incline, but a line between points can, just as a point cannot be closer to one axis than another without that other point. These properties emerge from differences in points' core attributes, specifically their coordinates.

To compute the difference between two points, we use the Euclidean distance formula. Coordinates are for points; binary attributes are for operations. Hamming distance measures distance between objects with binary attributes; we compute it by XORing the attributes.

Think of two opposing sets of Reversi pieces. If both opposing pieces are black side up, then XOR will report false - meaning no difference. So computing the number of moves to orient both sets the same way is as easy as counting how many times XOR returns true for their colors.

## Counting Attributes

As each operation has three attributes, there are nine distinct pairs of source and destination attributes.

These pairs aren't attributes themselves, only pairings: true attributes must show differences between functions, and emergent attributes must create new information. So if a source has a positive attribute A and the destination has the same positive attribute A, XOR reports false: there's no difference.

Likewise, if a source has a positive attribute A, but the destination has a negative A, then XOR reports true because the values differ.

| X -> Y                        | Impression | Identification | Calibration | Opportunity | Insight | Impact | Emotion | Conviction |
|-------------------------------|------------|----------------|-------------|-------------|---------|--------|---------|------------|
| Internal(X) XOR Internal(Y)   | 1          | 1              | 1           | 1           | 1       | 1      | 1       | 1          |
| Internal(X) XOR Objective(Y)  | 1          | 0              | 0           | 1           | 1       | 0      | 0       | 1          |
| Internal(X) XOR Relative(Y)   | 0          | 1              | 1           | 0           | 1       | 0      | 0       | 1          |
| Objective(X) XOR Internal(Y)  | 1          | 1              | 0           | 0           | 0       | 0      | 1       | 1          |
| Objective(X) XOR Objective(Y) | 1          | 0              | 1           | 0           | 0       | 1      | 0       | 1          |
| Objective(X) XOR Relative(Y)  | 0          | 1              | 0           | 1           | 0       | 1      | 0       | 1          |
| Relative(X) XOR Internal(Y)   | 1          | 1              | 0           | 0           | 1       | 1      | 0       | 0          |
| Relative(X) XOR Objective(Y)  | 1          | 0              | 1           | 0           | 1       | 0      | 1       | 0          |
| Relative(X) XOR Relative(Y)   | 0          | 1              | 0           | 1           | 1       | 0      | 1       | 0          |

From this table, we can see that if both the source (X) and the destination (Y) are either external and internal or internal and external, there is always a difference between these attributes in all functions, and there's no difference between functions. So Internal(X) XOR Internal(Y) is the only pairing in this table that does not emerge as an attribute, as a way to split all functions in half.

By contrast, Relative(X) XOR Objective(Y) is a true attribute because it evenly splits all functions into two groups of four. That said, this table alone doesn't tell us whether it is emergent or inherited; we need to compare the groupings this and other pairings create with the table of inherited and emergent attributes.

Before we line up the earlier attribute table against this table for verification, consider that our assignment of 1 and 0 in the original table is arbitrary. We could have used 0 instead of 1, and 1 instead of 0 across any row, and still ended up with the same set of splits. In other words, row-wise negation creates an invariant: functions in a group C labeled as 1 are going to be in the same group if we re-label it as 0.

We already eliminated one row as a non-attribute, and now we can use this observation to eliminate two more rows:

- Relative(X) XOR Objective(Y) is the same as Objective(X) XOR Relative(Y) but negated
- Relative(X) XOR Relative(Y) is the same as Objective(X) XOR Objective(Y) but negated

If we notice that negation is the same as a pole flip (Objective is not-Subjective), we get a list that matches six of seven earlier proposed attributes.

| X -> Y                         | Impression | Identification | Calibration | Opportunity | Insight | Impact | Emotion | Conviction |
|--------------------------------|------------|----------------|-------------|-------------|---------|--------|---------|------------|
| Immediate/Indirect (B^C)       | 0          | 1              | 1           | 0           | 0       | 1      | 1       | 0          |
| External(X) XOR Objective(Y)   | 0          | 1              | 1           | 0           | 0       | 1      | 1       | 0          |
| Strategic/Tactical (A^B^C)     | 1          | 0              | 0           | 1           | 0       | 1      | 1       | 0          |
| External(X) XOR Relative(Y)    | 1          | 0              | 0           | 1           | 0       | 1      | 1       | 0          |
| Temporal/Spatial (A^C)         | 0          | 1              | 0           | 1           | 1       | 0      | 1       | 0          |
| Relative(X) XOR Relative(Y)    | 0          | 1              | 0           | 1           | 1       | 0      | 1       | 0          |
| Absolute/Relative (A^B)        | 0          | 0              | 1           | 1           | 1       | 1      | 0       | 0          |
| Subjective(X) XOR Internal(Y)  | 0          | 0              | 1           | 1           | 1       | 1      | 0       | 0          |
| Deduction/Induction (C)        | 1          | 0              | 1           | 0           | 1       | 0      | 1       | 0          |
| Relative(X) XOR Objective(Y)   | 1          | 0              | 1           | 0           | 1       | 0      | 1       | 0          |
| Subjective/Objective (B)       | 1          | 1              | 0           | 0           | 1       | 1      | 0       | 0          |
| Relative(X) XOR Internal(Y)    | 1          | 1              | 0           | 0           | 1       | 1      | 0       | 0          |

For each attribute, at least one other attribute pairing has the same binary fingerprint. For example, after a double negation, Immediate/Indirect can be expressed as:

- Internal(X) XOR Subjective(Y)
- External(X) XOR Objective(Y)

Here, Internal(X) negated is External(X), and Subjective(Y) negated is Objective(Y).

Immediate/Indirect can also be derived as Absolute(Y).

A few attributes are special because you can't derive them by looking at only one end or the other. Further, they have twice as many expressions: Deduction/Induction and Temporal/Spatial are like this.

Deduction/Induction can be expressed as:

- Subjective(X) XOR Relative(Y)
- Objective(X) XOR Absolute(Y)
- Absolute(X) XOR Subjective(Y)
- Relative(X) XOR Objective(Y)

And Temporal/Spatial can be expressed with:

- Subjective(X) XOR Objective(Y)
- Objective(X) XOR Subjective(Y)
- Absolute(X) XOR Absolute(Y)
- Relative(X) XOR Relative(Y)

The missing attribute (Internal/External) is trivially read directly from the destination.

| Attribute                  | Example Pair                  |
|----------------------------|-------------------------------|
| Immediate/Indirect (B^C)   | External(X) XOR Objective(Y)  |
| Strategic/Tactical (A^B^C) | External(X) XOR Relative(Y)   |
| Temporal/Spatial (A^C)     | Relative(X) XOR Relative(Y)   |
| Absolute/Relative (A^B)    | Subjective(X) XOR Internal(Y) |
| Deduction/Induction (C)    | Relative(X) XOR Objective(Y)  |
| Subjective/Objective (B)   | Relative(X) XOR Internal(Y)   |
| External/Internal (A)      | External(Y)                   |

Now, let's figure out what this all means.
