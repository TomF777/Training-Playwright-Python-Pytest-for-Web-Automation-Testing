import report
import json

def test_report_json():
    report.generate_report()
    
    with open("report.json", "r") as file:
        dt = json.load(file)
        
        assert type(dt) == dict


def test_report_fields():
    report.generate_report()
    
    with open("report.json", "r") as file:
        dt = json.load(file)

        assert "timestamp" in dt
        assert "status" in dt