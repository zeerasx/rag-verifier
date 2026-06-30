from src.evaluation.answer_metrics import (exact_match,f1_score)

prediction = ("Google developed BERT")

reference = ("Google developed BERT")

print("EM:",exact_match(prediction,reference))
print("F1:",f1_score(prediction,reference)

)