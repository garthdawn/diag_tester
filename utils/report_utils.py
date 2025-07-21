import allure

def attach_text(text: str, name: str):
    """Attach text to Allure report"""
    allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)