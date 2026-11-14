import ollama

#1 Role
system_role_content = "You are a wildlife travel writer from south india travel blog."

#2 Task
user_role_content_v1 = "Write an introduction to karnataka's wildlife for first time visitor."

#3 Constraints
user_role_content_v2 = """
                        Write an introduction to karnataka's wildlife for first time visitor.
                           150 words.
                           Audience: city dwellers who have never been on a safari.
                           warm ,vivid tone. Exactly 3 parks . No jorgan. 
                            
                        """
#4 Format
user_role_content_v3 = """
                        Write an introduction to karnataka's wildlife for first time visitor.
                           150 words.
                           Audience: city dwellers who have never been on a safari.
                           warm ,vivid tone. Exactly 3 parks . No jorgan. 
                        Format : three bullets(park,signature animal,best month)then one line closing tip.
                        """

#5 Examples
# one shot prompting 

user_role_content_v4 = """
                        Write an introduction to karnataka's wildlife for first time visitor.
                           150 words.
                           Audience: city dwellers who have never been on a safari.
                           warm ,vivid tone. Exactly 3 parks . No jorgan. 
                        Format : three bullets(park,signature animal,best month)then one line closing tip.
                        Example :Mysuru shukavana: Birds sings , which is a thearpy.Best time - nov-dec
                        """

# Prompting types

#1 Zero shot prompting
user_role_content_v5 = "Write a one line bullet about Dandeli travel blog, with best time to visit."

#2 Few shot prompting 
user_role_content_v6 = """Write bullet in this style, then do dandeli.
        Bandipur: Wild elephants graZe at dusk along the forest edge.Best in nov-feb.
        Nagarhole:Tiger prowl the tall grass by kabini backwater.Best in march-may.
        Dandeli:
"""

#3 Think first prompting
user_role_content_v7 = """
    I have 3 days time, starting from banglore, i want see elephants and tigers and waterfalls, think through travel season time , and then reccomend parks.
"""

message = [
    {
        "role": "system",
        "content" : system_role_content
    },
    {
        "role" : "user",
        "content" : user_role_content_v7
    }
]

modell = "llama3.2:latest"
res = ollama.chat(model = modell , messages = message)
print(res.message.content)