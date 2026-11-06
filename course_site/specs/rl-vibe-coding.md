---
slug: rl-vibe-coding
number: 1
accent: rl
status: Built
short: RL for Chemical Engineers
nav: RL & Vibe Coding
title: Reinforcement Learning for Chemical Engineers
subtitle: Vignettes & Vibe Coding
tagline: From a no-code game to a tested fed-batch controller in seven weeks, with an AI pair-programmer at your side.
card: Teach a bioreactor to feed itself. Start with a snake game, finish with a verified reinforcement-learning controller for a fed-batch fermentation, all built by talking to an AI coding assistant.
level: Undergraduate (junior/senior) · Graduate · Professionals
prereq: None. Material balances help; no coding needed.
hero: rl-hero.svg
capstone: An RL feeding controller for a fed-batch bioreactor twin, benchmarked against an operator's recipe, stress-tested with a faulty pump, and shipped as a shareable web app.
weeks:
  - n: 1
    phase: Play
    title: Decisions, rewards and a snake
    summary: Play before equations. The snake game teaches state, action, reward and policy by hand.
    sessions:
      - Who writes the code now? AI as an engineering tool
      - "Meet the snake: state, action, reward, policy"
      - "Your AI workspace: first conversation with a coding assistant"
  - n: 2
    phase: Play
    title: From snake to bioreactor
    summary: The same loop, now feeding a fed-batch culture. When is a process problem an RL problem?
    sessions:
      - "The bioreactor game: feeding a culture by hand"
      - "Is your problem an RL problem? The process engineer's checklist"
      - "Episodes, returns, exploration: the learning loop in plain words"
  - n: 3
    phase: Build
    title: "Vibe coding: break it down"
    summary: The core habit of the course. Break the problem into pieces, one prompt and one test per piece.
    sessions:
      - What vibe coding is, and what it is not
      - "Break the problem into pieces: spec sheets for state, action, reward"
      - "One piece, one prompt, one test"
  - n: 4
    phase: Build
    title: Build the environment
    summary: Turn mass balances and Monod kinetics into a simulator, then into a Gymnasium environment.
    sessions:
      - "Mass balances as code: a fed-batch simulator with AI"
      - Wrap it as a Gymnasium environment
      - "Reward design studio: titer, constraints, penalties"
  - n: 5
    phase: Build
    title: Train the agent
    summary: PPO and SAC in plain language, a first training run, and reading learning curves.
    sessions:
      - "Algorithms in plain language: Q-learning, PPO, SAC"
      - "First training run with Stable-Baselines3"
      - "When the agent cheats: debugging rewards with AI"
  - n: 6
    phase: Verify
    title: Verify before you trust
    summary: A test ladder from units to closed loop. Beat the recipe, survive a faulty pump.
    sessions:
      - "The test ladder: units, balances, sanity bounds"
      - "Benchmark against the recipe; stress test with a faulty pump"
      - "Safety, constraints, and when not to use RL"
  - n: 7
    phase: Deploy
    title: Ship it and show it
    summary: From notebook to a shareable app, a gentle first look at Git, and the capstone showcase.
    sessions:
      - "From notebook to app: a controller dashboard"
      - "Version, document, hand off (Git through the browser)"
      - Capstone showcase and what comes next
---

# Writer brief — Course 1

**Motivation.** RL fits chemical engineering (sequential decisions, delayed rewards, dynamic states: control, fed-batch feeding, scheduling), yet it rarely appears in ChemE curricula. The barrier was never the idea; it was the software (Gymnasium, Stable-Baselines3, Python). That wall is gone: with AI coding assistants an engineer can describe a process in plain English and co-write a working environment. The instructor lived the old barrier in 2019 (building *Game of Cells*, a cell-culture twin on PyGame and the Gym interface, by hand) and published RL control for CAR T-cell expansion (Biotechnol Bioeng 2024) and fed-batch enzyme production (Biotechnol Bioeng 2026). This course compresses that path into seven weeks.

**Two halves.** *Vignettes* (Weeks 1–2): a snake game, then an interactive bioreactor game, so learners see the agent–environment–reward loop with zero code. *Vibe coding* (Weeks 3–7): one lesson repeated: **break it down → one piece, one prompt, one test → stack the pieces and test every layer.**

**Snake → bioreactor mapping (use as a table on the landing page).** Board → reactor; snake position, food location → biomass, substrate, product, volume, DO; up/down/left/right → feed pump rate (0–50 mL); eat food +1 → enzyme titer; hit the wall → overflow, substrate inhibition, oxygen limit; game over → batch end.

**Outcomes (6).** Explain RL in ChemE terms; decide if a problem is an RL problem; write a spec sheet an AI can build from; co-author and test a simulator and environment; train and benchmark an agent and diagnose reward hacking; ship a documented app.

**After the course.** Read and question RL papers in process control; prototype RL for your own unit operation; work fluently with any AI coding assistant; next: Course 2 (Digital Twins) builds a better world to train in.

**Images available:** `rl-hero.svg` (RL loop on a bioreactor), `bioreactor-rl.png` (the instructor's fed-batch RL schematic: external substrate tank, feed pump 0–50 mL, sample outlet, sensor output enzyme activity and cell concentration, RL algorithm), `pathway.svg` (Play → Build → Verify → Deploy).
