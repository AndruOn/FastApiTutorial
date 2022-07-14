# FastApiTutorial

## Installation

create a ptyhon virtual environnement and install all the needed libraries


RUn from the project root 
```
#first time
conda create -p env python=3.9
conda install -p env --file backend/requirements.txt

#when use env from new terminal
conda activate ./env
cd backend
uvicorn main:app --reload

```
 
## Used ressources (bibliography)


tutorial from https://www.fastapitutorial.com/blog/fastapi-course/
navbar.html https://getbootstrap.com/docs/5.0/components/navbar/