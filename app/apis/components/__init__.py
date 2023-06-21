
# from Freelance.upwork-33841525.app.apis.components.utils import get_config_file_name
from app.apis.components.utils import get_config_file_name

def init_components(*, application, environment:str):
    load_config(application=application, env_name=environment)    
    #initialize any other components like Database etc. here
    

def load_config(*, application, env_name: str):
    config_file_name: str = get_config_file_name(environment=env_name)
    application.config.from_object(f'config.{env_name}.{config_file_name}')    
