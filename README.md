# The Excuse an AI Agent Gives Its Human

[![Competition](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/ZQ051031/excuse-ai-agent-human-20261124/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/ZQ051031/excuse-ai-agent-human-20261124/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

One line: the funniest excuse an AI agent could give its human.

> I didn't miss your deadline — I delegated it to a subagent, who delegated it to another subagent, who is currently on holiday.

`main.py` (Python standard library only, no network) writes the line to `/output/entry.txt`. Running it twice produces byte-identical output.

## How it works

1. `ENTRY` holds the single excuse line (126 characters, inside the 200-character cap).
2. The script asserts the cap before writing, so a future edit can never silently break the limit.
3. It creates `/output` if needed and writes the line plus a trailing newline.

## License

MIT
