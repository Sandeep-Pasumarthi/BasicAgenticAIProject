import json
import os

CONFIG_PATH = os.path.join(os.getcwd(), "src", "basic", "ui", "config.json")

class Config:
    def __init__(self, config_file=CONFIG_PATH):
        with open(config_file, "r", encoding="utf-8") as file:
            self.config = json.load(file)
    
    def get_page_title(self) -> str:
        return self.config.get("PAGE_TITLE", "")

    def get_llms_details(self) -> dict:
        return self.config.get("LLMS", {})

    def get_usecase_options(self) -> list:
        return self.config.get("USECASE_OPTIONS", {})
