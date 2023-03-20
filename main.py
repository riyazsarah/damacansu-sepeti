import uvicorn
import argparse
from api.newapp import new_app

mongo_connection_string = "mongodb://localhost:27017"
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", type=str, default="127.0.0.1", help="Host address")
    parser.add_argument("-port", type=int, default=8000, help="Port to listen on")
    parser.add_argument("-dbuser", type=str, default="", help="Database username")
    parser.add_argument("-dbpass", type=str, default="", help="Database password")
    parser.add_argument("-dbhost", type=str, default="localhost", help="Database host")
    parser.add_argument("-dbport", type=int, default=27017, help="Database port")
    parser.add_argument("-dbname", type=str, default="defaultdb", help="Database name")
    args = parser.parse_args()
    global mongo_connection_string
    if "localhost" in args.dbhost and args.port != 27017:
        # set the mongo connection string to localhost, and set it on global
        mongo_connection_string = f"mongodb://{args.dbhost}:{args.dbport}"
    else:
        mongo_connection_string = f"mongodb://{args.dbuser}:{args.dbpass}@{args.dbhost}:{args.dbport}/{args.dbname}"
    uvicorn.run(new_app(), host=args.host, port=args.port)
