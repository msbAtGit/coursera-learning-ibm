
"""
Experimenting with flask for learning
"""
from flask import Flask,make_response,request

app = Flask(__name__)
data = [
        {
            "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
            "first_name": "Tanya",
            "last_name": "Slad",
            "graduation_year": 1996,
            "address": "043 Heath Hill",
            "city": "Dayton",
            "zip": "45426",
            "country": "United States",
            "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
        },
        {
            "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
            "first_name": "Ferdy",
            "last_name": "Garrow",
            "graduation_year": 1970,
            "address": "10 Wayridge Terrace",
            "city": "North Little Rock",
            "zip": "72199",
            "country": "United States",
            "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
        },
        {
            "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
            "first_name": "Lilla",
            "last_name": "Aupol",
            "graduation_year": 1985,
            "address": "637 Carey Pass",
            "city": "Gainesville",
            "zip": "32627",
            "country": "United States",
            "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
        },
        {
            "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
            "first_name": "Abdel",
            "last_name": "Duke",
            "graduation_year": 1995,
            "address": "2 Lake View Point",
            "city": "Shreveport",
            "zip": "71105",
            "country": "United States",
            "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
        },
        {
            "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
            "first_name": "Corby",
            "last_name": "Tettley",
            "graduation_year": 1984,
            "address": "90329 Amoth Drive",
            "city": "Boulder",
            "zip": "80305",
            "country": "United States",
            "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
        }
    ]

@app.route("/")
def index():
    return "hello world"


@app.route("/no_content")
def no_content_func():
    response = {"message": "no content found"}
    return (response, 204)

@app.route("/exp")
def index_explicit():
    resp = make_response({"message": "hello world"})
    resp.status_code = 200
    return resp

@app.route("/data")
def get_data():
    
    try:
        
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404


@app.route("/name_search")
def name_search():
    """Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If argument 'q' is missing
        422: If argument 'q' is present but invalid
    """
    #Get the argument 'q' 
    #from the query parameters of the request
    query = request.args.get('q')
    
    if query is None or query == "":
        return ({"message":"Invalid input parameter"}, 400)
   
    for entry in data:
        if entry["first_name"].lower() == query.lower():
            return (entry, 200)
    else:
        return ({"message":"Person not found"}, 404)


@app.route("/count")
def get_data_count():
    response_msg = {"data count": len(data)}
    return response_msg

@app.route("/person/<uuid>")
def find_by_uuid(uuid):
    """
    Name: 
        find_by_uuid
    Returns:
        Which matches the UUID passed as parameter
    """

    for entry in data:
        if entry["id"] == uuid:
            return entry
    else:
        response_obj = make_response()
        response_obj.status = 404
        return response_obj

@app.route("/person/<uuid>", methods=["DELETE"])
def delete_by_uuid(uuid):
    response_obj=None
    for entry in data:
        if entry["id"] == uuid:
            data.remove(entry)
            response_obj = make_response({"message": f"Person with ID {uuid} deleted"})
            response_obj.status = 200
            return response_obj
    else:
        response_obj = make_response()
        response_obj.status = 404
        return response_obj

@app.route("/person", methods=['POST'])
def create_person():
    # Get the JSON data from the incoming request
    new_person = request.get_json()

    # Check if the JSON data is empty or None
    if not new_person:
        # Return a JSON response indicating that the request data is invalid
        # with a status code of 422 (Unprocessable Entity)
        return {"message": "Invalid input, no data provided"}, 422

    # Proceed with further processing of 'new_person', such as adding it to a database
    # or validating its contents before saving it
    data.append(new_person)
    # Assuming the processing is successful, return a success message with status code 200 (Created)
    return {"message": "Person created successfully"}, 200

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500