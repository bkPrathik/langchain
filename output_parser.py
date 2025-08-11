#output parsers for the model that don't support strucutred output
#string output parser, json output parser

"""Main Purpose:String Output Parser
StrOutputParser takes the output from a language model and transforms it into a simple, usable string. 
If the model’s output is already a string, the parser passes it through unchanged. 
For ChatModels that return complex objects, StrOutputParser extracts just the text content.
Common Use Cases
	•	Simplifying outputs: Converting complex model responses into plain text for easy display or further processing
	•	Standardizing formats: Normalizing outputs from different types of models
	•	Streaming applications: Particularly useful in streaming contexts where you need clean text output
	•	Chain building: Essential component in LangChain chains where you need string outputs for downstream tasks"""
 
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
 
model = ChatOllama(model='deepseek-r1:1.5b',temperature=0) 
template_1= PromptTemplate(
    template='write future events in 2035 about the {topic} as if you are time traveller',
    input_variables=['topic']
)

template_2= PromptTemplate(
    template='write 2 points summary on this {text}',
    input_variables=['text']
)

perser =StrOutputParser()

chain = template_1 | model | perser | template_2 | model |perser

result= chain.invoke({'topic':'medicine'})
print(result)