# Contributing to Awesome CUHKSZ

English | [简体中文](CONTRIBUTING.zh-CN.md)

Help someone discover something useful. New projects are welcome; popularity is not a prerequisite.

## What belongs here

- Projects with a public, verifiable CUHK-Shenzhen connection: intended campus users, an explicit course or lab connection, or an author’s voluntary public statement.
- Useful software with a README and an explicit license. Public resources without a clear license may be linked as **public resources — license unclear**, never presented as freely reusable open source.
- Original notes, public teaching resources, campus utilities, research software, and community projects with a clear purpose.

Exclude unrelated keyword matches (LGU can refer to other universities), unmodified forks when the upstream is already listed, exposed personal data, unauthorized course/exam copies, and tools whose primary purpose is bypassing access controls. Course projects must comply with applicable course sharing rules. List links and original summaries; do not mirror upstream content.

## Submit a change

1. Search both READMEs and `data/projects.json` for duplicates.
2. Add or update a record in `data/projects.json`. Include the canonical repository URL, category, concise English and Chinese summaries, public affiliation evidence, license status, star count, observation date, and latest default-branch commit URL/date. Use `null` for an unclear license; do not guess.
3. Run `python3 scripts/render.py` and `python3 scripts/check.py`.
4. Open a focused pull request explaining usefulness and providing evidence. Self-submissions are welcome; disclose ownership or collaboration.

If editing JSON is inconvenient, open an issue with the same information. Maintainers can handle the formatting. Do not add someone’s real name, student number, contact address, or inferred school affiliation. Personal developer profiles require voluntary submission; a project listing does not mean its author has joined or endorsed this list.

## Editorial policy

Maintain six categories. Sort entries by repository name within each category. Stars are dated context, not a ranking or admission threshold. Activity uses default-branch commits: within 180 days, 181–365 days, or more than 365 days from the observation date. A recent commit is a signal, not a promise of support. Archive flags override activity labels.

Review links and metadata quarterly. Investigate failures before removal; record redirects, archiving, and replacements in a PR. Remove or correct an entry on a substantiated author request. Keep both languages consistent. Maintainers may decline low-value or unverifiable submissions and should explain why.

## Community and license

Follow the [Code of Conduct](CODE_OF_CONDUCT.md). Contributions to this repository are provided under its [MIT license](LICENSE); linked projects keep their own terms. No contributor agreement or copyright transfer is required.
