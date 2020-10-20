from . import auto_deploy_demo

def test_auto_deploy_demo():
    assert auto_deploy_demo.apply("Jane") == "hello Jane"
