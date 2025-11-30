from prompt import Prompt
from tools import file_tools
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from jinja2 import Template
from pydantic import BaseModel, Field
import os

from dotenv import load_dotenv
load_dotenv()



# ------------------------------------------- #
#               Output Format                 #
# ------------------------------------------- #
class Output(BaseModel):
  name: str
  arguments: dict

# -------------------------------------------- #
#               Agent Class                    #
# -------------------------------------------- #
class Agent:
  def __init__(self, system_instructions:str, tools):

    self.model = ChatOpenAI(
        model = os.environ["LLM"],
        api_key = os.environ["API_KEY"],
        base_url = os.environ["BASE_URL"],
        streaming = True,
        response_format={"type": "json_object"}
    ).with_structured_output(Output)

    self.contents = None
    self.system_instructions_template = system_instructions
    self.tools = tools
    self.prompt_variables = {"tools":tools}
  
  def render_yaml_template(self, file_content, variables):
    template = Template(file_content)
    rendered = template.render(**variables)
    return rendered

  def forward(self, message:str):

    # Update Context ------------ >
    if self.contents == None:
      self.contents = [
          SystemMessage(content=self.render_yaml_template(self.system_instructions_template, self.prompt_variables))
      ]

    self.contents.append(HumanMessage(content=message))

    # Call model
    res = self.model.invoke(self.contents)


    if res.name != "final_answer":
      functions_responses = []
      for tool in self.tools:
        if tool == res.name:
          result = {"result":self.tools[res.name]['function'](**res.arguments)}
        else:
          result = {"error": "Tool not found"}
        functions_responses.append(AIMessage(str(result)))

      return self.forward("\n".join([msg.content for msg in functions_responses]))
    return res.arguments
  
agent = Agent(
    system_instructions = Prompt,
    tools = file_tools
)

if __name__ == "__main__":
  question = input("Ask Anything ==================== \n")
  print(agent.forward(question))