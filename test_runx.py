import subprocess
import time
import os
import tempfile

def test_runx_execution():
    with tempfile.TemporaryDirectory() as tmpdir:
        marker_file = os.path.join(tmpdir, "marker.txt")
        # Command that sleeps briefly then touches marker file
        cmd = ["python3", "-c", f"import time; time.sleep(0.5); open(r'{marker_file}', 'w').write('ok')"]
        
        # Execute via runx.py
        result = subprocess.run(["python3", "runx.py"] + cmd, capture_output=True, text=True)
        assert result.returncode == 0
        
        # Wait for marker file to appear
        start_time = time.time()
        while time.time() - start_time < 3.0:
            if os.path.exists(marker_file):
                break
            time.sleep(0.1)
            
        assert os.path.exists(marker_file), "Spawned process failed to execute or write marker file"
        content = open(marker_file).read()
        assert content == "ok"

if __name__ == "__main__":
    test_runx_execution()
    print("All tests passed successfully!")
