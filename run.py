# run.py
import argparse
from core.sim import run_simulation

def main():
    parser = argparse.ArgumentParser(description="Artificial Life Simulator")

    parser.add_argument("--file", type=str, default="simstate.txt",
                        help="File to save/load simulation state")
    parser.add_argument("--max_ticks", type=int, default=0,
                        help="Maximum number of ticks to run (0 = infinite)")
    parser.add_argument("--save_interval", type=int, default=0,
                        help="Ticks between saving to file (0 = no saving)")
    parser.add_argument("--width", type=int, default=64,
                        help="Grid width")
    parser.add_argument("--height", type=int, default=64,
                        help="Grid height")

    args = parser.parse_args()

    run_simulation(
        filename=args.file,
        max_ticks=args.max_ticks,
        save_interval=args.save_interval,
        width=args.width,
        height=args.height
    )

if __name__ == "__main__":
    main()
