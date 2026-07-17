# Reinforcement Learning for Chemical Engineers: Vignettes and Vibe Coding

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ecosystem: Gymnasium & SB3](https://img.shields.io/badge/RL%20Ecosystem-Gymnasium%20%7C%20Stable%20Baselines3-brightgreen.svg)](https://gymnasium.farama.org/)

An integrated educational and practical framework designed to bridge the gap between advanced **Reinforcement Learning (RL)** methodologies and mainstream **Chemical Engineering (ChE)** curricula and industrial practice. This repository houses the curriculum outlines, interactive conceptual vignettes, AI-assisted "vibe coding" case studies, and a prototype Natural Language-to-RL (NL-to-RL) software platform.

---

## 📖 Executive Summary & Motivation

Reinforcement Learning is an autonomous machine learning paradigm where an agent learns optimal decision-making through iterative interaction with an environment, guided by reward signals that shape policy improvement over time. Unlike supervised learning, RL is inherently suited to sequential decision problems with delayed rewards and dynamic state transitions—making it a natural fit for complex chemical engineering challenges such as:

- **Process Control & Regulation:** Dynamic setpoint tracking and disturbance rejection in nonlinear chemical reactors.
- **Fed-Batch Fermentation Optimization:** Maximizing product titer while managing substrate feeds and aeration under strict biological constraints.
- **Reaction Pathway & Condition Selection:** Optimizing yield and selectivity across multi-step chemical syntheses.
- **Plant Resource Scheduling & Energy Management:** Minimizing utility costs and transitioning between operational states safely.

### The Historical Barrier
Despite its theoretical alignment with chemical engineering problems, RL has seen limited adoption in mainstream ChE curricula and industrial operations. This gap stems from:
1. **Ecosystem Complexity:** Unfamiliarity with modern software frameworks and the steep learning curve of RL libraries (e.g., OpenAI Gym / Gymnasium, Stable Baselines3, Ray RLlib).
2. **Programming Barriers:** A traditional ChE training culture that has been slow to integrate computational AI methods and software engineering best practices at the undergraduate and early graduate levels.
3. **Abstraction Gap:** Difficulty in translating mass/energy balance equations and physical constraints into Markov Decision Process (MDP) formulations (State, Action, Reward, Policy).

---

## 🎯 Our Pedagogical & Practical Framework

To overcome these barriers, this project introduces a two-pronged scaffolded approach:

```
+-----------------------------------------------------------------------------------+
|                        1. CONCEPTUAL VIGNETTES                                    |
|   Interactive simulation games (Snake, Bioreactor Game) without coding.           |
|   Builds intuitive mastery of State, Action, Reward, and Policy interaction loops. |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
|                        2. AI-ASSISTED "VIBE CODING"                               |
|   Translating natural language process descriptions into executable Python code.  |
|   Iterative human-AI co-authoring of Gymnasium environments and SB3 pipelines.     |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
|                        3. AUTOMATED NL-TO-RL PLATFORM                             |
|   A code-minimal rapid prototyping tool converting plain English process          |
|   specifications directly into deployable, constraint-aware RL controllers.       |
+-----------------------------------------------------------------------------------+
```

### 1. Conceptual Vignettes (No-Code Scaffolding)
Before writing code, students interact with graphical simulation environments where they observe the agent-environment-reward loop in real time. By experimenting with intuitive environments (such as the classic **Snake Game**) and domain-specific simulations (an **Interactive Bioreactor Game**), learners gain visceral intuition for:
- **State Space ($S$):** How physical variables (biomass, substrate concentration, dissolved oxygen) define system status.
- **Action Space ($A$):** How control inputs (feed rate, agitation, aeration) alter the environment.
- **Reward Function ($R$):** How immediate and delayed feedback guide policy convergence.
- **Policy ($\pi$):** The mapping from observed states to control actions.

### 2. AI-Assisted "Vibe Coding"
Colloquially termed **"vibe coding,"** large language model (LLM)-assisted code generation democratizes applied RL. Learners articulate chemical process behaviors and constraints in natural language, iteratively co-authoring functional environments and training scripts with AI coding assistants (e.g., GitHub Copilot, Claude, ChatGPT, Cursor). This reduces the time from conceptual problem formulation to a working RL prototype by an order of magnitude.

---

## 🏗️ Total Repository Structure

The repository is organized into distinct, modular directories reflecting the curriculum, pedagogical tools, case studies, automated platform, and test suites. *(Note: Document structures and skeletons are pre-configured to facilitate guided development and modular contributions).*

```text
RL_course_design/
├── curriculum/
│   ├── modules/
│   │   ├── 01_rl_foundations/              # Core MDP theory, exploration vs. exploitation
│   │   ├── 02_vibe_coding_methodology/     # LLM prompting workflows & human-AI collaboration
│   │   └── 03_che_problem_formulation/     # Translating ChE problems into RL frameworks
│   └── presentations/                      # Conference planning decks and lecture slide outlines
│
├── vignettes/                              # No-code / low-code interactive learning environments
│   ├── 01_snake_game/                      # Classic game introducing trial-and-error learning
│   ├── 02_bioreactor_optimization/         # Interactive fed-batch fermentation simulation game
│   └── 03_process_control_scheduling/    # Visual process control and resource management demo
│
├── vibe_coding/                            # Case studies, prompt libraries, and AI workflows
│   ├── case_studies/
│   │   ├── case_1_snake_game_strategy/     # Dynamic strategy acquisition via LLM-assisted code
│   │   ├── case_2_fed_batch_fermentation/  # Maximizing product titer under biological constraints
│   │   └── case_3_reaction_pathway_selection/ # Yield & selectivity optimization in synthesis
│   ├── prompt_templates/                   # Reusable prompt patterns for environment & reward design
│   └── workflows/                          # Step-by-step verification, validation & debugging guides
│
├── platform/                               # Prototype NL-to-RL Automated Generation Platform
│   ├── nlp_engine/                         # Natural language parser and prompt construction
│   ├── env_generator/                      # Automated Gymnasium environment & constraint builder
│   ├── training_pipeline/                  # Stable Baselines3 integration & hyperparameter tuning
│   ├── simulation_visualization/           # Real-time simulation plotting & interactive dashboards
│   ├── evaluation_deployment/              # Policy evaluation metrics and controller export tools
│   └── config/                             # Platform configuration and model settings
│
├── tests/                                  # Comprehensive unit and integration test suites
│   ├── test_platform/                      # Parser, generator, and pipeline verification
│   ├── test_vignettes/                     # Environment mechanics and physics validation
│   └── test_case_studies/                  # Convergence and reward shaping tests for case studies
│
├── docs/                                   # Architectural guides, API references & pedagogical theory
├── requirements.txt                        # Python package dependencies
├── pyproject.toml                          # Modern Python project build configuration
└── .gitignore                              # Version control exclusion rules
```

---

## 🔬 Case Studies

### Case Study 1: Vibe-Coded Game Environment (Snake Strategy)
- **Objective:** Establish foundational intuition for sequential decision-making and delayed rewards.
- **Approach:** Students prompt an LLM to build a grid-based Snake game using Gymnasium. They experiment with reward shaping (e.g., penalizing step duration vs. rewarding food consumption) to observe how reward structures dictate agent behavior and risk tolerance.

### Case Study 2: Vibe-Coded Bioprocess Simulation (Fed-Batch Fermentation)
- **Objective:** Solve an authentic chemical engineering optimization problem mirroring industrial biomanufacturing.
- **State Variables:** Biomass concentration ($X$), Substrate concentration ($S$), Product titer ($P$), Dissolved Oxygen ($DO$), and Bioreactor Volume ($V$).
- **Action Variables:** Substrate feed rate ($F_s$), Agitation speed ($N$), and Aeration rate ($Q_{in}$).
- **Constraints:** Maximum vessel volume, critical dissolved oxygen thresholds ($DO \ge DO_{crit}$), and metabolic inhibition limits.
- **Reward Function:**
  $$\mathcal{R}_t = w_1 \cdot \Delta P_t - w_2 \cdot F_{s,t} - w_3 \cdot \max(0, DO_{crit} - DO_t)$$
- **Outcome:** The RL agent discovers non-trivial feeding strategies that outperform static empirical feeding schedules while strictly respecting cellular oxygen demand.

---

## 🛠️ The Proposed Prototype Platform

To democratize RL beyond pedagogical exercises, we introduce an automated **Natural Language-to-RL (NL-to-RL)** prototyping platform. Designed for practicing chemical engineers with minimal software engineering backgrounds, the platform executes an end-to-end automated workflow:

```
[Natural Language Process Description]
                 │
                 ▼
     [NLP Problem Understanding]
                 │
                 ▼
[Automatic Gymnasium Env Generation]
                 │
                 ▼
     [Training Code Generation]
                 │
                 ▼
   [Simulation & Visualization]
                 │
                 ▼
 [Policy Evaluation & Deployment]
```

### Key Platform Capabilities
1. **Automated State & Action Mapping:** Extracts continuous/discrete physical variables and operating bounds from text descriptions.
2. **Physics & Mass-Balance Integration:** Embeds differential equations (e.g., Monod kinetics, Arrhenius rates) directly into the step-update loop.
3. **Constraint-Aware Reward Shaping:** Automatically penalizes physical violations (e.g., temperature overshoots, pressure spikes).
4. **Seamless SB3 Execution:** Spawns training pipelines using state-of-the-art algorithms (PPO, SAC, TD3) with automated evaluation dashboards.

---

## 🧭 Formulating ChE Problems as RL: The Decision Tree

Not every chemical engineering problem requires Reinforcement Learning. Use the following framework before initiating an RL project:

```
Is the problem dynamic and evolving over time?
  ├── NO  ──► Use Static Optimization, Regression, or Supervised Learning.
  └── YES
       │
       ▼
Does the system require a sequence of decisions where current actions affect future states?
  ├── NO  ──► Use Time-Series Forecasting or Model Predictive Control (MPC) with static horizon.
  └── YES
       │
       ▼
Are the underlying dynamics highly nonlinear, uncertain, or difficult to model analytically?
  ├── NO  ──► Traditional Linear/Nonlinear MPC may be sufficient and easier to certify.
  └── YES ──► 🌟 IDEAL CANDIDATE FOR REINFORCEMENT LEARNING!
```

### 10-Step ChE-to-RL Conversion Workflow
1. **Identify Objective:** Define the economic, safety, or yield target (e.g., maximize selectivity).
2. **Define Environment:** Specify the physical boundaries and simulation engine (e.g., Python ODE solver, Aspen Plus, OpenFOAM).
3. **Define States ($S$):** Select observable variables (temperatures, pressures, concentrations).
4. **Define Actions ($A$):** Select manipulated variables (valve positions, heat duty, feed flow rates).
5. **Define Rewards ($R$):** Formulate mathematical feedback balancing primary goals against operational costs.
6. **Identify Constraints:** Establish hard safety interlocks and physical bounds.
7. **Verify Simulation Availability:** Ensure a fast, numerically stable simulation is available for trial-and-error interaction ($>10^4$ episodes).
8. **Set Termination Criteria:** Define episode end conditions (batch completion time, safety interlock trip).
9. **Select Training Algorithm:** Choose appropriate continuous-action algorithms (e.g., SAC, PPO, DDPG).
10. **Evaluate & Deploy:** Assess policy robustness against process disturbances and sensor noise before plant deployment.

---

## 💻 Vibe Coding Best Practices & Methodology

When leveraging AI coding assistants for chemical engineering RL tasks, adhering to structured human-AI collaboration principles is vital to prevent subtle physical or algorithmic errors.

### ✅ Best Practices (The Do's)
- **Modular Prompting:** Break the problem into isolated components. Prompt for the ODE simulation class first, verify mass balances, then prompt for the Gymnasium wrapper, and finally the training script.
- **Iterative Refinement:** Start with a simplified linear model or reduced state space. Validate agent convergence before adding thermodynamic complexity or multi-variable constraints.
- **Rigorous Component Testing:** Create unit tests for every AI-generated function—especially step transitions and reward calculations.
- **Physics Verification:** Ensure generated code strictly obeys conservation of mass, energy, and momentum.
- **AI Debugging:** Use LLMs to interpret complex PyTorch/SB3 stack traces and explain unexpected policy divergence.

### ❌ Common Pitfalls (The Don'ts)
- **Blind Trust:** Never assume AI-generated reward functions or kinetic equations are physically accurate without mathematical verification.
- **Monolithic Prompts:** Avoid asking an LLM to generate an entire multi-reactor RL training pipeline in a single prompt; this leads to severe hallucination and unmaintainable code.
- **Ignoring Hallucinations:** Watch for invented Gymnasium API methods or deprecated OpenAI Gym syntax (`step()` returning 4 items instead of 5 in modern Gymnasium).
- **Overlooking Domain Constraints:** Do not allow neural network outputs to directly command physical actuators without clipping and safety wrappers.

---

## 🚀 Getting Started

### Prerequisites
- **Python:** Version 3.10 or higher.
- **Virtual Environment:** Recommended (`venv` or `conda`).

### Installation (Placeholder Guide)
```bash
# Clone the repository
git clone https://github.com/Sakib1418/RL_course_design.git
cd RL_course_design

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate

# Install core dependencies (when populated)
pip install -r requirements.txt
```

---

## 🗺️ Roadmap & Future Work

- [ ] **Phase 1: Curriculum & Vignette Population**
  - Complete interactive Python scripts for the Bioreactor and Snake Game vignettes.
  - Finalize conference presentation slides and detailed lecture notes.
- [ ] **Phase 2: Case Study Benchmarking**
  - Benchmark vibe-coded SAC and PPO policies against traditional PID and MPC controllers for fed-batch fermentation.
- [ ] **Phase 3: Prototype Platform Alpha Release**
  - Implement the natural language schema parser and Gymnasium environment builder.
  - Integrate web-based Streamlit/Gradio visualization dashboards for real-time training monitoring.
- [ ] **Phase 4: Educational Deployment & Assessment**
  - Pilot the framework in undergraduate/graduate process control and AI courses.
  - Evaluate pedagogical efficacy and reductions in prototyping time.

---

## 👥 Contributing

We welcome contributions from chemical engineering educators, RL researchers, and software developers! Please refer to the modular folder structure when submitting pull requests or opening issues. Ensure that all new environments adhere to modern `Gymnasium` standards and include comprehensive unit tests.

---

## 📄 License

This project is licensed under the MIT License. See the repository root for details.

---
*Co-authored by the AI & Chemical Engineering Education Initiative.*
