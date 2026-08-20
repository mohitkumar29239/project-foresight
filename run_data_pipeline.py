"""Execute the Project FORESIGHT data pipeline from one command."""

from pathlib import Path
import subprocess
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
NOTEBOOK_PATH = NOTEBOOK_DIR / "01_Data_Engineering_Validation.ipynb"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

MAIN_OUTPUTS = [
    "sales_daily_final.csv",
    "calendar_final.csv",
    "sku_master_final.csv",
    "inventory_snapshots_final.csv",
]

SCOPE_OUTPUT = "development_sku_scope.csv"


def create_development_scope() -> None:
    """Create the validated 300-SKU development-scope file."""

    sales_file = (
        PROCESSED_DATA_DIR
        / "sales_daily_final.csv"
    )

    sales_scope_source = pd.read_csv(
        sales_file,
        usecols=["sku_id"],
    )

    development_scope = (
        sales_scope_source
        .drop_duplicates()
        .sort_values("sku_id")
        .reset_index(drop=True)
    )

    assert len(development_scope) == 300, (
        "Expected exactly 300 development SKUs."
    )

    assert development_scope["sku_id"].is_unique, (
        "Duplicate SKU identifiers were detected."
    )

    assert development_scope["sku_id"].notna().all(), (
        "Missing SKU identifiers were detected."
    )

    scope_file = (
        PROCESSED_DATA_DIR
        / SCOPE_OUTPUT
    )

    development_scope.to_csv(
        scope_file,
        index=False,
    )


def main() -> None:
    """Execute Notebook 01 and verify all pipeline outputs."""

    print("=" * 70)
    print("PROJECT FORESIGHT — DATA PIPELINE")
    print("=" * 70)

    if not NOTEBOOK_PATH.exists():
        raise FileNotFoundError(
            f"Notebook not found: {NOTEBOOK_PATH}"
        )

    print(f"Notebook: {NOTEBOOK_PATH}")
    print("Starting clean notebook execution...")
    print("This process may take several minutes.\n")

    command = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.timeout=-1",
        NOTEBOOK_PATH.name,
    ]

    completed_process = subprocess.run(
        command,
        cwd=NOTEBOOK_DIR,
        check=False,
    )

    if completed_process.returncode != 0:
        raise RuntimeError(
            "Notebook execution failed. Review the error shown above."
        )

    missing_main_outputs = [
        file_name
        for file_name in MAIN_OUTPUTS
        if not (PROCESSED_DATA_DIR / file_name).exists()
    ]

    if missing_main_outputs:
        raise FileNotFoundError(
            "Expected outputs are missing: "
            f"{missing_main_outputs}"
        )

    create_development_scope()

    all_outputs = MAIN_OUTPUTS + [SCOPE_OUTPUT]

    missing_outputs = [
        file_name
        for file_name in all_outputs
        if not (PROCESSED_DATA_DIR / file_name).exists()
    ]

    if missing_outputs:
        raise FileNotFoundError(
            "Pipeline outputs are missing: "
            f"{missing_outputs}"
        )

    print("\n" + "=" * 70)
    print("✅ DATA PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("Verified outputs:")

    for file_name in all_outputs:
        output_path = PROCESSED_DATA_DIR / file_name
        file_size_mb = output_path.stat().st_size / (1024 ** 2)

        print(
            f"- {file_name} "
            f"({file_size_mb:.2f} MB)"
        )


if __name__ == "__main__":
    main()
