from dotenv import load_dotenv
from agents import Agent, Runner, RunContextWrapper, function_tool, input_guardrail,TResponseInputItem, GuardrailFunctionOutput, enable_verbose_stdout_logging
from pydantic import BaseModel

load_dotenv()
enable_verbose_stdout_logging()


class Accounts(BaseModel):
    name: str
    pin: int


class My_output(BaseModel):
    name: str
    balance: int


class Guardial_output(BaseModel):
    is_bank_related:bool


gaurdial_agent=Agent(
    name="gaurdial_agent",
    instructions="you are gaurdial_agent. you check if the user is asking you bank related queries or not.",
    output_type=Guardial_output
)


@input_guardrail
async def check_bank_related(ctx: RunContextWrapper[None], user_input: str
)-> GuardrailFunctionOutput:
    result = await Runner.run(gaurdial_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_bank_related
    )


def check_user(ctx: RunContextWrapper[Accounts],agent: Agent) -> bool:
    if ctx.context.name =="Laiba" and ctx.context.pin==7252:
        return True
    else:
        return False


@function_tool(is_enabled=check_user)
def check_balance(account_number: str) -> str:
    """
    Function to check the balance of a bank account.
    """
    # Simulate checking balance logic
    return f"The balance for account {account_number} is $1000."


def dynamic_instruction(ctx:RunContextWrapper[Accounts],agent:Agent):
    return f"user name is{ctx.context.name} and pin is {ctx.context.pin} check the user name and pin if its correct use the balance check tool to check thier balance."


bank_agent = Agent(
    name= "bank_agent",
    # Instruction= "you are bank agent. You help customer with their question you can use the tools to get the information you need. ",
    instructions="dynamic_instruction",
    tools=[check_balance],
    input_guardrails=[check_bank_related],
    model_settings=ModelSettings(temperature=0.2,toolchoice="reqired"),
    reset_tool_choice=True
)


user_context = Accounts(name="Laiba", pin=7252)


result = Runner.run_sync(bank_agent, "I want to check my balance for account 7252.", context=user_context)


print(result.final_output)

#                                   ----------------x---------------x-------------




from dotenv import load_dotenv
from agents import Agent, Runner , function_tool, RunContextWrapper,input_guardrail,GuardrailFunctionOutput, enable_verbose_stdout_logging,ModelSettings
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


enable_verbose_stdout_logging()



class Account(BaseModel):
    name: str
    pin: int



class Guardrail_output(BaseModel):
    isNot_bank_related:bool



guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="check if the user is asking you bank related quries.",
    output_type=Guardrail_output,
)


@input_guardrail
async def check_bank_related(ctx:RunContextWrapper[None],agent:Agent,input:str)->GuardrailFunctionOutput:
   
   result = await Runner.run(guardrail_agent,input,context=ctx.context)
   return GuardrailFunctionOutput(
       output_info=result.final_output,
       tripwire_triggered=result.final_output.isNot_bank_related
    )
   

def check_user(ctx:RunContextWrapper[Account],agent:Agent)->bool:
    if ctx.context.name == "Laiba" and ctx.context.pin == 7252:
        return True
    else:
        return False


@function_tool(is_enabled=check_user)
def check_balance(account_number: str) -> str:
    return f"The balance of account is $1000000"


def dynamic_instruction(ctx:RunContextWrapper[Account],agent:Agent):
    return f"user name is {ctx.context.name}  check the users name if its correct use the balance check tool to check thier balance"


bank_agent = Agent(
    name="Bank Agent",
    instructions=dynamic_instruction,
    tools=[check_balance],
    input_guardrails=[check_bank_related], 
    model_settings=ModelSettings(
        temperature=0.2,
          tool_choice='required',
          max_tokens=1000,
          parallel_tool_calls=None,
          frequency_penalty = 0.3,
          presence_penalty = 0.2
          ),
    reset_tool_choice=False,
    tool_use_behavior='run_llm_again'
)


user_context = Account(name="Laiba", pin=7252)


result = Runner.run_sync(bank_agent, "what is my balance my account 93849348", context=user_context,max_turns=3)


print(result.final_output)