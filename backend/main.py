#main.py 

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router

def include_router(app):
	app.include_router(general_pages_router)


def configure_static(app):  #to support static files
	"""
		Basically, we are informing fastapi that we are going to keep all our static files in a folder named 'static' 
		and whenever it has to search for a static file, say an image, don't search here and there. 
		It will be inside static folder only
	"""
	app.mount("/static", StaticFiles(directory="static"), name="static")



def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	return app 


app = start_application()