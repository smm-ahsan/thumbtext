# Examples

Real output from ThumbText, captured from an actual run.

## Morning fishing video, six headlines

Command:

```bash
python3 thumbtext.py --topic "morning fishing" --count 6 --seed 3
```

Output:

```
Morning Fishing: Day 1 vs Day 30  (7 words) - long, consider trimming
Try Morning Fishing Like This  (5 words)
Morning Fishing Mistakes Kill Results  (5 words)
The Truth About Morning Fishing  (5 words)
I Quit Morning Fishing...  (4 words)
Nobody Talks About Morning Fishing  (5 words)
```

Note the first headline: at 7 words it is flagged as long, because text
that size is hard to read on a small thumbnail.
