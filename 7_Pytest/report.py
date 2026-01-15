import json

def generate_report():
    """
    Generate report data
    """

    dt = {
        "timestamp": "2024-06-01T12:00:00",
        "status": "PASSED",
        "summary": "module.py::test_case"
    }

    with open("report.json", "w") as file:
        # write data to json file
        json.dump(dt, file)