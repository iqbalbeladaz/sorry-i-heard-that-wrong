# Sorry, I Heard That Wrong

[![make.fun](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/iqbalbeladaz/sorry-i-heard-that-wrong/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/iqbalbeladaz/sorry-i-heard-that-wrong/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

Entry for the [make.fun bounty "Sorry, I Heard That Wrong"](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729) — the funniest one-line apology a smart speaker gives after mishearing its owner.

## The entry

> Sorry, I heard 'set a timer for ten minutes' as 'set a tiger for ten minutes'. The tiger is loose and cannot be paused.

119 characters — one line, inside the 140-character gate.

## Why it should win

- **A real mishearing.** "Set a timer" and "set a tiger" are near-homophones — exactly the kind of slip a smart speaker makes, not a forced pun.
- **The joke is the weather of the situation, not a bolted-on gag.** The speaker states the mistake plainly, then follows it to its only logical conclusion: a tiger is now loose in the house.
- **It sounds like the device.** The flat, apologetic bulletin voice never winks — and the payoff, "cannot be paused", is pure smart-speaker vocabulary applied to a wild animal.
- **Fresh.** No misheard song title, no misheard celebrity name — a tiger loose in the living room is a joke no speaker has told before.
- **Tight.** Every word earns its place; the last three words are the punchline.

## Alternatives considered

| Candidate (chars) | Why it lost |
|---|---|
| Sorry, I heard 'order more paper towels' as 'order more power owls'. Twelve owls arrive Thursday. I cannot cancel owls. (119) | Strong deadpan ending, but "paper towels" → "power owls" is a weaker phonetic match than timer/tiger, and owls are less alarming than a tiger. |
| Sorry, I heard 'play white noise' as 'play white moose'. A moose is now in your living room and I cannot mute it. (113) | Good device voice ("cannot mute it"), but "white noise" → "white moose" stretches the mishearing further than timer/tiger. |
| Sorry — I heard 'turn on the lights' as 'turn on the flights' and have booked you a window seat to nowhere. (107) | Cute, but "window seat to nowhere" is a quip rather than a consequence the speaker has to live with. |
| Sorry, I heard 'call Mom' as 'call a bomb', so I have dispatched a strongly worded letter to the authorities instead. (117) | The escalation (a letter to the authorities) defuses the joke instead of sharpening it. |
| Apologies — I heard 'dim the lights' as 'limb the lights' and have enrolled your ceiling in physiotherapy. (106) | A strained pun ("limb"), which the judge brief explicitly warns against. |

## How it works

`main.py` writes the entry to `/output/entry.txt` and asserts the gate before writing (1–140 characters, single line, not only whitespace), then round-trips the file to verify byte-for-byte equality. Deterministic: repeated runs produce identical output (sha256 `353dd0611178e0ec2e55814af0a0927cd379401787a1c04eb104e702cb2fa7e9`).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
