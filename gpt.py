import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey = apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def getNewProject(self, prompt):
        ''' Generate a GPT response to give you a new project to create '''
        prompt = "What are some simple " + prompt + " projects I can create to get better at making " + prompt + ":\n\n"
        completion = openai.Completion.create(
        engine=self.model_engine,
        prompt=prompt,
        max_tokens=25,
        n=3,
        stop="\n",
        temperature=0.8,
    )

        responses = completion.choices
        formatted_responses = []
        for response in responses:
            formatted_response = "<p>" + response.text.strip() + "</p>"
            formatted_responses.append(formatted_response)

        return "\n".join(formatted_responses)

    
if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))