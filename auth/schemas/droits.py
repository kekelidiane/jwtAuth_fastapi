from enum import Enum
from pydantic import BaseModel, Field

class DroitEnum(Enum):
    CONFIGURER_SITE = "configurer le site"
    PUBLIER_ANNONCES = "publier des annonces"
    SUPPRIMER_ANNONCES = "supprimer des annonces"



