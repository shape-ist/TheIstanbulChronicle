def load_content(yaml_file):
    import yaml
    with open(yaml_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise Exception(e.message)