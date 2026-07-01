import json
from pathlib import Path


OUTPUT_DIR = Path("reports")
OUTPUT_DIR.mkdir(exist_ok=True)


class DiagnosticReportGenerator:

    def save(self, report, filename):

        output_file = (
            OUTPUT_DIR
            / filename
        )

        with open(output_file,"w",encoding="utf-8") as f:

            json.dump(
                report,
                f,
                indent=2
            )

        return output_file