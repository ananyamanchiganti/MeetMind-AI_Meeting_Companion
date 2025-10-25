from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import subprocess
import os

app = FastAPI()

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Save uploaded file locally
        audio_path = file.filename
        with open(audio_path, "wb") as f:
            f.write(await file.read())

        # Run your existing openaiwhisper.py script
        result = subprocess.run(
            ["python", "openaiwhisper.py"],
            capture_output=True,
            text=True
        )

        # Capture printed output from that script
        output = result.stdout

        # Save transcript text into a file
        output_path = f"{audio_path}_transcript.txt"
        with open(output_path, "w", encoding="utf-8") as out:
            out.write(output)

        return JSONResponse(content={
            "message": "Transcription successful",
            "transcript_file": output_path,
            "output_preview": output[:500]  # show first part only
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
