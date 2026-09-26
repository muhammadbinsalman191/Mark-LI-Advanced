# Mark-LI Advanced Roadmap

This roadmap describes goals for the **Mark-LI Advanced derivative**, not the upstream MARK LI roadmap.

Items are intentionally written as plans rather than claims that they already exist.

## Phase 1 — Repository clarity

- [x] Preserve upstream attribution
- [x] Maintain custom work on `jarvis-advanced`
- [x] Replace the inherited README with derivative-specific documentation
- [x] Add real screenshots from the current build
- [x] Add contributor guidance
- [x] Add issue templates
- [x] Document derivative changes more clearly
- [x] Make `jarvis-advanced` the default branch or merge the stable derivative into `main`

## Phase 2 — Reliability and testing

- [x] Create repeatable smoke tests for startup
- [ ] Test tool dispatch failures cleanly
- [ ] Test Core / Command Center mode transitions
- [ ] Add regression checks for memory/config privacy
- [x] Document supported Python versions
- [ ] Document platform-specific limitations
- [ ] Add a basic CI workflow once tests are stable

## Phase 3 — Command Center

- [ ] Refine the Command Center as a functional desktop workspace
- [ ] Keep Core Mode lightweight and focused
- [ ] Improve status/state visibility
- [ ] Improve keyboard navigation and accessibility
- [ ] Ensure UI state never claims an action succeeded when the underlying tool failed

## Phase 4 — Extensibility

- [ ] Improve plugin/developer documentation
- [ ] Add examples for safe tool integrations
- [ ] Define conventions for new actions/plugins
- [ ] Add clearer error reporting for optional integrations
- [ ] Document extension points without modifying upstream attribution

## Phase 5 — Maintainer workflow

- [x] Track bugs and requests through GitHub Issues
- [x] Use pull requests for non-trivial changes
- [ ] Add release tags / release notes for stable milestones
- [x] Maintain a changelog for derivative changes
- [ ] Review dependencies and security-sensitive integrations regularly

## Possible future work

These are ideas, not promises:

- browser-extension integration
- improved developer / coding workflows
- safer confirmation flows for sensitive actions
- stronger automated tests
- more modular UI components
- better contributor documentation
