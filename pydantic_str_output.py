from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel ,Field
#gemma3:4b
model = ChatOllama(model='qwen3:8b',temperature=0) 
class review(BaseModel):
    
    proper_headline:str=Field(description='give it a proper nice headline')
    summary:str= Field(description='generate 2 line summary')
    positives:Optional[str]=Field(description='what are the positive effects')
    negatives:Optional[str]=Field(description='what are the negative effects')
    overall_sentiment : Optional[Literal['positive','negative','cautionary','nuetral']]= Field(description='write the sentiment of the article')
    
structured_output = model.with_structured_output(review) 

story= """The world of software development 
is undergoing a profound transformation, spearheaded by the emergence and increasing sophistication of
Artificial Intelligence (AI) coding assistants. These powerful tools, leveraging the capabilities of 
Large Language Models (LLMs) and advanced machine learning algorithms, are reshaping how developers interact with code, 
from inception to deployment.
While promising a future of enhanced productivity, reduced errors, and greater accessibility to the craft of programming, 
the integration of AI coding assistants also presents unique challenges and demands a thoughtful approach to ensure their 
responsible and effective use.
At their core, AI coding assistants function as intelligent companions to developers, seamlessly integrated into popular 
development environments (IDEs) to provide real-time suggestions, automate repetitive tasks, and identify potential issues
within the code. Tools like GitHub Copilot, Amazon Q Developer, and Tabnine, for example, are adept at predicting and completing 
lines of code, generating boilerplate structures, detecting errors, and even suggesting optimizations based on extensive datasets 
of publicly available code. This augmentation of human capabilities translates into a significant boost in productivity, 
allowing developers to allocate more time to complex problem-solving, innovative design, and high-level architectural 
considerations rather than the mundane aspects of coding.
However, the transformative power of AI coding assistants is not without its complexities. Concerns surrounding the potential 
for over-reliance on these tools, which could lead to a decline in developers' fundamental coding skills, are frequently raised. 
There are also valid ethical considerations, such as the potential for bias ingrained within the training data of AI models 
to manifest in generated code, notes Upwork. Questions of intellectual property and code quality also emerge, necessitating 
diligent human oversight, thorough testing, and robust code reviews to ensure the reliability and security of AI-generated 
code, according to SonarSource.
Despite these challenges, the trajectory of AI in software development points towards even greater integration and autonomy. 
Future AI systems may be capable of generating entire applications from high-level specifications, continuously optimizing and 
refactoring codebases based on performance metrics, and actively participating in development teams as collaborative partners. 
This shift will require developers to adapt their skills, focusing more on understanding AI principles, crafting effective prompts,
and critically evaluating AI-generated outputs, transitioning their roles from mere code writers to architects, overseers, and
innovators.
Ultimately, the future of coding is likely to be a harmonious blend of human creativity and AI-powered efficiency.
By embracing AI coding assistants as valuable tools that augment human capabilities, fostering a culture of continuous
learning and adaptation, and prioritizing ethical considerations throughout the development lifecycle, software developers 
can harness the immense potential of AI to build better, more innovative software solutions, ushering in a new era of
unprecedented efficiency and creativity in the world of programming"""
   
    
result = structured_output.invoke(story)


print(result)
    
    
    
    




