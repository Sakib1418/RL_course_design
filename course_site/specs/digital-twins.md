---
slug: digital-twins
number: 2
accent: twin
status: Designed
short: Digital Twins for Process Engineering
nav: Digital Twins
title: Digital Twins for Process Engineering
subtitle: Hybrid models that stay honest
tagline: Build a hybrid twin, with first-principles balances around learned parts, and keep it honest against real plant data.
card: Build a living model of a process unit. Balances and kinetics form the skeleton, machine learning fills the gaps, and live data keeps the twin honest, then you use it to ask "what if?"
level: Upper undergraduate · Graduate · Professionals
prereq: None. Material and energy balances help; no coding needed.
hero: twin-hero.svg
capstone: A hybrid digital twin of a fed-batch bioreactor or CSTR that syncs with sensor data, reports what it does not know, runs what-if scenarios, and ships as a dashboard.
weeks:
  - n: 1
    phase: Play
    title: What a twin is, and what it is not
    summary: Models, simulators and twins on one spectrum. Play with a live bioreactor twin before building one.
    sessions:
      - "Models, simulators, twins: the spectrum, and where industry is"
      - "Play: steer a live bioreactor twin in the browser"
      - "Your AI workspace and a first vibe-coded simulation: a draining tank"
  - n: 2
    phase: Build
    title: First principles in code
    summary: Mass, energy and species balances become code, and the code must conserve mass.
    sessions:
      - "Balances as code: mass, energy, species"
      - "Kinetics and ODE solvers, explained by your AI assistant"
      - "A fed-batch model that conserves mass, with a test that proves it"
  - n: 3
    phase: Build
    title: Data meets model
    summary: Sensors, messy time series and parameter estimation. Residuals tell the story.
    sessions:
      - "Sensors and time series: cleaning messy plant data with AI"
      - "Parameter estimation: fitting kinetics to data"
      - "Calibrate your model and read the residuals"
  - n: 4
    phase: Build
    title: "Hybrid twins: learned parts bounded by balances"
    summary: Where physics stops, a small neural network learns the unknown term, inside the balances.
    sessions:
      - "Where physics stops: learning the unknown term"
      - "Build a hybrid: physics skeleton, machine-learned closure"
      - "Mechanistic vs. data-only vs. hybrid, head to head"
  - n: 5
    phase: Verify
    title: Keeping the twin honest
    summary: Uncertainty, state estimation and drift. A twin must say what it does not know.
    sessions:
      - "Uncertainty: fixed, drifting and live parameters"
      - "State estimation and data assimilation: Kalman intuition"
      - "A validation protocol and a drift alarm"
  - n: 6
    phase: Verify
    title: Put the twin to work
    summary: Soft sensors, what-if scenarios, design of experiments, and a hand-off to control.
    sessions:
      - "Soft sensors and what-if scenarios"
      - "Optimization and control on the twin: the hand-off to RL and MPC"
      - "Design the next experiment with the twin"
  - n: 7
    phase: Deploy
    title: Deploy the twin
    summary: From device to cloud to dashboard, with documentation others can trust.
    sessions:
      - "Device to cloud: data pipelines and dashboards, conceptually"
      - "Package the twin as an app; document and govern it"
      - Capstone showcase
---

# Writer brief — Course 2

**Motivation.** Self-driving cars, drones and robots learn in simulators first; biology and process engineering deserve their own virtual world (poster). Industry talks about "digital twins" constantly, but most engineers have never built one, and most so-called twins are either rigid first-principles models that drift from reality or black-box ML that breaks outside its data. The defensible middle is the **hybrid twin**: balances, kinetics and transport set the bounds, learned parts fill what physics cannot, and live data keeps it honest. The instructor builds these for a living: *Game of Cells* (a cell-culture twin), a finite-element transport model (AIChE J 2021), and the physics-based twin plus device-to-cloud architecture for a wall-aerated bag bioreactor at a biomanufacturing startup (oxygen transfer kLa with CO₂, pH and evaporation terms; parameters classified fixed / drifting / live).

**Spectrum (use as a visual):** spreadsheet model → simulator → calibrated model → digital shadow (one-way data) → digital twin (two-way: data in, decisions out).

**Outcomes (6).** Tell a model from a twin; turn balances into tested code; calibrate a model to data; build a hybrid model where physics bounds the learned part; quantify uncertainty and detect drift; use and deploy a twin for what-if questions and control.

**After the course.** Build a first twin of your own unit operation; judge vendor "twin" claims; hand a trustworthy simulator to an RL or MPC controller (Course 1) or to AI agents (Course 3).

**Images available:** `twin-hero.svg` (physical reactor ↔ hybrid twin, data in, decisions out), `pathway.svg`.
