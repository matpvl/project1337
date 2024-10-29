# PROJECT1337

A brief demonstration of celery, redis, flower.

---

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone <https://github.com/matpvl/project1337.git>
   cd <project1337>
   ```

---

## Installation

1. **Install Poetry:**  
   Follow the instructions [here](https://python-poetry.org/docs/#installation).

2. **Activate Poetry Environment:**
   ```bash
   poetry install
   poetry shell
   ```

---

## Development Workflow

1. **Run Build Script (it's important to run the build locally before pushing changes):**
   ```bash
   invoke build-local
   ```

2. **Format Code with Black:**
   ```bash
   invoke black
   ```

---

## Running the Application

1. **Build and Start Services with Docker:**
   ```bash
   docker compose up --build
   ```