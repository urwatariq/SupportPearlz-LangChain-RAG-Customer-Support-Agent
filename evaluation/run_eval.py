import json
from pathlib import Path
cases=json.loads((Path(__file__).parent/'test_questions.json').read_text())
print(json.dumps({'total':len(cases),'note':'Run this harness with a configured API key and record observed verdicts honestly.'},indent=2))
