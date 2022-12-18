import os
from app.app import app

port = int(os.environ.get('PORT', 8080)) # runs on port 8080

if __name__ == '__main__':
#     # we want the server to be multi-threaded
	app.run(threaded=True, host='0.0.0.0', port=port)