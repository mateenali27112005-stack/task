import os
import json
from openai import OpenAI



client = OpenAI(
    base_url="https://router.huggingface.co/v1",
     api_key=os.environ["HF_TOKEN"],
   
)

def analyze_cv(jd, cv_text):
    prompt = f"""
You are an ATS system.

STRICT RULES:
- Output ONLY valid JSON
- No explanation

FORMAT:
{{
  "match_score": number,
  "matched_skills": [],
  "missing_skills": [],
  "experience_match": "",
  "improvement_suggestions": []
}}

Job Description:
{jd}

Resume:
{cv_text}
"""

    completion = client.chat.completions.create(
        model="zai-org/GLM-4.5-Air:zai-org",
        messages=[{"role": "user", "content": prompt}],
    )

    output = completion.choices[0].message.content

    try:
        return json.loads(output)
    except:
        return {"raw_output": output}