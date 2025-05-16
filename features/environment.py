# from src.core.driver_factory import WebdriverFactory

# def before_all(context):
#     pass

# def before_feature(context, feature):
#     pass

def after_scenario(context, scenario):
    context.driver.close()
    # context.driver.quit()

# def after_feature(context, feature):
#     pass

# def after_all(context):
#     context.driver.quit()
