def load_content():
    import yaml
    with open("content.yaml", 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise Exception(e.message)