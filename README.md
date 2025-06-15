# 🧬 Artificial Life Simulator

A GPU-accelerated artificial life simulation written in Python, designed for open-ended evolution in a dynamic world. Cells consume and transfer energy, execute scripts, reproduce, and mutate — allowing complex behavior and ecosystems to emerge over time.

---

## 🚀 Quick Start

```bash
# Install dependencies (recommend using virtualenv)
pip install -r requirements.txt

# Run the simulation
python run.py --file simstate.json --max_ticks 1000 --save_interval 100 --width 128 --height 128
```

---

## 🧠 Core Concepts

### World

* A 2D grid (currently single chunk, chunked worlds planned)
* Each cell can store:

  * Energy (float)
  * A script (list of instructions)
  * Memory (dict)
  * Instruction pointer and activity flag

### Biots (Agents)

* A "biot" is a living script-carrying cell (or multicell colony)
* Executes one instruction per tick
* Energy is consumed for:

  * Thinking (interpreting script)
  * Acting (e.g. moving, copying)

### Scripting Language (MVP)

* `MOVE_RANDOM` – Move to a random adjacent empty cell
* `TRANSFER_ENERGY` – Share energy with a random neighbor
* `COPY_SCRIPT` – Copy script to a neighbor cell

Scripts are short and repeated cyclically. Evolution is driven by simple logic, energy economics, and selection pressures.

---

## ⚙️ Parameters

Run the simulator with flexible control:

```bash
python run.py \
  --file simstate.json \
  --max_ticks 10000 \
  --save_interval 500 \
  --width 128 \
  --height 128
```

| Flag              | Description                    |
| ----------------- | ------------------------------ |
| `--file`          | Save/load simulation state     |
| `--max_ticks`     | Ticks to run (0 = infinite)    |
| `--save_interval` | Save every N ticks (0 = never) |
| `--width`         | Grid width                     |
| `--height`        | Grid height                    |

---

---

## 🔭 Roadmap

* [ ] Multicellular beings (adjacent cooperating cells)
* [ ] Mutation rates that evolve
* [ ] Natural terrain and energy hotspots
* [ ] Lineage/speciation tracking
* [ ] Web-based UI with slice view & playback
* [ ] Chunked infinite worlds (Minecraft-style)
* [ ] Energy recycling via decay
* [ ] Modular scripting language design
* [ ] Visualization snapshots or live stats

---

## ❤️ Philosophy

Inspired by the principles of artificial life, evolutionary theory, and decentralized computation:

* Life emerges from local rules and global constraints
* Intelligence is costly, distributed, and embodied
* Mutation and selection can produce open-ended complexity

This is not a game — it’s a platform for studying how life might evolve under different rules. Let's simulate life.

---

## 🤝 Contributing

This project is open to collaborators! We welcome contributors interested in:

* Simulation engine optimization (NumPy, Numba, CuPy)
* Web visualization (React/Svelte, WebSockets)
* Agent-based modeling and evolution

Ping us via GitHub issues or start hacking on a module.

---

## 📄 License

MIT License — free to use, remix, and evolve.

---

## 🌱 Maintainers

Built by brifl and ChatGPT in co-development mode. Vibe coding FTW.

> "Complexity is what happens when simple things have to get clever to survive."

---
