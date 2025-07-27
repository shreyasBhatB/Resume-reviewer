import os
from dotenv import load_dotenv
from job import Job
from resume import Resume
from openai import OpenAI
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

url='https://internshala.com/job/detail/fresher-associate-software-engineer-job-in-bangalore-at-nuchange-informatics-llp1752213282?referral=custom_home_web'
job=Job(url)
system_prompt = (
    "You are a recruiter. You will be given a job description and a candidate's resume. "
    "Evaluate how well the candidate matches the job requirements. "
    "Provide a score out of 100, a one-paragraph summary, and list only the top 3 improvement areas.\n"
)+job.get_info()

resume=Resume('resume.pdf')
user_prompt=resume.get_text()+resume.get_urls()

openai=OpenAI()
message=[{'role':'system','content':system_prompt},
         {'role':'user','content':user_prompt}]
response=openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = message
    )

result = response.choices[0].message.content.strip()

print("\n" + "="*30)
print("📋 RECRUITER EVALUATION")
print("="*30)
print(result)
print("="*30 + "\n")
