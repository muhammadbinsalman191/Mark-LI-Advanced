# Contributing to Mark-LI Advanced

Thanks for your interest in contributing.

Mark-LI Advanced is a maintained derivative of **FatihMakes/Mark-LI**. Please keep upstream attribution intact and make it clear whether a change is inherited from upstream or introduced in this repository.

## Before opening a pull request

1. Search existing Issues and pull requests.
2. Create a focused branch for one bug fix or feature.
3. Keep secrets and personal runtime data out of commits.
4. Test the affected behavior.
5. Update documentation when behavior or setup changes.

## Recommended branch workflow

```bash
git checkout jarvis-advanced
git pull
git checkout -b fix/short-description
```

For features:

```bash
git checkout -b feat/short-description
```

## Commit guidance

Prefer small, descriptive commits, for example:

```text
fix: prevent duplicate UI mode transition
feat: add command center status indicator
docs: clarify upstream attribution
test: cover UI mode tool dispatch
```

## Pull request checklist

- [ ] The change is scoped and understandable
- [ ] I tested the affected behavior
- [ ] I did not commit API keys, tokens, private files, or personal memory
- [ ] I updated docs where necessary
- [ ] I preserved upstream attribution
- [ ] I explained whether the change is inherited, adapted, or original to this derivative
- [ ] New dependencies are documented

## Reporting bugs

Please use the Bug Report issue template and include:

- operating system
- Python version
- branch / commit
- exact reproduction steps
- expected behavior
- actual behavior
- relevant logs with secrets removed

## Requesting features

Please use the Feature Request template. Explain the problem first, then the proposed solution.

Good feature requests are specific, testable, and useful beyond one one-off setup.

## Code and privacy expectations

Never commit:

- API keys
- access tokens
- passwords
- private certificates
- personal memory files
- local configuration containing credentials

If you accidentally commit a secret, revoke/rotate it immediately; deleting it in a later commit is not enough to remove it from Git history.

## Licensing / attribution

This project contains code derived from FatihMakes/Mark-LI. Contributions must respect the applicable upstream terms and attribution requirements.

Submitting a contribution does not remove upstream ownership or attribution.
