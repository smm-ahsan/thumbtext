#!/usr/bin/env python3
"""ThumbText - generate short, punchy thumbnail headlines for videos.

Thumbnails convert in about a second, so the text has to land fast:
three to five bold words beat a full sentence every time. ThumbText takes
a topic, drops it into proven headline patterns and prints each idea with
its word count, flagging anything long enough to hurt readability.

Standard library only. No dependencies.
"""

import argparse
import random
import sys

TOPIC_TEMPLATES = [
    "{Topic} Changed Everything",
    "Stop Doing {Topic} Wrong",
    "The Truth About {Topic}",
    "{Topic}: Day 1 vs Day 30",
    "Why {Topic} Fails",
    "I Quit {Topic}...",
    "{Topic} in 24 Hours!",
    "Nobody Talks About {Topic}",
    "{Topic} Mistakes Kill Results",
    "Try {Topic} Like This",
]

GENERIC_TEMPLATES = [
    "Nobody Expected THIS",
    "Watch Before You Try",
    "This Changes Everything",
    "Day 1 vs Day 30",
]

TEMPLATES = TOPIC_TEMPLATES + GENERIC_TEMPLATES


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate short, punchy thumbnail headlines for a video topic."
    )
    parser.add_argument("--topic", required=True, help="Video topic, e.g. 'morning fishing'.")
    parser.add_argument("--count", type=int, default=6,
                        help="How many headlines to print (default 6).")
    parser.add_argument("--seed", type=int, default=1,
                        help="Random seed for reproducible picks (default 1).")
    args = parser.parse_args(argv)

    if args.count < 1:
        parser.error("--count must be at least 1")
    if args.count > len(TEMPLATES):
        print(
            f"error: --count {args.count} is more than the {len(TEMPLATES)} "
            "templates in the bank; lower --count.",
            file=sys.stderr,
        )
        return 2

    topic = args.topic.title()
    rng = random.Random(args.seed)
    picked = rng.sample(TEMPLATES, args.count)

    for template in picked:
        headline = template.format(Topic=topic)
        words = len(headline.split())
        line = f"{headline}  ({words} words)"
        if words > 6:
            line += " - long, consider trimming"
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
