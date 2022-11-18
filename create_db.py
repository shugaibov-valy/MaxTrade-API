from db import Base, config_, engine
from components.models import *

Base.metadata.create_all(engine)