# grid.py
import numpy as np
import random
import json

class Cell:
    def __init__(self):
        self.energy = 0.0
        self.script = []
        self.memory = {}
        self.pointer = 0
        self.active = False

    def is_empty(self):
        return not self.active

    def to_dict(self):
        return {
            'energy': self.energy,
            'script': self.script,
            'memory': self.memory,
            'pointer': self.pointer,
            'active': self.active
        }

    def from_dict(self, data):
        self.energy = data['energy']
        self.script = data['script']
        self.memory = data['memory']
        self.pointer = data['pointer']
        self.active = data['active']

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(height)] for _ in range(width)]

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[x][y]
        return None

    def set_cell_script(self, x, y, script):
        cell = self.get_cell(x, y)
        if cell:
            cell.script = script
            cell.pointer = 0
            cell.active = True

    def set_cell_energy(self, x, y, energy):
        cell = self.get_cell(x, y)
        if cell:
            cell.energy = energy

    def diffuse_energy(self, decay_rate=0.01, diffusion_rate=0.1):
        temp_energy = np.zeros((self.width, self.height))
        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[x][y]
                total_energy = cell.energy * (1 - decay_rate)
                neighbors = self.get_neighbors(x, y)
                share = total_energy * diffusion_rate / len(neighbors) if neighbors else 0
                for nx, ny in neighbors:
                    temp_energy[nx][ny] += share
                cell.energy = total_energy * (1 - diffusion_rate)
        for x in range(self.width):
            for y in range(self.height):
                self.cells[x][y].energy += temp_energy[x][y]

    def get_neighbors(self, x, y):
        deltas = [(-1,0), (1,0), (0,-1), (0,1)]
        return [(x+dx, y+dy) for dx, dy in deltas if 0 <= x+dx < self.width and 0 <= y+dy < self.height]

    def step_cell(self, x, y):
        cell = self.get_cell(x, y)
        if not cell or not cell.active or not cell.script:
            return

        if cell.energy <= 0:
            cell.active = False
            cell.script = []
            cell.memory.clear()
            return

        op = cell.script[cell.pointer % len(cell.script)]
        cell.pointer += 1
        cell.energy -= 0.1  # Fixed cost per op

        if op == "MOVE_RANDOM":
            neighbors = self.get_neighbors(x, y)
            if not neighbors:
                return
            nx, ny = random.choice(neighbors)
            target = self.get_cell(nx, ny)
            if target and target.is_empty():
                target.script = cell.script.copy()
                target.pointer = 0
                target.memory = cell.memory.copy()
                target.energy = cell.energy / 2
                target.active = True
                cell.energy /= 2

        elif op == "TRANSFER_ENERGY":
            neighbors = self.get_neighbors(x, y)
            if not neighbors:
                return
            nx, ny = random.choice(neighbors)
            target = self.get_cell(nx, ny)
            if target:
                amount = cell.energy * 0.5
                target.energy += amount
                cell.energy -= amount

        elif op == "COPY_SCRIPT":
            neighbors = self.get_neighbors(x, y)
            if not neighbors:
                return
            nx, ny = random.choice(neighbors)
            target = self.get_cell(nx, ny)
            if target and target.is_empty():
                target.script = cell.script.copy()
                target.pointer = 0
                target.memory = {}
                target.energy = 0.1
                target.active = True

    def save_to_file(self, filename):
        data = {
            'width': self.width,
            'height': self.height,
            'cells': [[self.cells[x][y].to_dict() for y in range(self.height)] for x in range(self.width)]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        grid = cls(data['width'], data['height'])
        for x in range(grid.width):
            for y in range(grid.height):
                grid.cells[x][y].from_dict(data['cells'][x][y])
        return grid