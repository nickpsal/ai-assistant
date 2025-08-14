from livekit.agents import function_tool, RunContext
import subprocess
import platform

@function_tool()
async def open_application(context: RunContext, app_name: str) -> str:
    """
    Άνοιξε μια τοπική εφαρμογή με βάση το όνομά της.
    Π.χ. 'notepad', 'calc'.
    """
    try:
        if platform.system() == "Windows":
            subprocess.Popen([app_name])
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", app_name])
        else:  # Linux
            subprocess.Popen([app_name])
        return f"Άνοιξα το {app_name}."
    except Exception as e:
        return f"Δεν κατάφερα να ανοίξω το {app_name}: {e}"