from src.verification.nli_verifier import NLIVerifier

context = ("Google developed BERT.")

answer = ("Google developed BERT.")

verifier = NLIVerifier()

result = verifier.verify(context,answer)

print(result)