# New Attributes

Where are these operations relative to the boundary? If we look at the final points of each operation's movement, Know and Feel belong to internal ideas, while Sense and Predict belong to external ideas.

| Operation   | Movement            | External or Internal? |  
|-------------|---------------------|-----------------------|
| **Know**    | External → Internal | Internal              |
| **Sense**   | External → External | External              |
| **Feel**    | Internal → Internal | Internal              |
| **Predict** | Internal → External | External              |

Knowing if an idea is external or internal to the boundary does not allow us to classify it into four buckets. As each question cuts the possibility space in half, we need at least one more question or attribute to specify exactly one of four binary classes: say, if an idea belongs to knowing or feeling.

Let's call attribute A the external/internal distinction.

- Know and Feel share A=Internal, so they must differ on B
- Sense and Predict share A=External, so they must differ on B
 
So, Know and Sense share the same value for the unknown attribute B, while Feel and Predict share the opposite value of the attribute B.

Alternatively, Know and Predict could share the same value for a different unknown attribute B', while Feel and Sense share the opposite value of attribute B'. Both attributes, B and B', satisfy our requirement.

If we look at the truth table with all three attributes, we immediately recognize the binary logical function XOR (exclusive OR). 

| A | B | B' |  
|---|---|----|
| 0 | 0 | 0  |
| 1 | 0 | 1  |
| 0 | 1 | 1  |
| 1 | 1 | 0  |

So B and B' are independent of each other, but neither is independent of A (knowing A and B determines B' while knowing A and B' determines B).

How does XOR work in action? Close one eye while keeping the other open - you've made a wink. This gesture exists only when your eyelids are in different states. Both eyes open? No wink. Both closed? No wink. Different states? Wink appears. That's XOR, creating something new from differences.

We are looking at more than we bargained for: a third binary attribute that is a valid classification pair to the first attribute. Both B and B' can be considered a third attribute relative to each other.

Whichever attribute we chose as the canonical attribute (a standard representation, not a superior one) for the classification basis, the other emerges as the third. Neither B nor B' is "more primary" because they're both describing the exact structural requirement: the second bit.

For simplicity's sake, let's take the grouping where Know and Sense share a value as our canonical attribute B, in addition to attribute A, so that the third attribute will be A^B.

For operations, we have

- One inherited attribute (external/internal), A - inherited from the membrane
- Two emergent attributes (B, A^B) - they appeared first for operations
- And two canonical attributes (A, B)

| Operation   | A        | B | A^B |  
|-------------|----------|---|-----|
| **Know**    | Internal | 0 | 0   |
| **Sense**   | External | 0 | 1   |
| **Feel**    | Internal | 1 | 1   |
| **Predict** | External | 1 | 0   |

This constrained triple's redundancy is practically convenient: classify using any two, then test it with the third. If the third disagrees, it means you made an error somewhere. 

But as with dance moves, the next logical step is [to name B and A^B](./03-naming-attributes.md).
