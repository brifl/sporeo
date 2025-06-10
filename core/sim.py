# sim.py
import time
from core.grid import Grid

def initialize_simulation(grid):
    starter_script = ["MOVE_RANDOM", "TRANSFER_ENERGY", "COPY_SCRIPT"]
    positions = [(10, 10), (20, 20), (30, 30)]
    for x, y in positions:
        grid.set_cell_script(x, y, starter_script)
        grid.set_cell_energy(x, y, 1.0)

def run_simulation(filename="simstate.txt", max_ticks=0, save_interval=0, width=64, height=64):
    try:
        grid = Grid.load_from_file(filename)
        print(f"Loaded simulation state from {filename}")
    except FileNotFoundError:
        print("No previous state found, initializing new simulation.")
        grid = Grid(width, height)
        initialize_simulation(grid)

    tick = 0
    while True:
        print(f"Tick {tick}")
        for x in range(grid.width):
            for y in range(grid.height):
                grid.step_cell(x, y)
        grid.diffuse_energy()

        if save_interval > 0 and tick % save_interval == 0:
            grid.save_to_file(filename)
            print(f"Saved simulation state at tick {tick}")

        tick += 1
        if max_ticks > 0 and tick >= max_ticks:
            print("Max ticks reached. Exiting.")
            break
        time.sleep(0.05)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="simstate.txt", help="File to save/load simulation state")
    parser.add_argument("--max_ticks", type=int, default=0, help="Maximum number of ticks to run (0 = infinite)")
    parser.add_argument("--save_interval", type=int, default=0, help="Ticks between saving to file (0 = no saving)")
    parser.add_argument("--width", type=int, default=64, help="Grid width")
    parser.add_argument("--height", type=int, default=64, help="Grid height")
    args = parser.parse_args()

    run_simulation(
        filename=args.file,
        max_ticks=args.max_ticks,
        save_interval=args.save_interval,
        width=args.width,
        height=args.height
    )