import sys
import json
from parser_agent.parser import parse_resume

if __name__ == "__main__":
    resume_input = sys.argv[1] if len(sys.argv) > 1 else "karan_resume (1).pdf"

    try:
        result = parse_resume(resume_input)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print("❌ Error parsing resume:", str(e))
