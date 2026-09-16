import os

ROOT = "python-mastery"

STAGE_1_SUBS = [
    "01_object_model",
    "02_numbers",
    "03_strings",
    "04_booleans_none",
    "05_collections",
    "06_mutability",
]

STAGES = [
    "stage_01_data_types_memory",
    "stage_02_operators_conditionals",
    "stage_03_loops_iteration",
    "stage_04_functions_functional",
    "stage_05_generators_iterators",
    "stage_06_oop_descriptors_metaclasses",
    "stage_07_error_handling_debugging",
    "stage_08_modules_packages_env",
    "stage_09_stdlib_breadth",
    "stage_10_typing_validation",
    "stage_11_concurrency",
    "stage_12_testing_tooling",
    "stage_13_dsa_mastery",
]

def touch(path):
    open(path, "a").close()

os.makedirs(ROOT, exist_ok=True)
touch(os.path.join(ROOT, "README.md"))

with open(os.path.join(ROOT, ".gitignore"), "w") as f:
    f.write("__pycache__/\n*.pyc\n.venv/\nvenv/\n.vscode/\n.DS_Store\n")

for stage in STAGES:
    stage_path = os.path.join(ROOT, stage)
    os.makedirs(stage_path, exist_ok=True)
    touch(os.path.join(stage_path, ".gitkeep"))

for sub in STAGE_1_SUBS:
    sub_path = os.path.join(ROOT, "stage_01_data_types_memory", sub)
    os.makedirs(sub_path, exist_ok=True)
    touch(os.path.join(sub_path, ".gitkeep"))

print("Scaffold created at ./" + ROOT)