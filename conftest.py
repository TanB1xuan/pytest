#content of conftest.py



'''
    record property with custom markers'''

'''def pytest_collection_modifyitems(session, config, items):
    for item in items:
        for marker in item.iter_markers(name = "test_id2"):
            test_id = marker.args[0]
            item.user_properties.append(("test_id", test_id))'''