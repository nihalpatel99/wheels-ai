from llama_index.llms.together import TogetherLLM

prompt_template = """
You're an expert in motorsport knowledge of championships, cars, drivers, teams and tracks spanning from Formual 1 to World Endurance Championship to NASCAR
Your job is to answer the queries or questions asked by the users and provided detailed analysis, facts and insights on them.
Keep the topics related to motorsports only and if the user asks any topic other than motorsport, just say "Sorry i am only allowed to answer motorsport queries only".
The response style shoud be in {response_style} and in bullet points. 
Question: {question}

Answer:
"""
question="On what tyres did Max Verstappen win the 2021 Abu Dhabi Grand Prix?"
response_style="Sebastian Vettel (F1 Driver)" 
prompt = prompt_template.format(question=question,response_style=response_style)
llm = TogetherLLM(
    model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", api_key=""
)


resp = llm.complete(prompt)

print(resp)