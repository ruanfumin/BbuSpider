from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

config_dict = {
    "host": cfg.get('mysql', 'host'),
    "port": cfg.get('mysql', 'port'),
    "user": cfg.get('mysql', 'user'),
    "password": cfg.get('mysql', 'password'),
    "database": cfg.get('mysql', 'database')
}

MySQLURI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(**config_dict)
