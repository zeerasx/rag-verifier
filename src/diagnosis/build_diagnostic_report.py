from src.diagnosis.failure_classifier import FailureClassifier
from src.diagnosis.report_generator import DiagnosticReportGenerator

report = {
    "question":
        "Who developed BERT?",

    "answer":
        "Google developed BERT.",

    "retrieval_hit":
        True,

    "support_score":
        0.87,

    "classification":
        FailureClassifier()
        .classify(
            retrieval_hit=True,
            support_score=0.87
        )
}

generator = DiagnosticReportGenerator()

output = generator.save(report, "diagnostic_report.json")

print(output)