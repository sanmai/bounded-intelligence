# Probabilistic Inference

When considering complex concepts like friendship, we often struggle to place them definitively. Is friendship more internal or external? More objective or subjective?

Infinite precision is infinitely expensive. By converting this uncertainty into confidence levels, we'll get usable answers from partial certainties on the cheap.

## Degrees, Not Boxes

Let's replace the binary yes-or-no with degree measurements. Instead of "Is this internal or external?" we ask "How internal and how external is this?"

Then, the probability for a given category is simply the product of the probabilities.

\\[
\begin{aligned}
P(Know) &= P(Internal) \times P(Objective) \times P(Relative) \\\\
P(Sense) &= P(External) \times P(Objective) \times P(Absolute) \\\\
P(Feel) &= P(Internal) \times P(Subjective) \times P(Absolute) \\\\
P(Predict) &= P(External) \times P(Subjective) \times P(Relative)
\end{aligned}
\\]

Think of the friendship that you had with your best friend. You express it through visible actions (external), but base it on personal feelings (subjective). You understand friendship in comparison: it is closer than acquaintanceship, less intense than romantic love (relative).

- P(Internal) = 0.35, P(External) = 0.65 (not fully external, but more outside than&nbsp;inside)
- P(Objective) = 0.3, P(Subjective) = 0.7 (more subjective, starts with&nbsp;you)
- P(Absolute) = 0.15, P(Relative) = 0.85 (strongly relative)

P(Predict) will have the highest score with 0.39 (39%), followed by P(Know) at 0.09, P(Feel) at 0.04, and P(Sense) at 0.03.

You did not need to decide if friendship is definitely external. Predicting still won with 39%, with everything else following far behind. You did not need 100% certainty to make decisions that work.

That 16% attributable to other operations is what we lost to aliasing, across many dimensions of friendship (a complex socio-biological phenomenon), to fit it into one of the four boxes.

## Selective Filter

If we compute the totals, we find that almost half the probability (46%) landed outside any operation, more than the highest answer. It isn't aliased-away information about friendship; it's information that meant nothing, void.

Those combinations did not correspond to anything: no operation is all internal, subjective, and relative, but this contradiction accounts for 21% of the total probability. The system excluded background noise using structural constraints between its own attributes.

Recall the sufficiency constraint. If the environment has infinite ways to kill you, then most structures of matter don't persist. Life has to find the tiny subset of designs that work against perpetual chaos.

The more attributes you add, the more selective the filter becomes. A classification with more types and attributes that selects only 5% meaning from the chaos suggests that coherent structures are rare.

Protocells did not stop at learning four operations just to listen to the world - [they discovered how to act, to respond, in the same four-verb language](../03-functions/01-eight-functions.md).




