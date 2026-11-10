# ThumbText

A tiny open-source CLI that generates short, punchy thumbnail headline text for videos.

## Why 3-5 words?

A thumbnail is read in about a second, usually at phone size, so three to
five big words stay legible and create curiosity without giving the video away.
Longer text shrinks, blurs and gets skipped - ThumbText counts the words for
you and flags anything over six.

## Requirements

- Python 3
- Standard library only - nothing to install

## Usage

```bash
python3 thumbtext.py --topic "morning fishing" --count 6 --seed 3
```

- `--topic` (required): your video topic, inserted into the headlines in Title Case.
- `--count`: how many distinct headlines to print (default 6, maximum 14).
- `--seed`: random seed, so the same command gives the same picks (default 1).

Each line prints the headline plus its word count, and any headline over
six words gets a "long, consider trimming" note.

See `examples.md` for real captured output.

## License

MIT - see `LICENSE`.
