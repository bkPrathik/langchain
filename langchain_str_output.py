from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated

# i will be using ollama models (i love running locally LOL!)
model = ChatOllama(model='llama3.2:3b')  #need to check what all models support structured output, not all models support it.
class Story_moral(TypedDict):
    
    #cannot force datatype in this method ,can;t expect string always 
    moral:Annotated[str,'a meaningfull moral summary of the story']   #to get the moral of  the story , same can be done to find the snetiment of the setence
    
structured_output = model.with_structured_output(Story_moral)  #with_structured_output is used for those models that support str otpt


stroy = """A hungry fox spots a luscious bunch of grapes hanging from a high vine. His mouth waters at the sight,
and he eagerly tries to leap and snatch them.
However, no matter how many times he jumps and stretches, 
the grapes remain out of his reach. 
Growing tired, frustrated, and unable to get the grapes,
the fox finally gives up. As he walks away, he scoffs, 
"Those grapes are probably sour anyway!"
He pretends that he never wanted them in the first place, 
or that they weren't worth the effort to obtain"""


result = structured_output.invoke(stroy)


print(result['moral'])