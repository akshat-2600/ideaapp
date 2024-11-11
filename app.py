from flask import Flask


app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=8080)

#Create the idea repository

ideas = {
    1 : {
        "id" : 1,
        "idea_name" : "ONDC",
        "idea_description" : "Details about ONDC",
        "idea_author" : "Adeeb"
    },
    2: {
        "id" : 2,
        "idea_name" : "Save Soil",
        "idea_description" : "Details about Saving Soil",
        "idea_author" : "Ankit Sharma"
    }
}

'''
Create an RESTful endpoint for fetching all the ideas
'''

@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    #Logic to fetch all the ideas
    return ideas

