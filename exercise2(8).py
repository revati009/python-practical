import re

def moderate_feedback(feedback, target_words):
    
    pattern = r"\b(" + "|".join(map(re.escape, target_words)) + r")\b"
    
    return re.sub(pattern, "****", feedback, flags=re.IGNORECASE)

feedback = """
The product was terrible and the service was awful.
I had a bad experience with the support team.
"""
target_words = ["terrible", "awful", "bad"]

clean_feedback = moderate_feedback(feedback, target_words)

print(clean_feedback)
